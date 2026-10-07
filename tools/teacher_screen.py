#!/usr/bin/env python3
"""teacher_screen.py - summarize a Teacher screening run (FITL_TEACHER_MODE=screen).

Usage: teacher_screen.py FILE... [--list N]

Each line is one US decision with up to 4 candidates (the policy's pick first),
each played to the end of the game the same number of times on common seeds.
A win is a playout value above 50.

Prints: cost; held-out regret of the policy's pick (the best candidate chosen on
one half of the playouts and measured on the other, both ways), overall and by
the pick's kind, by first/second eligible and by game stage; decisions whose
candidates differ by more than 20 points (all playouts) and which kinds win and
lose in them; the correlation of policy score differences with playout win
differences; and (--list N) the N decisions with the largest held-out regret.
"""
import collections
import json
import math
import statistics as st
import sys


def wins(vs):
    return [v > 50 for v in vs if v is not None]


def rate(vs):
    w = wins(vs)
    return st.mean(w) if w else float("nan")


def regret(r):
    cs = r["cands"]
    n = r["playouts"]
    h = n // 2
    out = []
    for a, b in ((slice(0, h), slice(h, n)), (slice(h, n), slice(0, h))):
        best = max(range(len(cs)), key=lambda i: rate(cs[i]["v"][a]))
        out.append(rate(cs[best]["v"][b]) - rate(cs[0]["v"][b]))
    return st.mean(out)


def spread(r):
    ws = [rate(c["v"]) for c in r["cands"]]
    return max(ws) - min(ws)


def stage(r):
    return "early (0-25)" if r["seen"] <= 25 else "middle (26-51)" if r["seen"] <= 51 else "late (52-78)"


def summary(label, rs):
    g = [regret(r) for r in rs]
    if not g:
        return
    se = st.stdev(g) / math.sqrt(len(g)) if len(g) > 1 else float("nan")
    print(f"  {label:<22} {len(g):>4}  {100 * st.mean(g):>+6.1f} {100 * se:>5.1f} {100 * st.median(g):>+7.1f}"
          f" {100 * sum(x > 0.10 for x in g) / len(g):>6.0f}% {100 * sum(x > 0.20 for x in g) / len(g):>6.0f}%")


def main(argv):
    nlist = 0
    if "--list" in argv:
        i = argv.index("--list")
        nlist = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    rs = [json.loads(l) for p in argv for l in open(p) if l.startswith("{")]
    secs = sum(r["secs"] for r in rs)
    npl = sum(r["playouts"] * len(r["cands"]) for r in rs)
    fails = sum(v is None for r in rs for c in r["cands"] for v in c["v"])
    print(f"{len(rs)} decisions from {len({r['seed'] for r in rs})} games, {npl} playouts, "
          f"{1000 * secs / npl:.0f} ms a playout (one core), {fails} failed ({100 * fails / npl:.1f}%)")

    print("\nM1 held-out regret of the policy's pick (points of win chance)")
    print(f"  {'':<22} {'n':>4}  {'mean':>6} {'se':>5} {'median':>7} {'>10':>7} {'>20':>7}")
    summary("all", rs)
    by = collections.defaultdict(list)
    for r in rs:
        by["pick " + r["cands"][0]["kind"]].append(r)
    for k in sorted(by, key=lambda k: -len(by[k])):
        summary(k, by[k])
    summary("first eligible", [r for r in rs if r["first"]])
    summary("second eligible", [r for r in rs if not r["first"]])
    for s in ("early (0-25)", "middle (26-51)", "late (52-78)"):
        summary(s, [r for r in rs if stage(r) == s])

    big = [r for r in rs if spread(r) > 0.20]
    print(f"\nM2 decisions with candidates more than 20 points apart: {len(big)} of {len(rs)} "
          f"({100 * len(big) / len(rs):.0f}%); more than 10: {sum(spread(r) > 0.10 for r in rs)}")
    best, worst, pickbest = collections.Counter(), collections.Counter(), 0
    for r in big:
        ws = [rate(c["v"]) for c in r["cands"]]
        best[r["cands"][ws.index(max(ws))]["kind"]] += 1
        worst[r["cands"][ws.index(min(ws))]["kind"]] += 1
        pickbest += ws.index(max(ws)) == 0
    print(f"  the policy's pick is the best in {pickbest} of them")
    print("  best kind:  " + ", ".join(f"{k} {v}" for k, v in best.most_common()))
    print("  worst kind: " + ", ".join(f"{k} {v}" for k, v in worst.most_common()))
    offered = collections.Counter(c["kind"] for r in big for c in r["cands"])
    print("  offered:    " + ", ".join(f"{k} {v}" for k, v in offered.most_common()))

    sd, td = [], []
    for r in rs:
        cs = r["cands"]
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                sd.append(cs[i]["score"] - cs[j]["score"])
                td.append(rate(cs[i]["v"]) - rate(cs[j]["v"]))
    print(f"\nM3 policy score differences against playout win differences ({len(sd)} pairs): correlation "
          f"{st.correlation(sd, td):.2f}; same sign in {sum((a > 0) == (b > 0) for a, b in zip(sd, td) if b != 0)} "
          f"of {sum(b != 0 for b in td)}")

    if nlist:
        print(f"\nThe {nlist} decisions with the largest held-out regret:")
        for r in sorted(rs, key=regret, reverse=True)[:nlist]:
            print(f"  seed {r['seed']} card {r['card']:>3} seen {r['seen']:>2} {'1st' if r['first'] else '2nd'} "
                  f"regret {100 * regret(r):+5.1f}: " +
                  "; ".join(f"{c['name']} {rate(c['v']):.2f} (score {c['score']:.2f})" for c in r["cands"]))


if __name__ == "__main__":
    main(sys.argv[1:])
