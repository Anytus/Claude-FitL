#!/usr/bin/env python3
"""botfit.py - fit the US search policy's weights to logged decisions.

Usage:
  FITL_POLICY_FIT=/tmp/f/f botrun.py --us-policy P.json --out run.jsonl ...  # writes /tmp/f/f.<pid>
  botfit.py --policy P.json --games run.jsonl --log '/tmp/f/f.*' --out policies/fit_1.json
            [--folds 5] [--lambdas 0.01,0.1,1,10,100,1000]

The search scores a candidate action by a weighted sum of the features of
the board it leaves (plus Pass/Event extras), so the weights are a guess at
how good a board is. This fits that guess to what happened: one row per US
decision (the features of the board the real action left), the target is
that game's outcome (--target): by default its final US lead (final US
margin minus the best rival's) if it reached the final Coup, and below any
full game, by how late it ended, if a Bot crossed its line first.
A game gives one row per US decision instead of one number per game.

The features of the board before the decision ("b" in the log) and the
number of cards seen go in as controls (unless --no-controls). They are the
same for every candidate of a decision, so they change no choice, but they
soak up how good the position already was: the after-board weights are then
fitted only from what the decisions and their dice changed, which is what
the search compares. Without them the fit also learns which positions are
good, and a feature that marks good positions (not good actions) gets weight.
--explored-only fits only the decisions chosen at random (policy "explore").

Ridge regression on standardised features, the intercept unpenalised (only
differences between candidates matter, so the intercept and the overall
scale of the weights do not change any choice). The ridge strength is
chosen by cross-validation with whole games held out together, since the
rows of one game share a target. Features that never vary are left out and
keep weight 0. The output policy is --policy with the fitted weights; the
other settings (focuses, samples, hinge_buffer, ...) are kept and "explore"
is dropped. With --phase each feature x also gets phase weights x@t and x@c,
fitted from x*t and x*c (see the option).
"""
import argparse
import glob
import json
import sys

import numpy as np

RIVALS = ("ARVN", "NVA", "VC")


def lead(r):
    s = r["final_scores"]
    return s["US"] - max(s[f] for f in RIVALS)


def load_rows(patterns, games):
    rows = []
    for pat in patterns:
        for p in sorted(glob.glob(pat)):
            for line in open(p, encoding="utf-8"):
                if line.strip():
                    d = json.loads(line)
                    if d["seed"] in games:
                        rows.append(d)
    return rows


