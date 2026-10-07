#!/usr/bin/env python3
"""botcalib.py - calibration of playout risk estimates.

Usage:
  FITL_CALIBRATE=30 FITL_CALIBRATE_OUT=/tmp/c/cal botrun.py ... --out games.jsonl   # writes /tmp/c/cal.<pid>
  botcalib.py '/tmp/c/cal.*' games.jsonl

After each US action Autoplay estimates, from FITL_CALIBRATE playouts, the
chance that a Bot is over its line at the next Victory check
(FITL_ROLLOUT_SEARCH=1: the US plays by its search policy in the playouts,
else by its Tru'ng routines). This compares those estimates with what
happened at that check in the same game, by bins of predicted risk.
"""
import json,glob,sys,collections,statistics as st
logs, games = sys.argv[1], sys.argv[2]
G={r['seed']:r for r in map(json.loads,open(games)) if not r.get('error')}
pts=[]
for p in glob.glob(logs):
    for l in open(p):
        d=json.loads(l)
        r=G.get(d['seed'])
        if not r or d['coups']>=len(r['coups']): continue
        vc=r['coups'][d['coups']]['victory_check']
        actual=any(vc[f]>0 for f in ['ARVN','NVA','VC'])
        pts.append((d['p_loss'],actual,d['seen']))
print(f"{len(pts)} US decisions with an estimate, from {len(set(G))} games")
bins=[0,0.001,0.1,0.2,0.3,0.5,0.7,1.01]
print(f"{'predicted risk':<16}{'decisions':>10}{'mean predicted':>16}{'observed':>10}")
for lo,hi in zip(bins,bins[1:]):
    b=[(p,a) for p,a,_ in pts if lo<=p<hi]
    if b: print(f"{lo:>5.2f}-{hi:<9.2f}{len(b):>10}{st.mean(p for p,_ in b):>16.3f}{sum(a for _,a in b)/len(b):>10.3f}")
P=[p for p,_,_ in pts]; A=[1.0 if a else 0.0 for _,a,_ in pts]
brier=st.mean((p-a)**2 for p,a in zip(P,A)); base=st.mean(A)
print(f"overall: mean predicted {st.mean(P):.3f}, observed {base:.3f}; Brier {brier:.4f} against {base*(1-base):.4f} for always predicting the average")
