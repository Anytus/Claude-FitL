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
    for m in re.finditer(r'(\w+)\s*->\s*Set\(([^)]*)\)', body):
        key = consts[m.group(1)]
        neigh = [consts[x.strip()] for x in m.group(2).split(",") if x.strip()]
        spaces[key]["adjacent"] = sorted(neigh)

    # checks: 47 spaces, every neighbour known, adjacency symmetric.
    # The program's table is what governs legal moves, so it is stored as is;
    # one-way entries are recorded so the board view can flag them.
    problems = []
    one_way = []
    if len(spaces) != 47:
        problems.append(f"expected 47 spaces, found {len(spaces)}")
    for name, sp in sorted(spaces.items()):
        if not sp["adjacent"]:
            problems.append(f"{name}: no adjacency entry")
        for n in sp["adjacent"]:
            if n not in spaces:
                problems.append(f"{name}: unknown neighbour {n}")
            elif name not in spaces[n]["adjacent"]:
                one_way.append([name, n])

    out = {"spaces": spaces, "one_way": one_way,
           "note": "Adjacency as the fitl program has it (v1.53). Entries in one_way are "
                   "listed from the first space to the second but not back; the printed "
                   "board decides which direction is right."}
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
