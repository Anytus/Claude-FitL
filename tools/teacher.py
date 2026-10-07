#!/usr/bin/env python3
"""teacher.py - summarize playout labels written by fitl.Teacher (FITL_TEACHER).

Usage: teacher.py FILE...

Each labelled decision has candidates Event, N1 (the best other candidate by
the policy's score) and sometimes N2 (the next best with a different
position), each played to the end of the game the same number of times on
common seeds. A playout's value is -100 (a Bot won early), the final lead
(lost at the final Coup) or the final lead + 100 (won); a win is value > 50.

Prints, per stratum ("disagree": the Event weight 0 policy picks the Event
and the fit3flat Event weight -0.71 would pick N1; "other": sampled
decisions with the Event on offer): each decision's win rates and paired
differences; the mean paired difference over decisions with its standard
error (the decisions' spread, noise included); how much the common seeds
reduce the noise; time per playout; and how the policy's score differences
line up with the playouts'.
"""
import json
import math
import statistics as st
import sys


def load(paths):
    for p in paths:
        for line in open(p):
            if line.startswith("{"):
                yield json.loads(line)


def paired(a, b):
    """Win differences on the seeds where both playouts finished."""
    return [(x > 50) - (y > 50) for x, y in zip(a, b) if x is not None and y is not None]


def mse(xs):
    m = st.mean(xs)
    return m, (st.stdev(xs) / math.sqrt(len(xs)) if len(xs) > 1 else float("nan"))


def corr(xs, ys):
    if len(xs) < 3 or st.pstdev(xs) == 0 or st.pstdev(ys) == 0:
        return float("nan")
    return st.correlation(xs, ys)


def main(paths):
    rs = list(load(paths))
    if not rs:
        sys.exit("no labelled decisions")
    secs = sum(r["secs"] for r in rs)
    n_play = sum(r["playouts"] * len(r["cands"]) for r in rs)
    fails = sum(v is None for r in rs for c in r["cands"] for v in c["v"])
    print(f"{len(rs)} labelled decisions, {n_play} playouts, {1000 * secs / n_play:.0f} ms a playout "
          f"(one core), {fails} failed")

    rhos, sd_pair, sd_unpair = [], [], []
    score_d, teach_d = [], []
    for stratum in ("disagree", "other"):
        g = [r for r in rs if r["stratum"] == stratum]
        if not g:
            continue
        print(f"\n== {stratum} ({len(g)} decisions)")
        print(f"  {'seed':>7} {'card':>4} {'seen':>4}  {'Event':>6} {'N1':>6} {'N2':>6}  {'E-N1':>6} {'se':>5}  N1 / N2")
        dE, dN = [], []
        for r in g:
            c = {x["name"]: x for x in r["cands"]}
            names = [x["name"] for x in r["cands"]]
            E, N1 = r["cands"][0], r["cands"][1]
            N2 = r["cands"][2] if len(r["cands"]) > 2 else None
            win = lambda x: st.mean(v > 50 for v in x["v"] if v is not None)
            d = paired(E["v"], N1["v"])
            m, se = mse(d)
            dE.append(m)
            both = [(x, y) for x, y in zip(E["v"], N1["v"]) if x is not None and y is not None]
            a = [float(x > 50) for x, _ in both]
            b = [float(y > 50) for _, y in both]
            rhos.append(corr(a, b))
            sd_pair.append(st.pstdev(d))
            sd_unpair.append(math.sqrt(st.pvariance(a) + st.pvariance(b)))
            pairs = [(E, N1)] + ([(N1, N2), (E, N2)] if N2 else [])
            for x, y in pairs:
                score_d.append(x["score"] - y["score"])
                teach_d.append(st.mean(paired(x["v"], y["v"])))
            if N2:
                dN.append(st.mean(paired(N1["v"], N2["v"])))
            print(f"  {r['seed']:>7} {r['card']:>4} {r['seen']:>4}  {win(E):>6.3f} {win(N1):>6.3f} "
                  f"{win(N2) if N2 else float('nan'):>6.3f}  {100 * m:>+6.1f} {100 * se:>5.1f}  "
                  f"{N1['name']} / {N2['name'] if N2 else '-'}")
        m, se = mse(dE)
        print(f"  mean Event - N1: {100 * m:+.1f} points of win chance (se {100 * se:.1f}); "
              f"Event better in {sum(x > 0 for x in dE)}, worse in {sum(x < 0 for x in dE)}")
        if len(dE) > 3:
            trim = sorted(dE, key=abs)[:-1]
            m2, se2 = mse(trim)
            print(f"  median {100 * st.median(dE):+.1f}; without the largest difference "
                  f"({100 * max(dE, key=abs):+.1f}): mean {100 * m2:+.1f} (se {100 * se2:.1f})")
        if dN:
            m, se = mse(dN)
            print(f"  mean N1 - N2: {100 * m:+.1f} (se {100 * se:.1f}); N1 better in {sum(x > 0 for x in dN)} "
                  f"of {len(dN)}, worse in {sum(x < 0 for x in dN)}")

    ok = [x for x in rhos if not math.isnan(x)]
    print(f"\nNoise (Event against N1, per decision): correlation of the paired playouts' wins "
          f"{st.mean(ok):.2f} (median {st.median(ok):.2f}); sd of a paired win difference "
          f"{st.mean(sd_pair):.2f} against {st.mean(sd_unpair):.2f} unpaired")
    sdp = st.mean(sd_pair)
    for target in (0.02, 0.01):
        print(f"  playouts per candidate for a se of {100 * target:.0f} points on one decision's difference: "
              f"{math.ceil((sdp / target) ** 2)}")
    print(f"Policy score differences against playout win differences (all pairs, {len(score_d)}): "
          f"correlation {corr(score_d, teach_d):.2f}; same sign in "
          f"{sum((s > 0) == (t > 0) for s, t in zip(score_d, teach_d) if t != 0)} of "
          f"{sum(t != 0 for t in teach_d)}")


if __name__ == "__main__":
    main(sys.argv[1:])
