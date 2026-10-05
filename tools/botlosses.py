#!/usr/bin/env python3
"""botlosses.py - how a --trace run was won and lost.

Usage: botlosses.py RUN.jsonl

Winner counts, when and by how much each faction won, score changes by source
per game for US/VC/NVA wins, Coup-round changes, margins at each Victory
check, the US policy decision mix, and the strongest insurgent Events.
"""
import json, collections, statistics as st, sys
recs=[json.loads(l) for l in open(sys.argv[1])]
ok=[r for r in recs if not r.get('error')]
R=('ARVN','NVA','VC')
def lead(r): s=r['final_scores']; return s['US']-max(s[f] for f in R)
groups=collections.defaultdict(list)
for r in ok: groups[r['winner']].append(r)
print(f"{len(ok)} games:", {k: len(v) for k,v in groups.items()})
print("\nwhen and by how much (winner's margin at the deciding check / US margin then)")
for w,gs in groups.items():
    ends=collections.Counter(r['end_coup'] for r in gs)
    wm=[r['final_scores'][w] for r in gs]; um=[r['final_scores']['US'] for r in gs]
    print(f"  {w:<5} n={len(gs):3}  ends {dict(sorted(ends.items()))}  winner margin {st.mean(wm):+.1f}  US margin {st.mean(um):+.1f}  US lead {st.mean(lead(r) for r in gs):+.1f}")
fin=[r for r in ok if r['end_coup']==6 and r['winner']!='US']
print(f"\nlosses at the final Coup: {len(fin)}; US lead there: " + str(sorted(collections.Counter(lead(r) for r in fin).items())[:12]))
# attribution by source, per game, in US wins vs VC wins vs NVA wins
def kind(a):
    if a['a']=='Event': return f"{a['f']} Event"
    if a['a']=='Pass': return f"{a['f']} Pass"
    return f"{a['f']} Op"
def attrib(gs):
    A=collections.defaultdict(collections.Counter); cards=0
    for r in gs:
        for a in r['actions']:
            for c,v in a['d'].items(): A[kind(a)][c]+=v
        for cp in r['coups']:
            for c,v in cp['d'].items(): A['Coup'][c]+=v
    return A
keys=['sup','usav','opp','vcb','coin','pat','nvac','nvab']
for w in ('US','VC','NVA'):
    gs=groups.get(w,[]); A=attrib(gs); n=len(gs)
    print(f"\n== games won by {w} (n={n}); change per game")
    print(f"{'source':<11}"+''.join(f"{k:>7}" for k in keys))
    for g in sorted(A): print(f"{g:<11}"+''.join(f"{A[g][k]/n:+7.1f}" for k in keys))
# per-coup: what the Coup round did (Agitation/Pacify), per coup
print("\nCoup rounds, mean change per Coup: support / opposition / US available")
for w in ('US','VC','NVA'):
    cps=[cp for r in groups.get(w,[]) for cp in r['coups']]
    print(f"  {w:<4} sup {st.mean(cp['d'].get('sup',0) for cp in cps):+.2f}  opp {st.mean(cp['d'].get('opp',0) for cp in cps):+.2f}  usav {st.mean(cp['d'].get('usav',0) for cp in cps):+.2f}")
# rival margins trajectory at victory checks
print("\nmean margins at each Victory check (US / VC / NVA)")
for w in ('US','VC','NVA'):
    row=[]
    for i in range(1,7):
        cs=[cp['victory_check'] for r in groups.get(w,[]) for cp in r['coups'] if cp['coup']==i]
        if cs: row.append(f"C{i}: {st.mean(c['US'] for c in cs):+.0f}/{st.mean(c['VC'] for c in cs):+.0f}/{st.mean(c['NVA'] for c in cs):+.0f}")
    print(f"  {w} wins: "+"  ".join(row))
# US decision mix
print("\nUS decisions (share), US wins vs VC wins vs NVA wins")
mix={}
for w in ('US','VC','NVA'):
    c=collections.Counter()
    for r in groups.get(w,[]):
        for a in r['actions']:
            if a['f']=='US' and 'pol' in a:
                c[a['pol'].split(' -> ')[0].rsplit(' ',2)[0].split(' @')[0]]+=1
    mix[w]=c
allk=collections.Counter(); [allk.update(c) for c in mix.values()]
for k,_ in allk.most_common(10):
    print(f"  {k:<20}"+''.join(f"{100*mix[w][k]/max(1,sum(mix[w].values())):7.1f}%" for w in ('US','VC','NVA')))
# top VC / NVA events by damage to US lead in losses
print("\nInsurgent Events: plays per game and mean change in VC/NVA points per play (all games)")
E=collections.defaultdict(list)
for r in ok:
    for a in r['actions']:
        if a['f'] in ('VC','NVA') and a['a']=='Event':
            d=a['d']; E[(a['f'],a['c'])].append((d.get('opp',0)+d.get('vcb',0)) if a['f']=='VC' else (d.get('nvac',0)+d.get('nvab',0)))
cards={int(k):v for k,v in json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__))), 'cards.json'))).items()}
for (f,c),v in sorted(E.items(), key=lambda kv:-sum(kv[1]))[:10]:
    print(f"  {f:<4}#{c:<4}{cards[c]['title'][:26]:<26} plays/game {len(v)/len(ok):.2f}  pts/play {st.mean(v):+.2f}")
