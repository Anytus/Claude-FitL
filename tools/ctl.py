#!/usr/bin/env python3
"""ctl.py - hold the fitl program in a persistent tmux session and talk to it.

Commands
  start                 Launch the program (fails if already running).
  status                Is it running? Where is the read cursor? Last lines.
  read                  Print output produced since the last read (ANSI stripped).
  read --all            Print the whole transcript since start.
  screen                Print the current visible tmux pane (what a human sees).
  send <text>           Type <text> + Enter, wait for output to settle, print it.
  send ""               Just press Enter (for "Press Enter to continue" pauses).
  enter                 Same as send "".
  advance               Run bot turns: answers "perform" on Bot-turn prompts,
                        Enter on pauses, "coup" on Coup-round prompts. Stops at
                        the first prompt that needs a human decision or a card
                        number. Prints everything the program wrote.
  new-game <name>       Scripted setup: Full scenario, 1 human (US),
                        human may win in any Coup Victory phase, game name.
  resume <name>         Scripted: pick "Resume '<name>'" at the startup menu.
  stop                  Kill the tmux session (only between sessions / for tests).

All output the program has ever written goes to transcript.log (append-only,
via tmux pipe-pane). `read` walks a byte offset stored in .ctl-cursor.
The program is run from the repository root so saves land in ./games/<name>/.
"""
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION = "fitl"
TRANSCRIPT = os.path.join(ROOT, "transcript.log")
CURSOR = os.path.join(ROOT, ".ctl-cursor")
LIBDIR = os.path.join(ROOT, "fitl", "lib")
ANSI_RE = re.compile(r'\x1b\[[0-9;?]*[A-Za-z]|\x1b\][^\x07]*\x07|\r')

# How long output must be quiet before `send` returns, and the hard cap.
SETTLE_SECS = 0.6
MAX_WAIT_SECS = 60.0


def tmux(*args, check=True, capture=True):
    return subprocess.run(["tmux", *args], check=check,
                          capture_output=capture, text=True)


def running():
    return subprocess.run(["tmux", "has-session", "-t", SESSION],
                          capture_output=True).returncode == 0


def read_cursor():
    try:
        with open(CURSOR) as f:
            return int(f.read().strip() or 0)
    except FileNotFoundError:
        return 0


def write_cursor(n):
    with open(CURSOR, "w") as f:
        f.write(str(n))


def transcript_size():
    try:
        return os.path.getsize(TRANSCRIPT)
    except FileNotFoundError:
        return 0


def read_since(offset):
    if not os.path.exists(TRANSCRIPT):
        return "", 0
    with open(TRANSCRIPT, "rb") as f:
        f.seek(offset)
        data = f.read()
    return ANSI_RE.sub("", data.decode("utf-8", errors="replace")), offset + len(data)


def cmd_start():
    if running():
        print("ERROR: program already running. Use `read`/`send`. Never relaunch mid-game.")
        return 1
    if not os.path.isdir(LIBDIR):
        print(f"ERROR: {LIBDIR} not found")
        return 1
    # Fresh transcript per launch; the old one is kept with a timestamp.
    if os.path.exists(TRANSCRIPT):
        os.rename(TRANSCRIPT, TRANSCRIPT + "." + time.strftime("%Y%m%d-%H%M%S"))
    write_cursor(0)
    # JAVA_TOOL_OPTIONS is sandbox proxy chatter the program does not need.
    java = 'env -u JAVA_TOOL_OPTIONS TERM=dumb java -cp "fitl/lib/*" fitl.FireInTheLake'
    tmux("new-session", "-d", "-s", SESSION, "-x", "200", "-y", "50",
         "-c", ROOT, java)
    subprocess.run(["tmux", "set-option", "-t", SESSION, "remain-on-exit", "on"], check=True)
    tmux("pipe-pane", "-t", SESSION, "-o", f"cat >> '{TRANSCRIPT}'")
    out = wait_settle()
    print(out, end="")
    return 0


def wait_settle(settle=SETTLE_SECS, max_wait=MAX_WAIT_SECS):
    """Block until the transcript stops growing, then return the new text."""
    start = time.time()
    last = transcript_size()
    last_change = time.time()
    while True:
        time.sleep(0.15)
        now = transcript_size()
        if now != last:
            last, last_change = now, time.time()
        elif time.time() - last_change >= settle and now > read_cursor():
            break
        if time.time() - start > max_wait:
            break
        if not running():
            break
    text, new_off = read_since(read_cursor())
    write_cursor(new_off)
    return text


def cmd_send(text):
    if not running():
        print("ERROR: program is not running. Use `status`, then `start`/`resume` if needed.")
        return 1
    if text:
        tmux("send-keys", "-t", SESSION, "-l", text)
    tmux("send-keys", "-t", SESSION, "Enter")
    print(wait_settle(), end="")
    return 0


def cmd_read(all_=False):
    if all_:
        text, _ = read_since(0)
        print(text, end="")
        return 0
    text, new_off = read_since(read_cursor())
    write_cursor(new_off)
    print(text, end="")
    return 0


def cmd_screen():
    if not running():
        print("ERROR: program is not running.")
        return 1
    r = tmux("capture-pane", "-p", "-t", SESSION)
    print(r.stdout.rstrip("\n"))
    return 0


