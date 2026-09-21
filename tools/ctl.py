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
                        Enter on pauses, "coup" on Coup-round prompts, and
                        draws event cards itself (tools/deck.py) when the
                        program asks for a card number. Stops at the first
                        prompt that needs a human decision. Prints everything.
                        Set FITL_MANUAL_DECK=1 to stop at card prompts instead
                        (a human then supplies the number with `send`).
  seq <step> [<step>...]
                        Answer several prompts in one call, each guarded:
                        a step is "<expected text>=><answer>". The expected
                        text must appear in the current prompt block (the
                        output since the previous answer) or the sequence
                        stops there and prints the screen. An answer of
                        "#<label>" picks the menu entry whose label starts
                        with <label>, so menus that renumber are safe. An
                        empty answer presses Enter. "Press Enter" pauses
                        between steps are handled automatically.
                        Example:
                          seq "Choose one=>#Op" "Choose operation=>#Train" \
                              "Train in which space=>#Saigon" \
                              "Training in Saigon=>#Place Irregulars" \
                              "how many Irregulars=>2" \
                              "US Training=>#Finished selecting" \
                              "final Train action=>#Finished" \
                              "special activity=>n"
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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SESSION = "fitl"
GAMEFILE = os.path.join(ROOT, ".ctl-game")
MANUAL_DECK = os.environ.get("FITL_MANUAL_DECK") == "1"
CARD_PROMPT_RE = re.compile(r"Enter the number of the (1st|2nd|next On Deck) Event card:")
TRANSCRIPT = os.path.join(ROOT, "transcript.log")
CURSOR = os.path.join(ROOT, ".ctl-cursor")
BLOCK = os.path.join(ROOT, ".ctl-block")     # transcript offset at the last send
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


def mark_block():
    """Remember where the transcript stood when the last answer was sent, so
    'the current prompt block' is exactly what the program printed since."""
    with open(BLOCK, "w") as f:
        f.write(str(transcript_size()))


def current_block():
    try:
        with open(BLOCK) as f:
            off = int(f.read().strip() or 0)
    except FileNotFoundError:
        off = 0
    text, _ = read_since(off)
    return text


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
    with open(BLOCK, "w") as f:
        f.write("0")
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
    if not MANUAL_DECK and CARD_PROMPT_RE.search(last_nonblank_screen_line()):
        print("ERROR: the program is asking for a card number. Card draws are automatic: run `advance`.")
        return 1
    mark_block()
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
    set_game(name)
    print("\n[ctl] new game created. Run `advance` to draw the first two cards and start play.")
    return 0


def set_game(name):
    with open(GAMEFILE, "w") as f:
        f.write(name)


def current_game():
    try:
        with open(GAMEFILE) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def cards_seen_so_far():
    """The cards drawn so far, from the program's latest save (the save is
    written before the program asks for a card) or, before the first save
    exists, from the program's own echo of the first card in the transcript."""
    import fitl_state as S
    game = current_game()
    if game and S.save_numbers(game):
        state = S.load_save(S.save_path(game, S.save_numbers(game)[-1]))
        return list(state["cardsSeen"])
    text, _ = read_since(0)
    m = re.findall(r"Enter the number of the 1st Event card:\s*(\d+)", text)
    return [int(m[-1])] if m else []


def auto_draw():
    """Answer a card prompt with a fresh draw from deck.py."""
    import deck
    seen = cards_seen_so_far()
    d = deck.Deck(deck.load_periods())
    where = d.explain(seen)
    card = d.next_card(seen)
    print(f"\n[deck] {where} -> drew #{card}")
    return send_raw(str(card))


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
    set_game(name)
    print(f"\n[ctl] resumed '{name}' from its latest save.")
    return 0


def send_raw(text, echo=False):
    mark_block()
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
        elif CARD_PROMPT_RE.search(last):
            if MANUAL_DECK:
                break
            print(auto_draw(), end="")
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


def cmd_seq(steps):
    """Guarded multi-answer send. See the module docstring."""
    if not running():
        print("ERROR: program is not running.")
        return 1
    parsed = []
    for st in steps:
        if "=>" not in st:
            print(f"ERROR: step {st!r} is not of the form 'expected=>answer'")
            return 2
        exp, ans = st.split("=>", 1)
        parsed.append((exp.strip(), ans.strip()))
    # The current prompt block is everything the program printed since the
    # last answer was sent (never the whole screen: stale menus above the
    # current one would otherwise match a label and give the wrong number).
    pending, off = read_since(read_cursor())
    write_cursor(off)
    print(pending, end="")
    block = current_block()
    for k, (exp, ans) in enumerate(parsed, 1):
        # step over pauses the program inserts between narration and prompt
        guard = 0
        while "Press Enter to continue" in last_nonblank_screen_line() and guard < 20:
            out = send_raw("")
            print(out, end="")
            block = out
            guard += 1
        if not MANUAL_DECK and CARD_PROMPT_RE.search(last_nonblank_screen_line()):
            print(f"\n[ctl] seq stopped before step {k}: the program wants a card number; run `advance`.")
            return 1
        if exp and exp.lower() not in block.lower():
            print(f"\n[ctl] seq stopped at step {k} ({exp!r} => {ans!r}): expected text not in the "
                  f"current prompt. Nothing sent for this step. Current screen:\n")
            print(screen_text().rstrip())
            return 1
        if ans.startswith("#"):
            num = menu_number(block, re.escape(ans[1:]))
            if num is None:
                print(f"\n[ctl] seq stopped at step {k}: no menu entry starting with {ans[1:]!r}. "
                      f"Nothing sent for this step. Current screen:\n")
                print(screen_text().rstrip())
                return 1
            print(f"\n[ctl] step {k}: {ans} -> {num}")
            ans = num
        out = send_raw(ans)
        print(out, end="")
        block = out
    print(f"\n[ctl] seq finished {len(parsed)} steps; stopped at: {last_nonblank_screen_line()}")
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
    if cmd == "seq":
        return cmd_seq(args)
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
