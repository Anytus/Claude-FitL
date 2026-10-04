#!/usr/bin/env python3
"""botrun.py - play many seeded all-Bot games headless, in parallel.

Usage:
  botrun.py --games 1000 [--seed 1] [--workers 4] [--us-final-only]
            [--timeout 10] [--out results/run.jsonl] [--via-main]
  botrun.py --summary results/run.jsonl

Each game is played by `fitl.Autoplay` (in the harness jar): all four
factions are the program's Tru'ng Bots, the event deck is built from the
seed as the Full scenario requires, and the program's console output is
discarded. The same seed always plays the same game. One JSON line per game
is appended to --out.

--us-final-only  the US Bot may not win before the final Coup, matching the
                 condition of the recent human-US games.
--via-main       validation: play each game through the program's own
                 interactive main loop (saves written to a scratch directory)
                 instead of the Autoplay loop. Same seeds give the same games.

Some seeds send a Bot into a loop that never ends; Autoplay's watchdog
reports those as "timeout" and the worker restarts at the next seed.
"""
import argparse
import json
import os
import statistics as st
import subprocess
import sys
import tempfile
import threading
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "fitl", "lib")
FACTIONS = ["US", "ARVN", "NVA", "VC"]


def classpath():
    return os.environ.get("FITL_CP") or os.path.join(LIB, "*")


def run_range(first, count, args, out_lock, out_f, progress):
    """Play seeds first .. first+count-1, restarting after a timed-out seed."""
    seed, end = first, first + count
    cwd = tempfile.mkdtemp(prefix="botrun-") if args.via_main else ROOT
    env = {k: v for k, v in os.environ.items() if k != "JAVA_TOOL_OPTIONS"}
    while seed < end:
        cmd = ["java", "-Xss8m", "-cp", classpath(), "fitl.Autoplay",
               "--seed", str(seed), "--games", str(end - seed),
               "--timeout", str(args.timeout)]
        if args.us_final_only:
            cmd.append("--us-final-only")
        if args.via_main:
            cmd.append("--via-main")
        proc = subprocess.Popen(cmd, cwd=cwd, env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL, text=True)
        last = seed - 1
        for line in proc.stdout:
            line = line.strip()
            if not line.startswith("{"):
                continue
            rec = json.loads(line)
            last = rec["seed"]
            with out_lock:
                out_f.write(line + "\n")
                out_f.flush()
                progress[0] += 1
        proc.wait()
        seed = last + 1
        if proc.returncode not in (0, 3) and seed < end:
            # crashed without a record for this seed: log it and move on
            with out_lock:
                out_f.write(json.dumps({"seed": seed, "error": f"jvm exit {proc.returncode}"}) + "\n")
                progress[0] += 1
            seed += 1


def run(args):
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    n, w = args.games, max(1, args.workers)
    chunks, start = [], args.seed
    for i in range(w):
        size = n // w + (1 if i < n % w else 0)
        if size:
            chunks.append((start, size))
            start += size
    lock, progress = threading.Lock(), [0]
    t0 = time.time()
    with open(args.out, "a", encoding="utf-8") as f:
        threads = [threading.Thread(target=run_range, args=(a, c, args, lock, f, progress))
                   for a, c in chunks]
        for t in threads:
            t.start()
        while any(t.is_alive() for t in threads):
            time.sleep(5)
            print(f"\r{progress[0]}/{n} games, {time.time() - t0:.0f}s", end="", file=sys.stderr)
        for t in threads:
            t.join()
    print(f"\r{progress[0]}/{n} games in {time.time() - t0:.0f}s -> {args.out}", file=sys.stderr)
    summary(args.out)


def summary(path):
    recs = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    ok = [r for r in recs if not r.get("error")]
    bad = [r for r in recs if r.get("error")]
    print(f"games {len(recs)}: completed {len(ok)}, failed {len(bad)}")
    kinds = {}
    for r in bad:
        k = r["error"].split(":")[0]
        kinds[k] = kinds.get(k, 0) + 1
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print(f"  failed: {k} x{v}")
    if not ok or "winner" not in ok[0]:
        return
    print("\nwinner           games   share")
    wins = {}
    for r in ok:
        wins[r["winner"]] = wins.get(r["winner"], 0) + 1
    for f in sorted(wins, key=lambda x: -wins[x]):
        print(f"  {f:<14} {wins[f]:>5}   {100 * wins[f] / len(ok):5.1f}%")
    print("\ngame ended at   games   share")
    ends = {}
    for r in ok:
        ends[r["end_coup"]] = ends.get(r["end_coup"], 0) + 1
    for c in sorted(ends):
        label = "final Coup" if c == 6 else f"Coup {c}"
        print(f"  {label:<14} {ends[c]:>5}   {100 * ends[c] / len(ok):5.1f}%")
    print("\nfinal margin     mean     sd     min    max")
    for f in FACTIONS:
        xs = [r["final_scores"][f] for r in ok]
        sd = st.stdev(xs) if len(xs) > 1 else 0.0
        print(f"  {f:<12} {st.mean(xs):+6.1f} {sd:6.1f} {min(xs):+6d} {max(xs):+6d}")
    secs = [r.get("secs", 0) for r in ok]
    print(f"\nseconds per game: mean {st.mean(secs):.2f}, max {max(secs):.2f}")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--games", type=int, default=100)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    p.add_argument("--timeout", type=int, default=10)
    p.add_argument("--us-final-only", action="store_true")
    p.add_argument("--via-main", action="store_true")
    p.add_argument("--out", default=os.path.join(ROOT, "results", "botrun.jsonl"))
    p.add_argument("--summary", metavar="JSONL")
    args = p.parse_args()
    if args.summary:
        summary(args.summary)
    else:
        run(args)


if __name__ == "__main__":
    main()
