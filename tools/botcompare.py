#!/usr/bin/env python3
"""botcompare.py - compare two botrun.py runs on the seeds they share.

Usage: botcompare.py BASELINE.jsonl VARIANT.jsonl

Seeds that failed in either run are left out. Prints each run's winner
shares and mean final margins, and the paired difference in the US margin
and in the US margin minus the best rival margin, with its standard error.
"""
import json
import math
import statistics as st
import sys

FACTIONS = ["US", "ARVN", "NVA", "VC"]


def load(path):
    return {r["seed"]: r for r in map(json.loads, open(path, encoding="utf-8")) if not r.get("error")}


def lead(r):
    s = r["final_scores"]
    return s["US"] - max(s["ARVN"], s["NVA"], s["VC"])


def main(a_path, b_path):
    a, b = load(a_path), load(b_path)
    seeds = sorted(set(a) & set(b))
    n = len(seeds)
    print(f"{n} seeds completed in both runs")
    print(f"\n{'':<10}" + "".join(f"{f:>8}" for f in FACTIONS) + "   US margin  US lead")
    for name, run in (("baseline", a), ("variant", b)):
        wins = [sum(run[s]["winner"] == f for s in seeds) / n for f in FACTIONS]
        us = st.mean(run[s]["final_scores"]["US"] for s in seeds)
        ld = st.mean(lead(run[s]) for s in seeds)
        print(f"{name:<10}" + "".join(f"{100 * w:7.1f}%" for w in wins) + f"   {us:+9.1f}  {ld:+7.1f}")
    for label, fn in (("US margin", lambda r: r["final_scores"]["US"]), ("US lead", lead)):
        d = [fn(b[s]) - fn(a[s]) for s in seeds]
        se = st.stdev(d) / math.sqrt(n) if n > 1 else 0.0
        print(f"\npaired change in {label}: {st.mean(d):+.2f} (se {se:.2f})")
    ends = {}
    for s in seeds:
        ends[b[s]["end_coup"]] = ends.get(b[s]["end_coup"], 0) + 1
    print("\nvariant games ended at: " + ", ".join(
        f"{'final' if c == 6 else 'Coup ' + str(c)} {100 * k / n:.0f}%" for c, k in sorted(ends.items())))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
