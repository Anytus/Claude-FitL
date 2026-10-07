#!/usr/bin/env python3
"""teacher_spread.py - how far apart the labelled alternatives truly are.

Usage: teacher_spread.py FILE [--space] [--kind turn|coup]

For every alternative (each candidate after the first, the bot's choice), the
paired win difference against the bot's choice is a noisy estimate of the
true difference. Two estimates of the true spread across alternatives:
  noise model: observed variance minus the mean sampling variance of a paired mean;
  split half:  the covariance between the estimates from the two halves of the
               playouts (independent noise, the same true difference),
               also without the alternatives in the top and bottom 1%.
Then the gain of a perfect chooser among the tested alternatives under a normal
model (true differences independent N(mean, spread)), with both spreads.
--space keeps only variants applied in 90% of their playouts (space-mode files).
"""
import json
import math
import random
import statistics as st
import sys


def main(argv):
    space = "--space" in argv
    kind = argv[argv.index("--kind") + 1] if "--kind" in argv else None
    path = argv[0]
    seen, decs = set(), []
    for line in open(path):
        r = json.loads(line)
        key = (r.get("kind", "turn"), r["seed"], r["i"], r["card"], r["seen"], r.get("coups", 0))
        if key in seen or (kind and r.get("kind", "turn") != kind):
            continue
        seen.add(key)
        cs = r["cands"]
        if space:
            cs = [cs[0]] + [c for c in cs[1:] if c["applied"] >= 0.9 * r["playouts"]]
        if len(cs) > 1:
            decs.append(cs)
    full, nvar, ha, hb, per_dec = [], [], [], [], []
    for cs in decs:
        base = cs[0]["v"]
        h = len(base) // 2
        k = 0
        for c in cs[1:]:
            d = [(x > 50) - (y > 50) for x, y in zip(c["v"], base) if x is not None and y is not None]
            a = [(x > 50) - (y > 50) for x, y in zip(c["v"][:h], base[:h]) if x is not None and y is not None]
            b = [(x > 50) - (y > 50) for x, y in zip(c["v"][h:], base[h:]) if x is not None and y is not None]
            if len(a) < 10 or len(b) < 10:
                continue
            full.append(st.mean(d)); nvar.append(st.pvariance(d) / len(d))
            ha.append(st.mean(a)); hb.append(st.mean(b)); k += 1
        if k:
            per_dec.append(k)
    mu = st.mean(full)
    obs = st.pvariance(full)
    sd_noise = math.sqrt(max(obs - st.mean(nvar), 0))

    def cov(x, y):
        mx, my = st.mean(x), st.mean(y)
        return sum((p - mx) * (q - my) for p, q in zip(x, y)) / (len(x) - 1)
    sd_split = math.sqrt(max(cov(ha, hb), 0))
    order = sorted(range(len(full)), key=lambda i: full[i])
    t = max(1, len(full) // 100)
    keep = order[t:-t]
    sd_trim = math.sqrt(max(cov([ha[i] for i in keep], [hb[i] for i in keep]), 0))
    print(f"{path}{' (' + kind + ')' if kind else ''}: {len(full)} alternatives in {len(per_dec)} decisions")
    print(f"  mean alternative minus the bot's choice {100 * mu:+.1f} points of win chance")
    print(f"  spread (sd) observed {100 * math.sqrt(obs):.1f}; true, by the noise model {100 * sd_noise:.1f}, "
          f"by split halves {100 * sd_split:.1f}, split halves without the top and bottom 1% {100 * sd_trim:.1f}")
    rng = random.Random(2)
    for label, sd in (("split-half spread", sd_split), ("trimmed spread", sd_trim)):
        g = [max(0.0, max(rng.gauss(mu, sd) for _ in range(per_dec[i % len(per_dec)]))) for i in range(20000)]
        print(f"  perfect choice among the tested alternatives ({label}): +{100 * st.mean(g):.1f} points a decision")


if __name__ == "__main__":
    main(sys.argv[1:])
