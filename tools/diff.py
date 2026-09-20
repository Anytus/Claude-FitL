#!/usr/bin/env python3
"""diff.py - mechanical delta between two saves, plus the program's log lines.

Usage:
  diff.py                    latest two saves of the (single) game
  diff.py <game>             latest two saves of that game
  diff.py <game> <a> <b>     save-<a> -> save-<b>
  diff.py <game> <a>         save-<a> -> latest
  diff.py --no-log ...       omit the program log lines

The output is what the human observer updates the physical board from, so it
is pasted verbatim into reports. Per space: piece changes, support, terror,
control. Then trackers, boxes, capabilities/momentum, leaders, eligibility,
and score changes. Then the log-NNN lines for every segment a+1..b.
"""
import sys
from collections import Counter

import fitl_state as S


def resolve(argv):
    game = None
    a = b = None
    if argv and not argv[0].isdigit():
        game = argv[0]
        argv = argv[1:]
    if game is None:
        game = S.default_game()
    nums = S.save_numbers(game)
    if len(nums) < 2 and not argv:
        raise SystemExit(f"game {game!r} has fewer than two saves")
    if len(argv) >= 2:
        a, b = int(argv[0]), int(argv[1])
    elif len(argv) == 1:
        a, b = int(argv[0]), nums[-1]
    else:
        a, b = nums[-2], nums[-1]
    return game, a, b


def piece_delta(before, after):
    cb, ca = Counter(before), Counter(after)
    added = {k: ca[k] - cb[k] for k in ca if ca[k] > cb[k]}
    removed = {k: cb[k] - ca[k] for k in cb if cb[k] > ca[k]}
    return added, removed


def fmt_pieces(d):
    return ", ".join(f"{n} {k}" for k, n in sorted(d.items()))


def diff_spaces(s0, s1, out):
    m0, m1 = S.space_map(s0), S.space_map(s1)
    changed = 0
    for reg, names in S.REGIONS + [("Other", [n for n in m1 if S.region_of(n) == "Other"])]:
        for name in names:
            if name not in m1 or name not in m0:
                continue
            a, b = m0[name], m1[name]
            lines = []
            added, removed = piece_delta(a["pieces"], b["pieces"])
            if added:
                lines.append(f"    + {fmt_pieces(added)}")
            if removed:
                lines.append(f"    - {fmt_pieces(removed)}")
            if a["support"] != b["support"]:
                lines.append(f"    support: {a['support']} -> {b['support']}")
            if a["terror"] != b["terror"]:
                label = "sabotage" if S.is_loc(b) else "terror"
                lines.append(f"    {label}: {a['terror']} -> {b['terror']}")
            ca, cb = S.control(a), S.control(b)
            if ca != cb:
                lines.append(f"    control: {ca} -> {cb}")
            if lines:
                changed += 1
                out.append(f"  {name} [{reg}]  now: {S.piece_summary(b['pieces'])}")
                out.extend(lines)
    if not changed:
        out.append("  (no space changes)")


TRACKERS = [
    ("arvnResources", "ARVN Resources"), ("nvaResources", "NVA Resources"),
    ("vcResources", "VC Resources / Agitate"), ("usAid", "US Aid"), ("patronage", "Patronage"),
    ("econ", "Econ"), ("trail", "Trail"), ("usPolicy", "US Policy"),
    ("coupCardsPlayed", "Coup cards played"), ("rvnLeaderFlipped", "RVN leader flipped"),
    ("peaceTalks", "Peace Talks marker"), ("gameOver", "Game over"),
]


def diff_scalars(s0, s1, out):
    any_ = False
    for key, label in TRACKERS:
        if s0.get(key) != s1.get(key):
            out.append(f"  {label}: {s0.get(key)} -> {s1.get(key)}")
            any_ = True
    if not any_:
        out.append("  (no tracker changes)")


def diff_box(label, before, after, out):
    added, removed = piece_delta(before, after)
    if added or removed:
        bits = []
        if added:
            bits.append("+ " + fmt_pieces(added))
        if removed:
            bits.append("- " + fmt_pieces(removed))
        out.append(f"  {label}: {'; '.join(bits)}  (now: {S.piece_summary(after)})")


def diff_available(s0, s1, out):
    a0, a1 = S.available(s0), S.available(s1)
    for f in S.FACTIONS:
        bits = [f"{gen} {a0[f][gen]} -> {a1[f][gen]}" for gen in S.MANIFEST[f] if a0[f][gen] != a1[f][gen]]
        if bits:
            out.append(f"  Available {f}: " + ", ".join(bits))


