#!/usr/bin/env python3
"""usage_report.py - summarise usage.log (written by the PostToolUse hook).

Prints, per tool and per kind of Bash command (ctl send/seq/advance, render,
diff, report, git, file edits...), the number of calls and the input and
output volume in characters and estimated tokens (chars / 4). Also the
grand totals, so 'unattributed' context growth can be pinned down.

Usage: usage_report.py [path]   (default: reports/<game>/usage.log if one
                                 game is present, else ~/.fitl-usage.log)
"""
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def kind(tool, label):
    if tool != "Bash":
        return tool
    m = re.search(r"tools/(\w+)\.py\s*(\S*)", label)
    if m:
        script, sub = m.group(1), m.group(2)
        return f"{script} {sub}" if script == "ctl" else script
    if label.startswith("git") or " git " in label:
        return "git"
    if label.startswith("cat ") or ">>" in label or label.startswith("printf") or label.startswith("echo"):
        return "shell write/append"
    return "shell other"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if path is None:
        games = sorted(d for d in os.listdir(os.path.join(ROOT, "reports")) if
                       os.path.isfile(os.path.join(ROOT, "reports", d, "usage.log"))) \
            if os.path.isdir(os.path.join(ROOT, "reports")) else []
        path = os.path.join(ROOT, "reports", games[0], "usage.log") if len(games) == 1 \
            else os.path.join(os.path.expanduser("~"), ".fitl-usage.log")
    calls = defaultdict(int)
    inp = defaultdict(int)
    out = defaultdict(int)
    n = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) != 5:
                continue
            _, tool, label, i, o = parts
            k = kind(tool, label)
            calls[k] += 1
            inp[k] += int(i)
            out[k] += int(o)
            n += 1
    print(f"{'kind':<24}{'calls':>6}{'in chars':>10}{'out chars':>11}{'~tokens':>9}")
    total_i = total_o = 0
    for k in sorted(calls, key=lambda k: -(inp[k] + out[k])):
        total_i += inp[k]
        total_o += out[k]
        print(f"{k:<24}{calls[k]:>6}{inp[k]:>10}{out[k]:>11}{(inp[k] + out[k]) // 4:>9}")
    print(f"{'TOTAL':<24}{n:>6}{total_i:>10}{total_o:>11}{(total_i + total_o) // 4:>9}")
    print("\nTool inputs and outputs both enter the context once. Not counted here: the")
    print("model's own reply text and reasoning, and the files it reads at session start.")


if __name__ == "__main__":
    main()
