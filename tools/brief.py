#!/usr/bin/env python3
"""brief.py - everything needed for one decision, in one call.

Usage:
  brief.py                    the (single) game under games/
  brief.py <game>
  brief.py ... --no-narration omit section 2 (ctl.py advance uses this,
                              having just printed the same lines)
  brief.py ... --full         full board view (every LoC, whole adjacency)

Sections, in order:
  1. The board view (render.py): spaces, trackers, Available, capabilities,
     sequence of play, both cards with their full text and Tru'ng markings,
     deck position, scores.
  2. This card so far: the program's own narration for every save that
     belongs to the current card (what the bots did before the US turn).
  3. Neighbours of every space holding a US piece, plus Saigon, from the
     printed map (map.json). Ask tools/map.py for any other space.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fitl_state as S
import render as R


def current_card_segments(game, state):
    """(save number, summary, log lines) for every save of the current card."""
    cur = state["currentCard"]
    prefix = f"#{cur} "
    out = []
    for h in state["history"]:
        if h["card"].startswith(prefix):
            n = h["save_number"]
            out.append((n, " / ".join(h["summary"]), S.load_log(S.log_path(game, n))))
    return out


def us_neighbours(state, board):
    """One line per space holding a US piece (plus Saigon): its neighbours.
    Pieces are on the board above, so only names are listed here."""
    smap = S.space_map(state)
    with_us = {sp["name"] for sp in state["spaces"]
               if any(p.startswith("US ") for p in sp["pieces"])}
    with_us.add("Saigon")
    order = [name for _, names in S.REGIONS for name in names]
    names = [n for n in order if n in with_us and n in board["spaces"]]
    names += sorted(n for n in with_us if n not in order and n in board["spaces"])
    lines = []
    for name in names:
        neigh = [n[4:] + " (LoC)" if n.startswith("LOC ") else n
                 for n in board["spaces"][name]["adjacent"]]
        lines.append(f"  {name}: {', '.join(neigh)}")
    return lines


def brief_text(game, n, path, narration=True, full=False):
    state = S.load_save(path)
    cards = S.load_cards()
    out = [R.render(state, game, n, cards, full=full)]
    w = out.append
    if narration:
        w(f"--- This card (#{state['currentCard']}) so far: the program's narration ---")
        segs = current_card_segments(game, state)
        if not segs:
            w("  (no saves for this card yet)")
        for num, summary, lines in segs:
            w(f"  [save-{num:03d}] {summary}")
            for line in lines:
                for sub in line.split("\n"):
                    w(f"    {sub}")
        w("")
    board = S.load_map()
    if board:
        w("--- Neighbours of every space with US pieces, and Saigon (tools/map.py <space> for others) ---")
        out.extend(us_neighbours(state, board))
        w("")
    return "\n".join(out)


def main(argv):
    narration = "--no-narration" not in argv
    full = "--full" in argv
    argv = [a for a in argv if not a.startswith("--")]
    game, n, path = R.resolve(argv)
    print(brief_text(game, n, path, narration=narration, full=full))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
