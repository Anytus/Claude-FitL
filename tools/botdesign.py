#!/usr/bin/env python3
"""botdesign.py - how the US search policy's features rank candidate moves.

Usage:
  FITL_POLICY_DESIGN=/tmp/d/d botrun.py ... --us-policy P.json   # writes /tmp/d/d.<pid>
  botdesign.py P.json /tmp/d/d.*

The policy only compares candidates within one decision, so the design
matrix that matters is each candidate's features minus the mean over that
decision's candidates. From it this prints, per feature:
  varies   share of decisions in which the feature differs between candidates
  sd       pooled within-decision standard deviation
  w*sd     typical size of its push on the ranking (|weight| * sd)
  VIF      variance inflation factor (how well the other features predict it)
  flips    share of decisions whose choice changes if this weight alone is 0
and the feature pairs whose within-decision correlation is |r| >= 0.5, the
eigenvalues of the correlation matrix, and choice flips for feature groups.
"""
import json
import sys

import numpy as np


def load(paths):
    decs = []
    for p in paths:
        for line in open(p, encoding="utf-8"):
            if line.strip():
                decs.append(json.loads(line))
    return decs


def main(policy_path, paths):
    pol = json.load(open(policy_path))
    w = pol["weights"]
    decs = [d for d in load(paths) if len(d["cands"]) >= 2]
    keys = sorted({k for d in decs for c in d["cands"] for k in c["f"]})
    W = np.array([w.get(k, 0.0) for k in keys])

    blocks, flips_base = [], []
    recon = 0.0
    for d in decs:
        F = np.array([[c["f"].get(k, 0.0) for k in keys] for c in d["cands"]])
        v = np.array([c["v"] for c in d["cands"]])
        recon = max(recon, float(np.max(np.abs(F @ W - v))))
        blocks.append((F, v))
    print(f"{len(decs)} decisions, {sum(len(b[0]) for b in blocks)} candidates, {len(keys)} features; "
          f"max |value - weights.features| = {recon:.3f}")

    Xc = np.vstack([F - F.mean(axis=0) for F, _ in blocks])
    sd = Xc.std(axis=0)
    varies = np.array([np.mean([np.ptp(F[:, j]) > 1e-9 for F, _ in blocks]) for j in range(len(keys))])

    def flip_rate(cols):
        n = 0
        for F, _ in blocks:
            s = F @ W
            s2 = s - F[:, cols] @ W[cols]
            n += int(np.argmax(s) != np.argmax(s2))
        return n / len(blocks)

    live = [j for j in range(len(keys)) if sd[j] > 1e-9]
    R = np.corrcoef(Xc[:, live], rowvar=False)
    try:
        vif_live = np.diag(np.linalg.inv(R))
    except np.linalg.LinAlgError:
        vif_live = np.diag(np.linalg.pinv(R))
    vif = {live[i]: vif_live[i] for i in range(len(live))}

    print(f"\n{'feature':<24}{'weight':>8}{'varies':>8}{'sd':>8}{'w*sd':>8}{'VIF':>8}{'flips':>8}")
    order = sorted(range(len(keys)), key=lambda j: -abs(W[j]) * sd[j])
    for j in order:
        v = f"{vif[j]:8.1f}" if j in vif else f"{'-':>8}"
        print(f"{keys[j]:<24}{W[j]:8.3f}{100 * varies[j]:7.0f}%{sd[j]:8.2f}{abs(W[j]) * sd[j]:8.2f}{v}"
              f"{100 * flip_rate([j]):7.1f}%")

    print("\nwithin-decision correlations |r| >= 0.5")
    pairs = []
    for a in range(len(live)):
        for b in range(a + 1, len(live)):
            if abs(R[a, b]) >= 0.5:
                pairs.append((abs(R[a, b]), keys[live[a]], keys[live[b]], R[a, b]))
    for _, ka, kb, r in sorted(pairs, reverse=True):
        print(f"  {ka:<24}{kb:<24}{r:+.2f}")

    ev = np.sort(np.linalg.eigvalsh(R))[::-1]
    print(f"\neigenvalues of the correlation matrix ({len(live)} varying features):")
    print("  " + " ".join(f"{e:.2f}" for e in ev))
    print(f"  condition number {ev[0] / max(ev[-1], 1e-12):.0f}")

    groups = {
        "pivotal (tet_*, easter_*)": ["tet_live", "tet_near", "easter_live", "easter_near"],
        "VC pieces (vc_guerrillas, vc_underground, tet_near)": ["vc_guerrillas", "vc_underground", "tet_near"],
        "rival threat (max_rival, rival_hinge*)": ["max_rival", "rival_hinge", "rival_hinge_coup_next", "rival_hinge_coup_soon"],
        "margins (us, arvn, nva, vc)": ["us", "arvn", "nva", "vc"],
        "agitate_exposure + vc": ["agitate_exposure", "vc"],
    }
    print("\nchoice flips when a whole group's weights are 0")
    for name, g in groups.items():
        cols = [keys.index(k) for k in g if k in keys]
        print(f"  {name:<52}{100 * flip_rate(cols):6.1f}%")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
