#!/usr/bin/env python3
"""apply_periods.py - record each event card's period marking in cards.json.

Usage:
  apply_periods.py --y1964 "1,17,29,..." --y1968 "2,3,7,..."
  apply_periods.py --file periods.json     # {"1964": [...], "1965": [...], "1968": [...]}

Cards 1-120 not listed as 1964 or 1968 are recorded as 1965 (unless a 1965
list is given explicitly, in which case all three lists must cover 1-120
exactly once). Coup and pivotal cards (121-130) get no period.

The marking is the year printed in the upper-left corner of the physical
card. It is public information; it decides which deck pile a card can be in.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_PATH = os.path.join(ROOT, "cards.json")


def parse_list(s):
    out = []
    for tok in s.replace(";", ",").replace("\n", ",").split(","):
        tok = tok.strip()
        if not tok:
            continue
        if "-" in tok:
            a, b = tok.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(tok))
    return out


def main(argv):
    y64 = y65 = y68 = None
    i = 0
    while i < len(argv):
        if argv[i] == "--y1964":
            y64 = parse_list(argv[i + 1]); i += 2
        elif argv[i] == "--y1965":
            y65 = parse_list(argv[i + 1]); i += 2
        elif argv[i] == "--y1968":
            y68 = parse_list(argv[i + 1]); i += 2
        elif argv[i] == "--file":
            with open(argv[i + 1]) as f:
                d = json.load(f)
            y64 = [int(x) for x in d.get("1964", [])]
            y65 = [int(x) for x in d.get("1965", [])] or None
            y68 = [int(x) for x in d.get("1968", [])]
            i += 2
        else:
            print(__doc__); return 2
    if y64 is None or y68 is None:
        print(__doc__); return 2

    periods = {}
    for n in y64:
        periods[n] = "1964"
    for n in y68:
        if n in periods:
            raise SystemExit(f"card {n} listed in two periods")
        periods[n] = "1968"
    if y65 is not None:
        for n in y65:
            if n in periods:
                raise SystemExit(f"card {n} listed in two periods")
            periods[n] = "1965"
        missing = [n for n in range(1, 121) if n not in periods]
        if missing:
            raise SystemExit(f"cards not in any list: {missing}")
    else:
        for n in range(1, 121):
            periods.setdefault(n, "1965")
    bad = [n for n in periods if not 1 <= n <= 120]
    if bad:
        raise SystemExit(f"not event cards: {bad}")

    with open(CARDS_PATH, encoding="utf-8") as f:
        cards = json.load(f)
    for n, p in periods.items():
        cards[str(n)]["period"] = p
    for n in range(121, 131):
        cards[str(n)].pop("period", None)
    with open(CARDS_PATH, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=1, ensure_ascii=False)
    counts = {p: sum(1 for v in periods.values() if v == p) for p in ("1964", "1965", "1968")}
    print(f"periods written to cards.json: {counts}")
    for p, need in (("1964", 24), ("1965", 24), ("1968", 24)):
        if counts[p] < need:
            print(f"WARNING: only {counts[p]} cards marked {p}; the Full deck needs at least {need}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
