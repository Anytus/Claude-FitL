#!/bin/bash
# teach_progress.sh - write OUTDIR/PROGRESS.txt for a teach_run.sh job, once a
# minute until every scheduled game is done or no Java process is left.
# Usage: teach_progress.sh OUTDIR TOTAL_GAMES [NAME]
OUT=$1; TOTAL=$2; NAME=${3:-Teacher run}
while true; do
  done_games=$(cat "$OUT"/games*.jsonl 2>/dev/null | grep -c '"seed"')
  turn=$(cat "$OUT"/lab.* 2>/dev/null | grep -c '"kind":"turn"')
  coup=$(cat "$OUT"/lab.* 2>/dev/null | grep -c '"kind":"coup"')
  running=$(pgrep -c -x java)
  start=$(cat "$OUT/started" 2>/dev/null || date -u +%s); now=$(date -u +%s)
  eta="unknown until the first game finishes"
  if [ "$done_games" -gt 0 ] && [ "$done_games" -lt "$TOTAL" ]; then
    left=$(( (now - start) * (TOTAL - done_games) / done_games ))
    eta="about $((left / 60)) min more, around $(date -u -d @$((now + left)) +%H:%M) UTC"
  fi
  {
    echo "$NAME"
    echo "Games: $done_games of $TOTAL done ($((100 * done_games / TOTAL))%)"
    echo "Decisions labelled: $turn US-turn space choices, $coup Coup Support-phase Pacify"
    echo "Java processes running: $running (0 while games remain means the run has stopped)"
    echo "Started $(date -u -d @$start +%H:%M) UTC; updated $(date -u +%H:%M) UTC; finish: $eta"
    if [ "$done_games" -ge "$TOTAL" ]; then echo "FINISHED"; fi
  } > "$OUT/PROGRESS.txt.new"
  mv "$OUT/PROGRESS.txt.new" "$OUT/PROGRESS.txt"
  if [ "$done_games" -ge "$TOTAL" ] || [ "$running" -eq 0 ]; then break; fi
  sleep 60
done
