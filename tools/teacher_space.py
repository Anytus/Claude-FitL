#!/usr/bin/env python3
"""teacher_space.py - summarize a Teacher space-choice run (FITL_TEACHER_MODE=space).

Usage: teacher_space.py FILE... [--list N]

Each line is one decision ("kind": "turn" for a US action's space picks,
"coup" for the US Bot's Support-phase Pacify picks): the choice as played and
up to 3 variants, each changing one space pick, played to the end of the game
the same number of times on common seeds. A win is a playout value above 50.
Duplicate decisions (a game played again after a restart) are dropped;
variants applied in fewer than 90% of their playouts are left out.

Prints, for turns and Coups separately: S1 the held-out regret of the choice as
played against the playout-best candidate (best chosen on one half of the
playouts, measured on the other, both ways); S2 S1 by action; S3 the mean
variant minus the choice as played, by the changed pick's first priority; and
(--list N) the decisions where the best variant gains most over all playouts.
"""
import collections
import json
import math
import statistics as st
import sys


def rate(vs):
    w = [v > 50 for v in vs if v is not None]
    return st.mean(w) if w else float("nan")


def mse(xs):
    if not xs:
        return float("nan"), float("nan")
    return st.mean(xs), (st.stdev(xs) / math.sqrt(len(xs)) if len(xs) > 1 else float("nan"))


def regret(r):
    cs = r["cands"]
    n = r["playouts"]
    h = n // 2
    out = []
    for a, b in ((slice(0, h), slice(h, n)), (slice(h, n), slice(0, h))):
        best = max(range(len(cs)), key=lambda i: rate(cs[i]["v"][a]))
        out.append(rate(cs[best]["v"][b]) - rate(cs[0]["v"][b]))
    return st.mean(out)


def load(paths):
    seen, rs, dropped = set(), [], collections.Counter()
    for p in paths:
        for line in open(p):
            if not line.startswith("{"):
                continue
            r = json.loads(line)
            key = (r["kind"], r["seed"], r["i"], r["card"], r["seen"], r["coups"])
            if key in seen:
                dropped["duplicate"] += 1
                continue
            seen.add(key)
            keep = [r["cands"][0]] + [c for c in r["cands"][1:] if c["applied"] >= 0.9 * r["playouts"]]
            dropped["variants not applied"] += len(r["cands"]) - len(keep)
            if len(keep) < 2:
                dropped["decisions with no applied variant"] += 1
                continue
            r["cands"] = keep
            rs.append(r)
    return rs, dropped


def row(label, g):
    m, se = mse([regret(r) for r in g])
    print(f"  {label:<44} {len(g):>4}  {100 * m:>+6.1f} {100 * se:>5.1f}  {100 * st.median([regret(r) for r in g]):>+6.1f}")


def main(argv):
    nlist = 0
    if "--list" in argv:
        i = argv.index("--list")
        nlist = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    rs, dropped = load(argv)
    npl = sum(r["playouts"] * len(r["cands"]) for r in rs)
    print(f"{len(rs)} decisions ({sum(r['kind'] == 'turn' for r in rs)} turn, {sum(r['kind'] == 'coup' for r in rs)} Coup) "
          f"from {len({r['seed'] for r in rs})} games, {npl} playouts kept; dropped: {dict(dropped)}")
    for kind, title in (("turn", "US turns: space picks inside the chosen action"),
                        ("coup", "Coup rounds: the US Bot's Support-phase Pacify picks")):
        g = [r for r in rs if r["kind"] == kind]
        if not g:
            continue
        print(f"\n== {title}")
        print(f"  {'S1 held-out regret of the choice as played':<44} {'n':>4}  {'mean':>6} {'se':>5}  {'median':>6}")
        row("all", g)
        if kind == "turn":
            by = collections.defaultdict(list)
            for r in g:
                by[r["action"].split(" @")[0]].append(r)
            for k in sorted(by, key=lambda k: -len(by[k]))[:8]:
                row("action " + k, by[k])
        else:
            for label, f in (("not the final Coup", lambda r: r["coups"] < 5), ("final Coup", lambda r: r["coups"] == 5)):
                sub = [r for r in g if f(r)]
                if sub:
                    row(label, sub)
        diffs = collections.defaultdict(list)
        for r in g:
            base = r["cands"][0]["v"]
            for c in r["cands"][1:]:
                d = [(x > 50) - (y > 50) for x, y in zip(c["v"], base) if x is not None and y is not None]
                if d:
                    diffs[c["pick"]["priority"] or "(none)"].append(st.mean(d))
        allv = [x for v in diffs.values() for x in v]
        m, se = mse(allv)
        print(f"  S3 variant minus as played: {100 * m:+.1f} (se {100 * se:.1f}) over {len(allv)} variants; "
              f"variant better in {sum(x > 0 for x in allv)}, worse in {sum(x < 0 for x in allv)}")
        for k in sorted(diffs, key=lambda k: -len(diffs[k]))[:10]:
            m, se = mse(diffs[k])
            print(f"     {k[:60]:<60} {len(diffs[k]):>4}  {100 * m:>+6.1f} {100 * se:>5.1f}")
        if nlist:
            print(f"  Decisions where the best variant gains most (all playouts):")
            def gain(r):
                return max(rate(c["v"]) for c in r["cands"][1:]) - rate(r["cands"][0]["v"])
            for r in sorted(g, key=gain, reverse=True)[:nlist]:
                b = max(r["cands"][1:], key=lambda c: rate(c["v"]))
                print(f"    seed {r['seed']} card {r['card']:>3} seen {r['seen']:>2} {r.get('action', 'Coup')[:30]:<30} "
                      f"as played {rate(r['cands'][0]['v']):.2f}, {b['name'][:50]} {rate(b['v']):.2f} "
                      f"({b['pick']['priority'][:40]})")


if __name__ == "__main__":
    main(sys.argv[1:])
