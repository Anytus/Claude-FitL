#!/usr/bin/env python3
"""report.py - assemble the observer's report from the program's own records.

Usage:
  report.py                      everything since the last report, for the
                                 (single) game under games/
  report.py <game>               same, for that game
  report.py <game> <a> <b>       saves a+1 .. b
  report.py ... --stdout         print instead of writing the file

Writes reports/<game>/report-<first>-<last>.md containing, for every save in
the range: which card it was, what happened (the program's own summary), the
program's log lines verbatim (every placement, removal, shift, die roll and
Tru'ng check), and after the last save the trackers, sequence of play, cards
and scores from render.py. An index.md in the same directory lists reports.

The playing model runs this once per card and points the observer at the
file; it does not retype the narration into chat. reports/<game>/.last
remembers the last save reported so the default range is always "new since
last time".
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fitl_state as S
import render as R

ROOT = S.ROOT


def load_last(game):
    try:
        with open(os.path.join(ROOT, "reports", game, ".last")) as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_last(game, n):
    d = os.path.join(ROOT, "reports", game)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, ".last"), "w") as f:
        f.write(str(n))


def segment_header(state, i, cards):
    hist = {h["save_number"]: h for h in state["history"]}
    h = hist.get(i)
    card = h["card"] if h else f"#{state['currentCard']}"
    summary = " / ".join(h["summary"]) if h else ""
    return card, summary


def build(game, a, b):
    cards = S.load_cards()
    out = []
    w = out.append
    first_state = S.load_save(S.save_path(game, min(a + 1, b)))
    last_state = S.load_save(S.save_path(game, b))
    seen_cards = []
    for i in range(a + 1, b + 1):
        st = S.load_save(S.save_path(game, i))
        card, summary = segment_header(st, i, cards)
        if card not in seen_cards:
            seen_cards.append(card)
    w(f"# {game}: save-{a + 1:03d} to save-{b:03d}")
    w("")
    w("Cards: " + "; ".join(seen_cards))
    w("")
    for i in range(a + 1, b + 1):
        st = S.load_save(S.save_path(game, i))
        card, summary = segment_header(st, i, cards)
        w(f"## save-{i:03d} — {card} — {summary}")
        w(f"Current card #{st['currentCard']}, on deck #{st['onDeckCard'] or 'none'}")
        w("")
        lines = S.load_log(S.log_path(game, i))
        w("```")
        for line in lines:
            for sub in line.split("\n"):
                w(sub)
        w("```")
        w("")
    w(f"## Board after save-{b:03d}")
    w("")
    w("```")
    w(R.summary_sections(last_state, game, b, cards))
    w("```")
    return "\n".join(out) + "\n"


def main(argv):
    to_stdout = "--stdout" in argv
    argv = [x for x in argv if x != "--stdout"]
    game = None
    if argv and not argv[0].isdigit():
        game = argv[0]
        argv = argv[1:]
    if game is None:
        game = S.default_game()
    nums = S.save_numbers(game)
    if not nums:
        raise SystemExit(f"no saves for game {game!r}")
    if len(argv) >= 2:
        a, b = int(argv[0]), int(argv[1])
    elif len(argv) == 1:
        a, b = int(argv[0]), nums[-1]
    else:
        a, b = load_last(game), nums[-1]
    if b <= a:
        print(f"nothing new: last reported save-{a:03d}, latest save-{b:03d}")
        return 0
    text = build(game, a, b)
    if to_stdout:
        print(text, end="")
        return 0
    d = os.path.join(ROOT, "reports", game)
    os.makedirs(d, exist_ok=True)
    name = f"report-{a + 1:03d}-{b:03d}.md"
    with open(os.path.join(d, name), "w", encoding="utf-8") as f:
        f.write(text)
    cards_line = text.splitlines()[2]
    with open(os.path.join(d, "index.md"), "a", encoding="utf-8") as f:
        f.write(f"- {name}: {cards_line[len('Cards: '):]}\n")
    save_last(game, b)
    sync_usage_log(d)
    print(f"wrote reports/{game}/{name} ({b - a} segments; {cards_line})")
    return 0


def sync_usage_log(report_dir):
    """Copy the tool-usage log (kept outside the tree by usage_hook.py) into
    the game's report directory so it is committed with the game."""
    import shutil
    src = os.path.join(os.path.expanduser("~"), ".fitl-usage.log")
    if os.path.isfile(src):
        shutil.copyfile(src, os.path.join(report_dir, "usage.log"))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
