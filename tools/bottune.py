#!/usr/bin/env python3
"""bottune.py - tune a US search policy's weights against the Bots.

Usage:
  bottune.py --start policies/tune-start.json --name t1 [--generations 15]
             [--pairs 4] [--games 80] [--sigma 0.5] [--alpha 0.2]
             [--seed-base 20000] [--workers 4] [--all-wins] [--us-player]
             [--freeze w1,w2]

Evolution strategy with antithetic pairs and common random numbers. Each
generation plays the current policy and `pairs` pairs of mirrored
perturbations (weights +/- sigma * scale * d, d ~ N(0, I)) on the same fresh
block of `games` seeds, scores each by its mean "US lead" (final US margin
minus the best rival's margin), and moves the weights along the rank-weighted
perturbations. Each weight's scale is its starting size (0.5 if it starts at
0); hinge_buffer is tuned as well (scale 1).

By default games are played with --us-final-only (the US may win only at
the final Coup), the condition of the human-US games; --all-wins drops it.

Writes, and resumes from:
  results/tune_<name>.jsonl     one line per generation
  policies/tuned_<name>.json    the current policy after each generation
Seeds: generation g uses seed-base + g*games .. +games-1, so training never
reuses a seed. Validate on seeds outside that range (botrun + botcompare).
"""
import argparse
import json
import math
import os
import random
import statistics as st
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIVALS = ("ARVN", "NVA", "VC")


def lead(r):
    s = r["final_scores"]
    return s["US"] - max(s[f] for f in RIVALS)


def play(policy, seed, games, args, tag):
    """Play `games` seeds with `policy`; return {seed: record} for completed games."""
    d = tempfile.mkdtemp(prefix=f"tune-{tag}-")
    pfile, out = os.path.join(d, "policy.json"), os.path.join(d, "run.jsonl")
    json.dump(policy, open(pfile, "w"))
    cmd = [sys.executable, os.path.join(ROOT, "tools", "botrun.py"), "--games", str(games), "--seed", str(seed),
           "--workers", str(args.workers), "--timeout", "180", "--us-policy", pfile, "--out", out]
    if not args.all_wins:
        cmd.append("--us-final-only")
    if args.us_player:
        cmd.append("--us-player")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    recs = [json.loads(l) for l in open(out)]
    return {r["seed"]: r for r in recs if not r.get("error")}


def to_vec(policy, keys):
    w = policy["weights"]
    return [policy.get("hinge_buffer", 3.0) if k == "hinge_buffer" else w[k] for k in keys]


def to_policy(base, keys, vec, name):
    p = json.loads(json.dumps(base))
    p["name"] = name
    for k, v in zip(keys, vec):
        if k == "hinge_buffer":
            p["hinge_buffer"] = round(max(v, 0.0), 4)
        else:
            p["weights"][k] = round(v, 4)
    return p


def centered_ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    for rank, i in enumerate(order):
        r[i] = rank / (len(xs) - 1) - 0.5
    return r


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--start", required=True)
    p.add_argument("--name", required=True)
    p.add_argument("--generations", type=int, default=15)
    p.add_argument("--pairs", type=int, default=4)
    p.add_argument("--games", type=int, default=80)
    p.add_argument("--sigma", type=float, default=0.5)
    p.add_argument("--alpha", type=float, default=0.2)
    p.add_argument("--seed-base", type=int, default=20000)
    p.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    p.add_argument("--freeze", default="", metavar="W1,W2",
                   help="weights kept at their start value and not tuned")
    p.add_argument("--all-wins", action="store_true")
    p.add_argument("--us-player", action="store_true",
                   help="Bots treat the US as a player (ARVN Resources tracked); see botrun.py")
    args = p.parse_args()

    start = json.load(open(args.start))
    frozen = set(filter(None, args.freeze.split(",")))
    unknown = frozen - set(start["weights"]) - {"hinge_buffer"}
    if unknown:
        sys.exit(f"--freeze: not in the start policy: {', '.join(sorted(unknown))}")
    keys = [k for k in sorted(start["weights"]) + ["hinge_buffer"] if k not in frozen]
    x0 = to_vec(start, keys)
    scale = [abs(v) if v != 0 else 0.5 for v in x0]
    if "hinge_buffer" in keys:
        scale[keys.index("hinge_buffer")] = 1.0

    log_path = os.path.join(ROOT, "results", f"tune_{args.name}.jsonl")
    out_policy = os.path.join(ROOT, "policies", f"tuned_{args.name}.json")
    z, gen0 = [0.0] * len(keys), 0
    if os.path.exists(log_path):
        lines = [json.loads(l) for l in open(log_path) if l.strip()]
        if lines:
            z, gen0 = lines[-1]["z_next"], lines[-1]["gen"] + 1
            print(f"resuming at generation {gen0}", file=sys.stderr)

    rng = random.Random(f"{args.name}")
    for _ in range(gen0):            # keep the perturbation stream identical on resume
        for _ in range(args.pairs * len(keys)):
            rng.gauss(0, 1)

    for gen in range(gen0, args.generations):
        seed = args.seed_base + gen * args.games
        dirs = [[rng.gauss(0, 1) for _ in keys] for _ in range(args.pairs)]
        vec = lambda zz: [a + s * b for a, s, b in zip(x0, scale, zz)]
        variants = [("center", z)]
        for i, d in enumerate(dirs):
            variants.append((f"+{i}", [a + args.sigma * b for a, b in zip(z, d)]))
            variants.append((f"-{i}", [a - args.sigma * b for a, b in zip(z, d)]))
        runs = {}
        for tag, zz in variants:
            runs[tag] = play(to_policy(start, keys, vec(zz), f"{args.name}-g{gen}{tag}"), seed, args.games, args, tag)
        common = sorted(set.intersection(*(set(r) for r in runs.values())))
        J = {t: st.mean(lead(runs[t][s]) for s in common) for t in runs}
        wins = {t: sum(runs[t][s]["winner"] == "US" for s in common) for t in runs}

        tags = [t for t, _ in variants[1:]]
        ranks = dict(zip(tags, centered_ranks([J[t] for t in tags])))
        grad = [sum((ranks[f"+{i}"] - ranks[f"-{i}"]) * dirs[i][j] for i in range(args.pairs)) / args.pairs
                for j in range(len(keys))]
        z_next = [a + args.alpha * g for a, g in zip(z, grad)]

        rec = {"gen": gen, "seeds": [seed, seed + args.games - 1], "games": len(common),
               "J": {t: round(v, 3) for t, v in J.items()}, "us_wins": wins,
               "weights": dict(zip(keys, [round(v, 4) for v in vec(z)])),
               "z": z, "z_next": z_next}
        with open(log_path, "a") as f:
            f.write(json.dumps(rec) + "\n")
        json.dump(to_policy(start, keys, vec(z_next), f"tuned_{args.name}"), open(out_policy, "w"), indent=2)
        best = max(tags, key=lambda t: J[t])
        print(f"gen {gen}: center lead {J['center']:+.2f} wins {wins['center']}/{len(common)}; "
              f"best {best} {J[best]:+.2f}; step {math.sqrt(sum(g * g for g in grad)) * args.alpha:.2f}", flush=True)
        z = z_next


if __name__ == "__main__":
    main()
