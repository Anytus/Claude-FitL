#!/usr/bin/env python3
"""Build map.json (the static board: spaces and adjacency) from the fitl source.

Usage: build_map.py <path-to-fitl-source-root> [out.json]

Reads src/main/scala/fitl/FireInTheLake.scala for:
  - the space-name constants (`val Hue = "Hue"`, `val LOC_Hue_DaNang = "LOC Hue -- Da Nang"`)
  - the default space definitions (`Space(Hue, City, 2, coastal = true)`)
  - the adjacency table (`Hue -> Set(QuangTri_ThuaThien, LOC_Hue_KheSanh, ...)`)

Everything extracted is printed on the physical game board (names, terrain,
population / econ, coastal, and which spaces touch which), so it is fair for
the playing model to see. Build-time only; the source stays outside the repo.
"""
import json
import os
import re
import sys


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    src = os.path.join(sys.argv[1], "src", "main", "scala", "fitl", "FireInTheLake.scala")
    out_path = sys.argv[2] if len(sys.argv) > 2 else "map.json"
    text = open(src, encoding="utf-8").read()

    # 1. name constants
    consts = dict(re.findall(r'^\s*val\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"([^"]+)"\s*$', text, re.M))

    # 2. default spaces
    spaces = {}
    for m in re.finditer(r'val Default_\w+\s*=\s*Space\(\s*(\w+)\s*,\s*(\w+)\s*,\s*(\d+)\s*(,\s*coastal\s*=\s*true)?\s*\)', text):
        ident, stype, pop, coastal = m.groups()
        name = consts[ident]
        spaces[name] = {
            "type": {"City": "City", "HighlandProvince": "Highland Province", "LowlandProvince": "Lowland Province",
                     "JungleProvince": "Jungle Province", "LoC": "LOC"}[stype],
            "population": int(pop),        # econ value for LoCs
            "coastal": bool(coastal),
            "adjacent": [],
        }

    # 3. adjacency table
    start = text.index("val adjacencyMap")
    end = text.index("def getAdjacent(", start)
    body = text[start:end]
    raw = {}
    for m in re.finditer(r'(\w+)\s*->\s*Set\(([^)]*)\)', body):
        key = consts[m.group(1)]
        raw[key] = {consts[x.strip()] for x in m.group(2).split(",") if x.strip()}

    # Adjacency is symmetric (rules 1.3.6). The release table listed three
    # junction adjacencies in one direction only; the harness's program patch
    # closes the table under symmetry, and so does this builder. The raw
    # one-way entries are recorded for the record.
    problems = []
    one_way = []
    if len(spaces) != 47:
        problems.append(f"expected 47 spaces, found {len(spaces)}")
    for name in sorted(raw):
        for n in raw[name]:
            if n not in spaces:
                problems.append(f"{name}: unknown neighbour {n}")
            elif name not in raw.get(n, ()):
                one_way.append([name, n])
    for name in spaces:
        adj = set(raw.get(name, ())) | {o for o, oa in raw.items() if name in oa}
        if not adj:
            problems.append(f"{name}: no adjacency entry")
        spaces[name]["adjacent"] = sorted(adj)

    out = {"spaces": spaces, "one_way": [],
           "raw_one_way_in_release_table": one_way,
           "note": "Adjacency per rules 1.3.6, symmetric. Built from the fitl program's table "
                   "closed under symmetry (the harness build of the program does the same)."}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, sort_keys=True)
    print(f"wrote {len(spaces)} spaces to {out_path}")
    for a, b in one_way:
        print(f"ONE-WAY in program table: {a} -> {b} (not listed back)")
    for p in problems:
        print("PROBLEM:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
