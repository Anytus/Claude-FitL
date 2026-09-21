#!/usr/bin/env python3
"""usage_hook.py - PostToolUse hook: log the size of every tool call.

Claude Code runs this after each tool call with a JSON object on stdin
(tool_name, tool_input, tool_response, ...). It appends one line per call to
a log OUTSIDE the repository (~/.fitl-usage.log): timestamp, tool, a short
label (the command or file), input size and output size in characters.
Characters divided by four is a fair token estimate.

The log lives outside the working tree on purpose: a git commit is itself a
tool call, so a log inside the tree would be dirty again the instant a
commit finished. report.py copies the log into reports/<game>/usage.log
each time it runs, which is once per card, so the committed copy lags by a
few calls at most. tools/usage_report.py summarises either copy.

This is measurement only; it never changes what a tool does.
"""
import json
import os
import sys
import time

LOG = os.path.join(os.path.expanduser("~"), ".fitl-usage.log")


def label(tool, inp):
    if tool == "Bash":
        return (inp.get("command") or "")[:80].replace("\n", " ")
    for k in ("file_path", "path", "pattern", "url", "prompt"):
        if k in inp:
            return str(inp[k])[:80].replace("\n", " ")
    return ""


def size(x):
    if x is None:
        return 0
    if isinstance(x, str):
        return len(x)
    try:
        return len(json.dumps(x, ensure_ascii=False))
    except Exception:
        return len(str(x))


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tool = data.get("tool_name", "?")
    inp = data.get("tool_input") or {}
    resp = data.get("tool_response")
    line = "\t".join([
        time.strftime("%Y-%m-%dT%H:%M:%S"),
        tool,
        label(tool, inp).replace("\t", " "),
        str(size(inp)),
        str(size(resp)),
    ])
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