def ridge(X, y, lam, w=None):
    """Ridge on standardised X with an unpenalised intercept. Returns (b0, b)."""
    w = np.ones(len(y)) if w is None else w
    mu = np.average(X, axis=0, weights=w)
    ym = np.average(y, weights=w)
    Xc, yc = X - mu, y - ym
    A = (Xc * w[:, None]).T @ Xc + lam * np.eye(X.shape[1])
    b = np.linalg.solve(A, (Xc * w[:, None]).T @ yc)
    return ym - mu @ b, b


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--policy", required=True, help="the policy the games were played with")
    p.add_argument("--games", required=True, nargs="+", help="botrun.py output(s): final results by seed")
    p.add_argument("--log", required=True, nargs="+", help="FITL_POLICY_FIT files (globs allowed)")
    p.add_argument("--out", help="write the fitted policy here")
    p.add_argument("--name", help="name of the fitted policy (default: from --out)")
    p.add_argument("--folds", type=int, default=5)
    p.add_argument("--no-controls", action="store_true")
    p.add_argument("--explored-only", action="store_true")
    p.add_argument("--phase", action="store_true",
                   help="also fit phase weights x@t and x@c (the weight of x becomes w + t*w@t + c*w@c, "
                        "t = share of the deck seen, c = chance of a Coup in the next 2 cards)")
    p.add_argument("--lambdas", default="0.01,0.1,1,3,10,30,100,300,1000,3000,10000")
    p.add_argument("--target", choices=["lead", "survival"], default="survival",
                   help="lead: final US lead. survival (default): final US lead for games that reach the "
                        "final Coup; a game that ends early (a Bot crossed its line) scores below every "
                        "full game, by how late it ended (see --floor, --step)")
    p.add_argument("--floor", type=float, default=-25.0,
                   help="survival: full games score their final lead but no less than this; a loss at the "
                        "5th Coup scores floor - step, at the 1st floor - 5 * step (default -25)")
    p.add_argument("--step", type=float, default=5.0, help="survival: points per Coup not reached")
    args = p.parse_args()

    pol = json.load(open(args.policy))
    games = {}
    for g in args.games:
        for line in open(g, encoding="utf-8"):
            r = json.loads(line)
            if not r.get("error"):
                games[r["seed"]] = r
    floor = args.floor

    def target(r):
        if args.target == "lead":
            return lead(r)
        if r["end_coup"] == 6:
            return max(lead(r), floor)
        return floor - args.step * (6 - r["end_coup"])

    n_early = sum(r["end_coup"] != 6 for r in games.values())
    games = {s: target(r) for s, r in games.items()}
    if args.target == "survival":
        print(f"target: survival; {n_early} of {len(games)} games ended early, scored "
              f"{floor - args.step:.0f} (5th Coup) down to {floor - 5 * args.step:.0f} (1st Coup)")
    rows = load_rows(args.log, games)
    if args.explored_only:
        rows = [d for d in rows if d.get("explored")]
    if not rows:
        sys.exit("no logged decisions from completed games")
    base_keys = sorted({k.split("@")[0] for k in pol["weights"]})
    if args.phase:
        if not all("t" in d and "c" in d for d in rows):
            sys.exit("the log has no phase (t, c); --phase needs a newer log")
        keys_all = base_keys + [k + "@t" for k in base_keys] + [k + "@c" for k in base_keys]
        mult = lambda d, k: d["t"] if k.endswith("@t") else d["c"] if k.endswith("@c") else 1.0
    else:
        keys_all, mult = base_keys, (lambda d, k: 1.0)
    F = np.array([[d["f"].get(k.split("@")[0], 0.0) * mult(d, k) for k in keys_all] for d in rows])
    sd_all = F.std(axis=0)
    keys = [k for k, s in zip(keys_all, sd_all) if s > 1e-9]
    dropped = [k for k, s in zip(keys_all, sd_all) if s <= 1e-9]
    X = F[:, [keys_all.index(k) for k in keys]]
    mu, sd = X.mean(axis=0), X.std(axis=0)
    Z = (X - mu) / sd
    nc = 0
    if not args.no_controls:
        if not all("b" in d for d in rows):
            sys.exit("the log has no before-decision features (b); use --no-controls")
        C = np.array([[d["b"].get(k, 0.0) for k in base_keys] + [d["seen"], d["seen"] ** 2]
                      + ([d["t"], d["c"]] if args.phase else []) for d in rows], dtype=float)
        C = C[:, C.std(axis=0) > 1e-9]
        Z = np.hstack([Z, (C - C.mean(axis=0)) / C.std(axis=0)])
        nc = C.shape[1]
    y = np.array([games[d["seed"]] for d in rows], dtype=float)
    seeds = np.array([d["seed"] for d in rows])
    useeds = np.unique(seeds)
    n_expl = sum(d.get("explored", False) for d in rows)
    print(f"{len(useeds)} games, {len(rows)} US decisions ({len(rows) / len(useeds):.1f} a game, "
          f"{n_expl} explored); {len(keys)} features vary"
          + (f"; never vary, kept at 0: {', '.join(dropped)}" if dropped else "")
          + (f"; {nc} controls" if nc else "; no controls"))
    print(f"target: mean {y.mean():+.2f} per decision, sd {np.std([games[s] for s in useeds]):.2f} per game")

    # Cross-validation by game.
    rng = np.random.default_rng(0)
    fold_of = dict(zip(useeds, rng.permutation(len(useeds)) % args.folds))
    folds = np.array([fold_of[s] for s in seeds])
    lams = [float(x) for x in args.lambdas.split(",")]
    print(f"\n{'lambda':>8} {'CV R2':>7} {'CV MSE':>8}")
    cv = []
    for lam in lams:
        err = np.zeros(len(y))
        for k in range(args.folds):
            tr, te = folds != k, folds == k
            b0, b = ridge(Z[tr], y[tr], lam)
            err[te] = y[te] - (b0 + Z[te] @ b)
        mse = float(np.mean(err ** 2))
        cv.append(mse)
        print(f"{lam:8g} {1 - mse / np.var(y):7.3f} {mse:8.2f}")
    lam = lams[int(np.argmin(cv))]
    b0, b = ridge(Z, y, lam)
    r2 = 1 - np.mean((y - b0 - Z @ b) ** 2) / np.var(y)
    b = b[:len(keys)]          # the after-board weights; the controls are dropped
    raw = b / sd
    print(f"\nchosen lambda {lam:g}: in-sample R2 {r2:.3f}, CV R2 {1 - min(cv) / np.var(y):.3f}")

    old = np.array([pol["weights"].get(k, 0.0) for k in keys])
    # The old weights in the fitted scale, for comparison (choices depend only on direction).
    scale = float(old @ raw / (old @ old)) if old @ old > 0 else 0.0
    print(f"\n{'feature':<24}{'sd':>8}{'std coef':>10}{'fitted':>10}{'old':>10}{'old*k':>10}")
    for i in np.argsort(-np.abs(b)):
        print(f"{keys[i]:<24}{sd[i]:8.2f}{b[i]:10.3f}{raw[i]:10.4f}{old[i]:10.4f}{scale * old[i]:10.4f}")
    cos = float(old * sd @ b / (np.linalg.norm(old * sd) * np.linalg.norm(b) + 1e-12))
    print(f"\nold weights scaled by k = {scale:.3f} (least squares onto the fit); "
          f"cosine between old and fitted (standardised): {cos:.2f}")

    if args.out:
        new = json.loads(json.dumps(pol))
        new.pop("explore", None)
        new["name"] = args.name or args.out.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        new["weights"] = {k: 0.0 for k in keys_all}
        for k, v in zip(keys, raw):
            new["weights"][k] = round(float(v), 5)
        json.dump(new, open(args.out, "w"), indent=2)
        print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