def diff_lists(label, l0, l1, out, key=None):
    k = key or (lambda x: x)
    s0, s1 = {k(x) for x in l0}, {k(x) for x in l1}
    added = [x for x in l1 if k(x) not in s0]
    removed = [x for x in l0 if k(x) not in s1]
    if added or removed:
        bits = []
        if added:
            bits.append("+ " + ", ".join(str(x) for x in added))
        if removed:
            bits.append("- " + ", ".join(str(x) for x in removed))
        out.append(f"  {label}: {'; '.join(bits)}")


def cap_str(c):
    return f"{c['name']} ({'shaded' if c['shaded'] else 'unshaded'})"


def diff_sequence(s0, s1, out):
    q0, q1 = s0["sequence"], s1["sequence"]
    for key, label in [("eligibleThisTurn", "Eligible this card"), ("passed", "Passed"),
                       ("eligibleNextTurn", "Eligible next card"), ("ineligibleNextTurn", "Ineligible next card")]:
        if sorted(q0[key]) != sorted(q1[key]):
            out.append(f"  {label}: {', '.join(q0[key]) or 'none'} -> {', '.join(q1[key]) or 'none'}")
    a0 = [f"{a['faction']} -> {a['action']}" for a in q0["actors"]]
    a1 = [f"{a['faction']} -> {a['action']}" for a in q1["actors"]]
    if a0 != a1:
        out.append(f"  Acted: {', '.join(a0) or 'none'} -> {', '.join(a1) or 'none'}")
    if (s0["currentCard"], s0["onDeckCard"]) != (s1["currentCard"], s1["onDeckCard"]):
        out.append(f"  Cards: current #{s0['currentCard']} / on deck #{s0['onDeckCard']} -> "
                   f"current #{s1['currentCard']} / on deck #{s1['onDeckCard']}")


def diff_scores(s0, s1, out):
    c0, c1 = S.scores(s0), S.scores(s1)
    for f in S.FACTIONS:
        if c0[f]["points"] != c1[f]["points"]:
            out.append(f"  {f}: {c0[f]['points']} -> {c1[f]['points']} (score {c1[f]['score']:+d})")
    if not any(c0[f]["points"] != c1[f]["points"] for f in S.FACTIONS):
        out.append("  (no score changes)")


def diff(game, a, b, with_log=True):
    s0 = S.load_save(S.save_path(game, a))
    s1 = S.load_save(S.save_path(game, b))
    out = []
    hist = {h["save_number"]: h for h in s1["history"]}
    segs = [hist[i] for i in range(a + 1, b + 1) if i in hist]
    out.append(f"### diff {game}: save-{a:03d} -> save-{b:03d}")
    for h in segs:
        out.append(f"  segment {h['save_number']:03d} on {h['card']}: {' / '.join(h['summary'])}")
    out.append("Spaces:")
    diff_spaces(s0, s1, out)
    out.append("Trackers:")
    diff_scalars(s0, s1, out)
    box = []
    diff_available(s0, s1, box)
    diff_box("Casualties", s0["casualties"], s1["casualties"], box)
    diff_box("Out of Play", s0["outOfPlay"], s1["outOfPlay"], box)
    if box:
        out.append("Boxes:")
        out.extend(box)
    misc = []
    diff_lists("Capabilities", s0["capabilities"], s1["capabilities"], misc, key=cap_str)
    diff_lists("Momentum", s0["momentum"], s1["momentum"], misc)
    diff_lists("Ongoing events", s0["ongoingEvents"], s1["ongoingEvents"], misc)
    diff_lists("RVN Leader box", s0["rvnLeaders"], s1["rvnLeaders"], misc)
    diff_lists("Pivotal events available", s0["pivotCardsAvailable"], s1["pivotCardsAvailable"], misc)
    if misc:
        out.append("Markers:")
        out.extend(misc)
    seq = []
    diff_sequence(s0, s1, seq)
    if seq:
        out.append("Sequence:")
        out.extend(seq)
    out.append("Scores:")
    diff_scores(s0, s1, out)
    if with_log:
        out.append("Program log:")
        for i in range(a + 1, b + 1):
            for line in S.load_log(S.log_path(game, i)):
                for sub in line.split("\n"):
                    out.append("  | " + sub if sub else "  |")
    return "\n".join(out)


def main():
    argv = sys.argv[1:]
    with_log = True
    if "--no-log" in argv:
        with_log = False
        argv = [x for x in argv if x != "--no-log"]
    game, a, b = resolve(argv)
    print(diff(game, a, b, with_log))


if __name__ == "__main__":
    main()
