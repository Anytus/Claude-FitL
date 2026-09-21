#!/usr/bin/env python3
"""render.py - the board view. Renders a save file as text.

Usage:
  render.py                  latest save of the (single) game under games/
  render.py <game>           latest save of that game
  render.py <game> <n>       save-<n> of that game
  render.py <path-to-save>   a specific save file

Sections: spaces by region, trackers, Available / Casualties / Out of Play,
capabilities and momentum, RVN leaders, sequence of play, current and on-deck
cards, deck position, scores. Scores are computed here; never by hand.

Default is the brief view: LoCs holding nothing are collapsed to one line per
region and the adjacency section is omitted (use tools/map.py for adjacency).
`--full` prints every LoC and the whole adjacency table.
"""
import os
import sys

import fitl_state as S


def resolve(argv):
    """Return (game, save number, path)."""
    if not argv:
        game = S.default_game()
        n = S.save_numbers(game)[-1]
        return game, n, S.save_path(game, n)
    if os.path.isfile(argv[0]):
        p = os.path.abspath(argv[0])
        game = os.path.basename(os.path.dirname(p))
        n = int(p.rsplit("-", 1)[1])
        return game, n, p
    game = argv[0]
    nums = S.save_numbers(game)
    if not nums:
        raise SystemExit(f"no saves for game {game!r}")
    n = int(argv[1]) if len(argv) > 1 else nums[-1]
    return game, n, S.save_path(game, n)


def space_line(sp):
    loc = S.is_loc(sp)
    kind = "LoC" if loc else sp["spaceType"].replace(" Province", "")
    if loc:
        head = f"{sp['name']} [{kind}, econ {sp['population']}]"
        state_bits = [f"sabotage {sp['terror']}" if sp["terror"] else "no sabotage"]
    else:
        pop = sp["population"]
        head = f"{sp['name']} [{kind}, pop {pop}" + (", coastal]" if sp["coastal"] else "]")
        sup = sp["support"] if pop > 0 else "n/a"
        state_bits = [sup, S.control(sp)]
        if sp["terror"]:
            state_bits.append(f"terror {sp['terror']}")
    return f"  {head:<48} {' / '.join(state_bits):<40} {S.piece_summary(sp['pieces'])}"


