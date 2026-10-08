#!/usr/bin/env python3
"""breadth.py - what US actions accomplish, and how many spaces were open to them:
the LLM's games against the bot's.

Usage: breadth.py LLM.jsonl BOT.jsonl

Input: one line per US card decision (fitl.Diag --saves for the LLM's saves;
FITL_ACTION_STATS for bot games): the action, what it did (Diag.actionStats:
spaces changed, spaces changed for the better, enemy pieces removed, bases
removed, Underground Guerrillas activated or removed, ARVN pieces and
Irregulars placed, US pieces to the map, COIN Control gained, NVA Control
broken, Support, Opposition, US score, best rival), the number of spaces each
US Operation could act in before and after (Diag.opportunity), and whether
passing would have left the US first eligible on the next card.
"""
import collections
import json
import statistics as st
import sys

STATS = ["spaces", "spaces_positive", "enemy_removed", "bases_removed", "underground_down", "arvn_placed",
         "sf_placed", "us_to_map", "coin_control_gained", "nva_control_lost", "support", "opposition",
         "us_score", "best_rival"]
OPP = ["assault", "sweep", "air_strike", "advise", "train_place", "train_pacify", "patrol", "coup_pacify"]
ACT = {"Op/Special Activity": "Op+SA", "Op Only": "Op only", "Limited Op": "LimOp", "Event": "Event", "Pass": "Pass"}


def stage(r):
    return "early" if r["seen"] <= 25 else "middle" if r["seen"] <= 51 else "late"


def mean(rs, f):
    xs = [f(r) for r in rs]
    return st.mean(xs) if xs else float("nan")


def table(title, groups, rows, fmt="{:>7.2f}"):
    names = list(groups)
    print(f"\n{title}")
    print(f"  {'':<24}" + "".join(f"{n:>12}" for n in names))
    print(f"  {'decisions':<24}" + "".join(f"{len(groups[n]):>12}" for n in names))
    for label, f in rows:
        print(f"  {label:<24}" + "".join(f"{mean(groups[n], f):>12.2f}" for n in names))


def main(llm_path, bot_path):
    llm = [json.loads(l) for l in open(llm_path)]
    bot = [json.loads(l) for l in open(bot_path)]
    for r in llm + bot:
        r["act"] = ACT.get(r["action"], r["action"])
    games = lambda rs: len({r["game"].split("/")[0] for r in rs})
    print(f"LLM: {len(llm)} US card decisions in {games(llm)} games; bot: {len(bot)} in {games(bot)} games")
    for name, rs in (("LLM", llm), ("bot", bot)):
        c = collections.Counter(r["act"] for r in rs)
        print(f"  {name}: " + ", ".join(f"{k} {100 * v / len(rs):.0f}%" for k, v in c.most_common()))

    for act in ("Op+SA", "LimOp", "Event"):
        g = {"LLM": [r for r in llm if r["act"] == act], "bot": [r for r in bot if r["act"] == act]}
        table(f"What a US {act} did (mean per action)", g, [(k, (lambda k: lambda r: r["stats"][k])(k)) for k in STATS])

    g = {}
    for s in ("early", "middle", "late"):
        g[f"LLM {s}"] = [r for r in llm if r["act"] == "Op+SA" and stage(r) == s]
        g[f"bot {s}"] = [r for r in bot if r["act"] == "Op+SA" and stage(r) == s]
    table("US Op+SA by game stage (cards seen 0-25, 26-51, 52-78)", g,
          [(k, (lambda k: lambda r: r["stats"][k])(k)) for k in ("spaces", "spaces_positive", "enemy_removed",
                                                                 "coin_control_gained", "support", "us_score", "best_rival")])

    g = {}
    for s in ("early", "middle", "late"):
        g[f"LLM {s}"] = [r for r in llm if stage(r) == s]
        g[f"bot {s}"] = [r for r in bot if stage(r) == s]
    table("Spaces open to each US Operation at the US's decisions (before acting), by stage", g,
          [(k, (lambda k: lambda r: r["opp_before"][k])(k)) for k in OPP])
    table("Change in those spaces made by the US's own action (after minus before), by stage", g,
          [(k, (lambda k: lambda r: r["opp_after"][k] - r["opp_before"][k])(k)) for k in OPP])

    per_game(llm, bot)

    print("\nTurn economy: if the US passed, would it be first eligible on the next card? (share of decisions, and what it did)")
    for name, rs in (("LLM", llm), ("bot", bot)):
        by = collections.defaultdict(list)
        for r in rs:
            by[r["first_next_if_pass"]].append(r)
        for k in ("first", "maybe", "not first", "coup next"):
            sub = by.get(k, [])
            if not sub:
                continue
            c = collections.Counter(r["act"] for r in sub)
            print(f"  {name:<4} {k:<10} {100 * len(sub) / len(rs):>4.0f}% of decisions: " +
                  ", ".join(f"{a} {100 * v / len(sub):.0f}%" for a, v in c.most_common()))
    print("\n  Pass rate by the next-card status, for each set of options the US had now:")
    for name, rs in (("LLM", llm), ("bot", bot)):
        for opt in ("full", "after Op", "after Op+SA"):
            row = []
            for k in ("first", "maybe", "not first", "coup next"):
                sub = [r for r in rs if r["options"] == opt and r["first_next_if_pass"] == k]
                if sub:
                    row.append(f"{k} {100 * sum(r['act'] == 'Pass' for r in sub) / len(sub):.0f}% of {len(sub)}")
            print(f"  {name:<4} {opt:<12} " + "; ".join(row))
    print("\n  When passing would leave the US first eligible next card, by the options it had now:")
    for name, rs in (("LLM", llm), ("bot", bot)):
        for opt in ("full", "after Op", "after Op+SA", "after Event"):
            sub = [r for r in rs if r["first_next_if_pass"] == "first" and r["options"] == opt]
            if sub:
                c = collections.Counter(r["act"] for r in sub)
                print(f"  {name:<4} options {opt:<12} {len(sub):>4}: " + ", ".join(f"{a} {100 * v / len(sub):.0f}%" for a, v in c.most_common()))


def per_game(llm, bot):
    """Totals per game: the LLM's games (all full) against the bot's games that reach the final Coup."""
    def by_game(rs):
        g = collections.defaultdict(list)
        for r in rs:
            g[r["game"].split("/")[0]].append(r)
        return g
    lg = by_game(llm)
    bg = {k: v for k, v in by_game(bot).items() if max(x["seen"] for x in v) >= 70}
    print("\nPer game, all US card decisions added up (LLM games; bot games that reach the final Coup):")
    for name, G in (("LLM", lg), ("bot", bg)):
        n = len(G)
        tot = lambda f: sum(f(r) for rs in G.values() for r in rs) / n
        print(f"  {name} ({n} games): decisions {tot(lambda r: 1):.1f}: Op+SA {tot(lambda r: r['act'] == 'Op+SA'):.1f}, "
              f"LimOp {tot(lambda r: r['act'] == 'LimOp'):.1f}, Event {tot(lambda r: r['act'] == 'Event'):.1f}, "
              f"Pass {tot(lambda r: r['act'] == 'Pass'):.1f}; spaces changed for the better "
              f"{tot(lambda r: r['stats']['spaces_positive']):.1f}, enemy pieces removed {tot(lambda r: r['stats']['enemy_removed']):.1f}, "
              f"Support {tot(lambda r: r['stats']['support']):+.1f}, US score {tot(lambda r: r['stats']['us_score']):+.1f}, "
              f"best rival {tot(lambda r: r['stats']['best_rival']):+.1f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
