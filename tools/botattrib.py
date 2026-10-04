#!/usr/bin/env python3
"""botattrib.py - where each faction's points came from, in a --trace run.

Usage: botattrib.py results/run_trace.jsonl

Sums every score component's change (Support, US Available, Opposition, VC
Bases, COIN Control, Patronage, NVA Control, NVA Bases) by the faction and
kind of action that made it, and by Coup rounds, per completed game.
"""
import collections
import json
import sys

KEYS = ["sup", "usav", "opp", "vcb", "coin", "pat", "nvac", "nvab"]
POINTS = {"US": ("sup", "usav"), "ARVN": ("coin", "pat"), "NVA": ("nvac", "nvab"), "VC": ("opp", "vcb")}


def kind(a):
    if a["a"] == "Event":
        return "Event " + a["ev"]
    if a["a"] == "Pass" or not a["ops"]:
        return a["a"]
    return "+".join(a["ops"][:2])


def main(path):
    ok = [r for r in map(json.loads, open(path, encoding="utf-8")) if not r.get("error")]
    n = len(ok)
    grp, det, uses = (collections.defaultdict(collections.Counter) for _ in range(3))
    for r in ok:
        for a in r["actions"]:
            g = f"{a['f']} {'Event' if a['a'] == 'Event' else 'Pass' if a['a'] == 'Pass' else 'Op'}"
            k = f"{a['f']} {kind(a)}"
            uses[k]["n"] += 1
            for c, v in a["d"].items():
                grp[g][c] += v
                det[k][c] += v
        for cp in r["coups"]:
            uses["Coup round"]["n"] += 1
            for c, v in cp["d"].items():
                grp["Coup round"][c] += v
                det["Coup round"][c] += v
    print(f"{n} completed games; change per game")
    print(f"{'source':<12}" + "".join(f"{k:>7}" for k in KEYS))
    for g in sorted(grp):
        print(f"{g:<12}" + "".join(f"{grp[g][k] / n:+7.1f}" for k in KEYS))
    for f, (a, b) in POINTS.items():
        print(f"\n{f} points, largest sources (per game; uses per game; per use)")
        rows = sorted(det, key=lambda k: -abs(det[k][a] + det[k][b]))[:10]
        for k in rows:
            v = det[k][a] + det[k][b]
            print(f"  {k:<30} {v / n:+6.2f}   {uses[k]['n'] / n:5.2f}   {v / uses[k]['n']:+.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