def cmd_status():
    alive = running()
    print(f"running: {alive}")
    print(f"transcript: {TRANSCRIPT} ({transcript_size()} bytes), cursor at {read_cursor()}")
    if alive:
        r = tmux("capture-pane", "-p", "-t", SESSION)
        lines = [l for l in r.stdout.rstrip("\n").splitlines() if l.strip()]
        print("last lines on screen:")
        for l in lines[-8:]:
            print("  " + l)
    return 0


def expect(pattern, text, what):
    if not re.search(pattern, text):
        print(f"\nERROR: expected {what!r} but did not see it. Output was:\n{text}")
        return False
    return True


def menu_number(text, label_regex):
    """Find 'N) <label>' in a menu and return N as a string."""
    m = re.search(r'^\s*(\d+)\)\s*' + label_regex, text, re.M)
    return m.group(1) if m else None


def cmd_new_game(name):
    if not running():
        rc = cmd_start()
        if rc:
            return rc
    text, _ = read_since(0)
    # If saved games exist the program first asks which game to play.
    if "Which game would you like to play" in text:
        n = menu_number(text, r"Start a new game")
        out = send_raw(n, echo=True)
        text = out
    if not expect(r"Choose a scenario", text, "scenario menu"):
        return 1
    out = send_raw(menu_number(text, r"Full: 1964-1972"), echo=True)
    if not expect(r"How many factions will be played by human players", out, "human count prompt"):
        return 1
    out = send_raw("1", echo=True)
    if not expect(r"Select the human faction", out, "faction menu"):
        return 1
    out = send_raw(menu_number(out, r"US\s*$"), echo=True)
    if not expect(r"Allow human faction to win in Victory phase", out, "human-win prompt"):
        return 1
    out = send_raw("y", echo=True)
    if not expect(r"Enter a name for your new game", out, "game name prompt"):
        return 1
    out = send_raw(name)
    if "already exists" in out:
        print("ERROR: a game with that name already exists. Refusing to overwrite.")
        send_raw("n")
        return 1
    print(out, end="")
    print("\n[ctl] new game created; the program now wants the first two card numbers.")
    return 0


def cmd_resume(name):
    if running():
        print("ERROR: program already running; nothing to resume. Use `read`/`status`.")
        return 1
    rc = cmd_start()
    if rc:
        return rc
    text, _ = read_since(0)
    if not expect(r"Which game would you like to play", text, "resume menu"):
        return 1
    n = menu_number(text, r"Resume '" + re.escape(name) + r"'")
    if n is None:
        print(f"ERROR: no saved game named {name!r} in the menu:\n{text}")
        return 1
    out = send_raw(n)
    print(out, end="")
    print(f"\n[ctl] resumed '{name}' from its latest save.")
    return 0


def send_raw(text, echo=False):
    if text:
        tmux("send-keys", "-t", SESSION, "-l", text)
    tmux("send-keys", "-t", SESSION, "Enter")
    out = wait_settle()
    if echo:
        print(out, end="")
    return out


def last_nonblank_screen_line():
    r = tmux("capture-pane", "-p", "-t", SESSION)
    lines = [l for l in r.stdout.splitlines() if l.strip()]
    return lines[-1] if lines else ""


def screen_text():
    return tmux("capture-pane", "-p", "-t", SESSION).stdout


def cmd_advance():
    """Drive bot turns until a human decision or card draw is needed."""
    if not running():
        print("ERROR: program is not running.")
        return 1
    # Print anything pending first so nothing is lost.
    pending, off = read_since(read_cursor())
    write_cursor(off)
    print(pending, end="")
    steps = 0
    while steps < 200:
        steps += 1
        last = last_nonblank_screen_line()
        scr = screen_text()
        # Find the header of the current prompt block (last '>>> ... <<<' line)
        headers = [l for l in scr.splitlines() if l.strip().startswith(">>>") and l.strip().endswith("<<<")]
        header = headers[-1] if headers else ""
        if "Press Enter to continue" in last:
            print(send_raw(""), end="")
        elif last.startswith("(perform or ?)") and "(Bot)" in header:
            print(send_raw("perform"), end="")
        elif last.startswith("(discard or ?)"):
            print(send_raw("discard"), end="")
        elif last.startswith("(coup or ?)"):
            print(send_raw("coup"), end="")
        else:
            break
    print(f"\n[ctl] stopped at: {last_nonblank_screen_line()}")
    return 0


def cmd_stop():
    if running():
        tmux("kill-session", "-t", SESSION)
        print("stopped")
    else:
        print("not running")
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    if cmd == "start":
        return cmd_start()
    if cmd == "status":
        return cmd_status()
    if cmd == "read":
        return cmd_read(all_=("--all" in args))
    if cmd == "screen":
        return cmd_screen()
    if cmd == "send":
        return cmd_send(" ".join(args))
    if cmd == "enter":
        return cmd_send("")
    if cmd == "advance":
        return cmd_advance()
    if cmd == "new-game":
        if not args:
            print("usage: ctl.py new-game <name>")
            return 2
        return cmd_new_game(" ".join(args))
    if cmd == "resume":
        if not args:
            print("usage: ctl.py resume <name>")
            return 2
        return cmd_resume(" ".join(args))
    if cmd == "stop":
        return cmd_stop()
    print(f"unknown command {cmd!r}\n{__doc__}")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
