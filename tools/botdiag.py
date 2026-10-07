#!/usr/bin/env python3
"""botdiag.py - diagnostic report for traced all-Bot games.

Usage: botdiag.py TRACE.jsonl     (botrun.py --trace output)

Prints: winners and how games end; for each campaign that ends with a Bot
over its line, where that Bot's points came from (by faction and Event/Op,
plus the previous Coup round); the US's final-Coup losses; means at each
Victory check (US score, best rival, Support, US Aid, ARVN Resources,
Troops Available); and, for games reaching the final Coup, Support and ARVN
Resources gained or lost per game by source, and the US action mix.
Campaign boundaries are rebuilt from the score components in the trace.
"""
import collections
import json
import statistics as st
import sys

RIVALS = ("ARVN", "NVA", "VC")


def score(c, f):
    return {"US": c["sup"] + c["usav"] - 50, "ARVN": c["coin"] + c["pat"] - 50,
            "NVA": c["nvac"] + c["nvab"] - 18, "VC": c["opp"] + c["vcb"] - 35}[f]


def dscore(d, f):
    g = lambda k: d.get(k, 0)
    return {"US": g("sup") + g("usav"), "ARVN": g("coin") + g("pat"),
            "NVA": g("nvac") + g("nvab"), "VC": g("opp") + g("vcb")}[f]


def kind(a):
    if a.get("ev") == "Pivotal":
        return a["f"] + " Pivotal"
    return a["f"] + {"Event": " Event", "Pass": " Pass"}.get(a["a"], " Op")


def campaigns(r):
    """Yield (coup number, actions in the campaign, coup record, round delta before)."""
    keys = list(r["initial"])
    cum = dict(r["initial"])
    k, cur, prev_round = 0, [], {}
    coups = r["coups"]
    for a in r["actions"] + [None]:
        while k < len(coups) and all(cum[x] == coups[k]["at"].get(x, cum[x]) for x in keys):
            yield k + 1, cur, coups[k], prev_round
            prev_round = coups[k]["d"]
            for x, v in prev_round.items():
                cum[x] = cum.get(x, 0) + v
            cur, k = [], k + 1
        if a is None:
            break
        for x, v in a["d"].items():
            cum[x] = cum.get(x, 0) + v
        cur.append(a)


def main(path):
    rs = [r for r in map(json.loads, open(path)) if not r.get("error")]
    n = len(rs)
    early = [r for r in rs if r["end_coup"] != 6]
    fin = [r for r in rs if r["end_coup"] == 6]
    print(f"{n} games. Winners: " + ", ".join(f"{f} {100 * sum(r['winner'] == f for r in rs) / n:.1f}%"
                                              for f in ("US",) + RIVALS))
    print(f"Ended early (a Bot over its line): {len(early)} ({100 * len(early) / n:.0f}%), by Coup "
          f"{dict(sorted(collections.Counter(r['end_coup'] for r in early).items()))}, by Bot "
          f"{dict(collections.Counter(r['winner'] for r in early))}")
    lf = [r for r in fin if r["winner"] != "US"]
    if lf:
        print(f"Reached the final Coup: {len(fin)}; US won {sum(r['winner'] == 'US' for r in fin)}; lost {len(lf)}, "
              f"US {st.mean(r['final_scores']['US'] for r in lf):+.1f} against the winner "
              f"{st.mean(r['final_scores'][r['winner']] for r in lf):+.1f}; a Bot over its line at the final check in "
              f"{sum(1 for r in lf if any(r['coups'][-1]['victory_check'][f] > 0 for f in RIVALS))}")

    print("\nCampaigns that end with a Bot over its line, against those it stays under (not final):")
    for F in ("VC", "NVA", "ARVN"):
        groups = {"crossed": [], "stayed under": []}
        for r in rs:
            for c, acts, coup, prev_round in campaigns(r):
                crossed = coup["victory_check"][F] > 0
                if c == 6 and not crossed:
                    continue
                start = coup["victory_check"][F] - sum(dscore(a["d"], F) for a in acts)
                src = collections.Counter()
                for a in acts:
                    src[kind(a)] += dscore(a["d"], F)
                groups["crossed" if crossed else "stayed under"].append((start, dscore(prev_round, F), src, coup["victory_check"][F]))
        for name, g in groups.items():
            if not g:
                continue
            tot = collections.Counter()
            for _, _, s, _ in g:
                tot.update(s)
            top = sorted(tot.items(), key=lambda kv: -abs(kv[1]))[:6]
            print(f"  {F} {name} ({len(g)}): start {st.mean(x[0] for x in g):+.1f} (previous Coup round "
                  f"{st.mean(x[1] for x in g):+.1f}), gain {st.mean(x[3] - x[0] for x in g):+.1f}: "
                  + ", ".join(f"{k} {v / len(g):+.2f}" for k, v in top))

    print("\nMeans at each Victory check, games reaching it:")
    print(f"  {'Coup':<5}{'n':>5}{'US':>7}{'rival':>7}{'Support':>9}{'Aid':>6}{'ARVN Res':>9}{'Avail':>7}{'round Sup':>10}")
    for c in range(6):
        cs = [r["coups"][c] for r in rs if len(r["coups"]) > c]
        if not cs:
            continue
        m = lambda f: st.mean(f(x) for x in cs)
        at = lambda key: m(lambda x: x["at"].get(key, 0))
        print(f"  C{c + 1:<4}{len(cs):>5}{m(lambda x: x['victory_check']['US']):>+7.1f}"
              f"{m(lambda x: max(x['victory_check'][f] for f in RIVALS)):>+7.1f}{at('sup'):>9.1f}{at('aid'):>6.1f}"
              f"{at('ares'):>9.1f}{at('usav'):>7.1f}{m(lambda x: x['d'].get('sup', 0)):>+10.1f}")

    for key, label in (("sup", "Support"), ("ares", "ARVN Resources")):
        tot = collections.Counter()
        for r in fin:
            for a in r["actions"]:
                tot[kind(a)] += a["d"].get(key, 0)
            for c in r["coups"]:
                tot["Coup round"] += c["d"].get(key, 0)
        print(f"\n{label} per game reaching the final Coup ({len(fin)}), by source: "
              + ", ".join(f"{k} {v / len(fin):+.1f}" for k, v in sorted(tot.items(), key=lambda kv: -abs(kv[1]))
                          if abs(v / len(fin)) >= 0.1))
    acts = collections.Counter()
    for r in fin:
        for a in r["actions"]:
            if a["f"] == "US":
                acts[a["a"]] += 1
    tot = sum(acts.values())
    print(f"\nUS actions per game reaching the final Coup: {tot / len(fin):.1f}; "
          + ", ".join(f"{k} {100 * v / tot:.0f}%" for k, v in acts.most_common()))


if __name__ == "__main__":
    main(sys.argv[1])
