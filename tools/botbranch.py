#!/usr/bin/env python3
"""botbranch.py - compare human US decisions with the US search policy's.

Usage:
  botbranch.py --policy policies/fit3flat.json --rollouts 30 --out DIR GAMEDIR:SAVE ...
  botbranch.py --summary DIR

GAMEDIR is a human-US game's save directory (games/<name>); SAVE the number
of a save with the US to act (its summary reads "US is up"). The save after
it holds the human's action. For each branch point `fitl.Branch` lets the
policy decide on the same position, then plays both positions to the end
`--rollouts` times with all four factions as Bots (the US by the policy),
each pair on the same seed and deck continuation, as in `Autoplay
--us-final-only --us-player`. Output: DIR/<game>_<save>.jsonl, one line per
run; --summary prints, per branch point, the policy's choice and the paired
difference in final US lead (human minus policy).
"""
import argparse
import collections
import glob
import json
import math
import os
import statistics as st
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def lead(s):
    return s["US"] - max(s["ARVN"], s["NVA"], s["VC"])


def summary(d):
    rows = []
    for p in sorted(glob.glob(os.path.join(d, "*.jsonl"))):
        recs = [json.loads(l) for l in open(p) if l.strip()]
        by = {(r["seed"], r["arm"]): r for r in recs if not r["error"]}
        seeds = sorted(s for s, a in by if a == "llm" and (s, "bot") in by)
        if len(seeds) < 2:
            print(f"{os.path.basename(p)}: fewer than 2 completed pairs")
            continue
        dl = [lead(by[(s, "llm")]["final_scores"]) - lead(by[(s, "bot")]["final_scores"]) for s in seeds]
        ch = collections.Counter(by[(s, "bot")]["choice"].rsplit(" ", 2)[0] for s in seeds).most_common(1)[0][0]
        imm = lead(by[(seeds[0], "llm")]["after"]) - st.mean(lead(by[(s, "bot")]["after"]) for s in seeds)
        se = st.stdev(dl) / math.sqrt(len(dl))
        rows.append(st.mean(dl))
        print(f"{os.path.basename(p)[:-6]:<14} n={len(seeds):<3} policy: {ch:<34} "
              f"lead now {imm:+5.1f}  final lead diff {st.mean(dl):+6.2f} (se {se:.2f})")
    if len(rows) > 1:
        print(f"\nmean over {len(rows)} points {st.mean(rows):+.2f} (se {st.stdev(rows) / math.sqrt(len(rows)):.2f})")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("points", nargs="*", metavar="GAMEDIR:SAVE")
    p.add_argument("--policy", default=os.path.join(ROOT, "policies", "fit3flat.json"))
    p.add_argument("--rollouts", type=int, default=30)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    p.add_argument("--timeout", type=int, default=300, help="seconds per branch point")
    p.add_argument("--out")
    p.add_argument("--summary", metavar="DIR")
    args = p.parse_args()
    if args.summary:
        return summary(args.summary)
    if not args.out or not args.points:
        sys.exit("give --out and at least one GAMEDIR:SAVE")
    os.makedirs(args.out, exist_ok=True)
    cp = os.environ.get("FITL_CP") or os.path.join(ROOT, "fitl", "lib", "*")
    env = {k: v for k, v in os.environ.items() if k != "JAVA_TOOL_OPTIONS"}

    def run(point):
        gdir, save = point.rsplit(":", 1)
        n = int(save)
        name = f"{os.path.basename(os.path.normpath(gdir))}_{n:03d}"
        cmd = ["java", "-Xss8m", "-cp", cp, "fitl.Branch", "--policy", os.path.abspath(args.policy),
               "--before", os.path.join(gdir, f"save-{n:03d}"), "--after", os.path.join(gdir, f"save-{n + 1:03d}"),
               "--rollouts", str(args.rollouts), "--seed", str(args.seed)]
        with open(os.path.join(args.out, name + ".jsonl"), "w") as f:
            try:
                subprocess.run(cmd, stdout=f, stderr=subprocess.DEVNULL, env=env, timeout=args.timeout)
                status = "ok"
            except subprocess.TimeoutExpired:
                status = "timeout"
        print(f"{name}: {status}", file=sys.stderr, flush=True)

    with ThreadPoolExecutor(args.workers) as ex:
        list(ex.map(run, args.points))
    summary(args.out)


if __name__ == "__main__":
    main()
