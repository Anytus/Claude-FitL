#!/bin/bash
# teach_run.sh - run a Teacher labelling job as W workers over a fixed schedule
# of games, resumable, with a progress file.
#
# Usage: teach_run.sh JAR POLICY OUTDIR FIRST_SEED GAMES_PER_WORKER WORKERS [NAME]
#   Teacher settings come from the environment (FITL_TEACHER_MODE, ..._N, ...);
#   FITL_TEACHER is set to OUTDIR/lab. Worker w plays seeds
#   FIRST_SEED + w*1000 + 0..GAMES_PER_WORKER-1, one JVM per game, appending
#   to OUTDIR/games<w>.jsonl; a seed already there is skipped, so after a
#   container restart the same command picks up where it stopped (the labels
#   of a game cut off are written again; tools/teacher_space.py drops
#   duplicates). OUTDIR/PROGRESS.txt is rewritten every minute (teach_progress.sh).
set -u
JAR=$1; POL=$2; OUT=$3; FIRST=$4; PER=$5; W=$6; NAME=${7:-Teacher run}
cd "$(dirname "$0")/.."
L=fitl/lib
CP="$JAR:$L/scala-library-2.13.18.jar:$L/scala-parser-combinators_2.13-2.1.1.jar"
mkdir -p "$OUT"
TOTAL=$((PER * W))
[ -f "$OUT/started" ] || date -u +%s > "$OUT/started"

worker() {
  local w=$1
  for ((i = 0; i < PER; i++)); do
    local s=$((FIRST + w * 1000 + i))
    grep -q "\"seed\":$s," "$OUT/games$w.jsonl" 2>/dev/null && continue
    FITL_TEACHER="$OUT/lab" env -u JAVA_TOOL_OPTIONS java -Xss8m -cp "$CP" fitl.Autoplay --seed $s --games 1 \
      --timeout 100000 --us-final-only --us-player --us-policy "$POL" >> "$OUT/games$w.jsonl" 2>> "$OUT/err$w.txt"
  done
}

for ((w = 0; w < W; w++)); do worker $w & done
sleep 5
bash tools/teach_progress.sh "$OUT" "$TOTAL" "$NAME" &
wait
