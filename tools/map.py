#!/usr/bin/env python3
"""map.py - the static board: what is next to what.

Usage:
  map.py <space name>        neighbours of one space (prefix or case-insensitive match ok)
  map.py <space> <space>     are the two spaces adjacent?
  map.py all                 every space with its neighbours
  map.py locs                every LoC with the spaces it touches

Data comes from map.json (built once from the program's own adjacency table,
which is what the program uses to decide legal moves). Entries the program
lists in one direction only are marked with '*'; the printed board decides.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP_PATH = os.path.join(ROOT, "map.json")


def load():
    with open(MAP_PATH, encoding="utf-8") as f:
        return json.load(f)


def resolve(spaces, query):
    q = query.strip().lower()
    names = list(spaces)
    exact = [n for n in names if n.lower() == q]
    if exact:
        return exact[0]
    pre = [n for n in names if n.lower().startswith(q)]
    if len(pre) == 1:
        return pre[0]
    sub = [n for n in names if q in n.lower()]
    if len(sub) == 1:
        return sub[0]
    cands = pre or sub
    raise SystemExit(f"'{query}' is ambiguous or unknown" + (f": {', '.join(sorted(cands))}" if cands else ""))


def describe(spaces, name):
    sp = spaces[name]
    kind = "LoC" if sp["type"] == "LOC" else sp["type"].replace(" Province", "")
    if sp["type"] == "LOC":
        return f"{name} [LoC, econ {sp['population']}]"
    return f"{name} [{kind}, pop {sp['population']}" + (", coastal]" if sp["coastal"] else "]")


def neighbour_list(data, name):
    spaces = data["spaces"]
    one_way = {tuple(p) for p in data["one_way"]}
    out = []
    for n in spaces[name]["adjacent"]:
        mark = "*" if (name, n) in one_way else ""
        out.append(n + mark)
    return out


def main(argv):
    data = load()
    spaces = data["spaces"]
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "all":
        for name in sorted(spaces, key=lambda n: (spaces[n]["type"] == "LOC", n)):
            print(f"{describe(spaces, name)}: " + ", ".join(neighbour_list(data, name)))
        if data["one_way"]:
            print("\n* listed by the program in this direction only; check the board.")
        return 0
    if argv[0] == "locs":
        for name in sorted(n for n in spaces if spaces[n]["type"] == "LOC"):
            print(f"{describe(spaces, name)}: " + ", ".join(neighbour_list(data, name)))
        return 0
    if len(argv) == 2:
        a, b = resolve(spaces, argv[0]), resolve(spaces, argv[1])
        ab = b in spaces[a]["adjacent"]
        ba = a in spaces[b]["adjacent"]
        if ab and ba:
            print(f"yes: {a} and {b} are adjacent")
        elif ab or ba:
            print(f"one-way in the program's table: {a if ab else b} lists {b if ab else a}, not back. Check the board.")
        else:
            print(f"no: {a} and {b} are not adjacent")
        return 0
    name = resolve(spaces, " ".join(argv))
    print(describe(spaces, name))
    for n in neighbour_list(data, name):
        bare = n.rstrip("*")
        print(f"  {describe(spaces, bare)}{' *' if n.endswith('*') else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