def render(state, game, n, cards, full=False):
    out = []
    w = out.append
    w(f"=== {game} save-{n:03d} === {state['scenarioName']} | US policy: {state['usPolicy']}")
    w("")
    smap = S.space_map(state)
    seen = set()
    for reg, names in S.REGIONS:
        w(f"--- {reg} ---")
        quiet_locs = []
        for name in names:
            if name in smap:
                sp = smap[name]
                seen.add(name)
                if not full and S.is_loc(sp) and not sp["pieces"] and not sp["terror"]:
                    quiet_locs.append(f"{name[4:]} ({sp['population']})")
                    continue
                w(space_line(sp))
        if quiet_locs:
            w(f"  empty LoCs (econ): {'; '.join(quiet_locs)}")
    rest = [sp for sp in state["spaces"] if sp["name"] not in seen]
    if rest:
        w("--- Other ---")
        for sp in rest:
            w(space_line(sp))
    w("")
    w("--- Trackers ---")
    humans = set(state["humanFactions"])
    nva_res = f"NVA Resources {state['nvaResources']}" if "NVA" in humans else "NVA Resources not tracked (bot)"
    vc_res = f"VC Resources {state['vcResources']}" if "VC" in humans else f"VC Agitate total {state['vcResources']}"
    w(f"  ARVN Resources {state['arvnResources']} | {nva_res} | {vc_res}")
    w(f"  US Aid {state['usAid']} | Patronage {state['patronage']} | Econ {state['econ']} | Trail {state['trail']}")
    w("")
    av = S.available(state)
    w("--- Available (force pool) ---")
    for f in S.FACTIONS:
        w(f"  {f:<4} " + ", ".join(f"{gen} {av[f][gen]}" for gen in S.MANIFEST[f]))
    w(f"--- Casualties --- {S.piece_summary(state['casualties'])}")
    w(f"--- Out of Play --- {S.piece_summary(state['outOfPlay'])}")
    w("")
    w("--- Capabilities ---")
    if state["capabilities"]:
        for c in state["capabilities"]:
            w(f"  {c['name']} ({'shaded' if c['shaded'] else 'unshaded'}, {c['faction']})")
    else:
        w("  none")
    w(f"--- Momentum --- {', '.join(state['momentum']) or 'none'}")
    other = [e for e in state["ongoingEvents"] if e not in state["momentum"]
             and e not in [c["name"] for c in state["capabilities"]]]
    if other:
        w(f"--- Other ongoing events --- {', '.join(other)}")
    w(f"--- RVN Leader box --- {', '.join(state['rvnLeaders'])}"
      + (" (top leader flipped)" if state["rvnLeaderFlipped"] else ""))
    w(f"--- Pivotal events still available --- {', '.join(state['pivotCardsAvailable']) or 'none'}"
      + ("  [Peace Talks marker on Linebacker II]" if state.get("peaceTalks") else ""))
    w("")
    seq = state["sequence"]
    w("--- Sequence of play (this card) ---")
    w(f"  Eligible this card: {', '.join(seq['eligibleThisTurn']) or 'none'}")
    w(f"  Acted: {', '.join(a['faction'] + ' -> ' + a['action'] for a in seq['actors']) or 'none'}")
    w(f"  Passed: {', '.join(seq['passed']) or 'none'}")
    w(f"  Eligible next card (so far): {', '.join(seq['eligibleNextTurn']) or '-'} | "
      f"Ineligible next card (so far): {', '.join(seq['ineligibleNextTurn']) or '-'}")
    w("")
    w("--- Cards ---")
    w("  Current: " + S.card_line(cards, state["currentCard"]))
    if state["onDeckCard"]:
        w("  On deck: " + S.card_line(cards, state["onDeckCard"]))
    else:
        w("  On deck: (none)")
    seen = len(state["cardsSeen"])
    per = state["cardsPerCampaign"]
    pile, pos = (seen - 1) // per + 1, (seen - 1) % per + 1   # position of the on-deck card
    w(f"  Deck: Coup cards played {state['coupCardsPlayed']} of {state['totalCoupCards']} | "
      f"on-deck card is card {pos} of {per} in pile {pile} of {state['totalCoupCards']} | "
      f"{seen} cards drawn so far")
    if state.get("gameOver"):
        w("  *** GAME OVER ***")
    w("")
    board = S.load_map() if full else None
    if board:
        w("--- Adjacency (the printed map; * = listed by the program in this direction only) ---")
        one_way = {tuple(p) for p in board["one_way"]}
        for reg, names in S.REGIONS:
            for name in names:
                if name in board["spaces"]:
                    neigh = [n + ("*" if (name, n) in one_way else "") for n in board["spaces"][name]["adjacent"]]
                    w(f"  {name:<38} {', '.join(neigh)}")
        w("")
    else:
        w("--- Adjacency --- omitted; python3 tools/map.py <space> for neighbours, render.py --full for all")
        w("")
    sc = S.scores(state)
    w("--- Scores (computed from the save; thresholds US 50, ARVN 50, NVA 18, VC 35) ---")
    for f in S.ranked(sc):
        s = sc[f]
        w(f"  {f:<4} points {s['points']:>3}  score {s['score']:+d}   ({s['detail']})")
    w("  Victory order on ties: VC, ARVN, NVA, US. A faction with score > 0 at a Coup Victory phase wins.")
    return "\n".join(out)


def summary_sections(state, game, n, cards):
    """Trackers, sequence of play, cards and scores only (for reports)."""
    text = render(state, game, n, cards)
    keep = []
    on = False
    for line in text.splitlines():
        if line.startswith("--- Trackers") or line.startswith("--- Sequence") or line.startswith("--- Cards") or line.startswith("--- Scores"):
            on = True
        elif line.startswith("--- ") and not line.startswith("--- Trackers"):
            on = False
        if on:
            keep.append(line)
    return "\n".join(keep)


def main():
    argv = sys.argv[1:]
    full = "--full" in argv
    argv = [a for a in argv if a not in ("--full", "--no-map")]
    game, n, path = resolve(argv)
    state = S.load_save(path)
    cards = S.load_cards()
    print(render(state, game, n, cards, full=full))


if __name__ == "__main__":
    main()
