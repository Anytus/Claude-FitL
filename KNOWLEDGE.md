# What we know about playing the US against the Tru'ng bots

One place for established facts, each with its evidence. Conditions unless
stated: Full scenario, the US may win only at the final Coup
(`--us-final-only`), the Bots treat the US as a player (`--us-player`:
ARVN Resources tracked, the VC Bot's priorities against a human US).
"Search bot" = `fitl.USPolicy` search with `policies/fit3flat.json`.
Update this file when a fact is established or overturned; keep claims
to what the cited results show.

## Measuring

- **200 games give a standard error of about 3 points on a win rate near
  20%.** A change smaller than about 6-7 points of wins cannot be seen in a
  200-game paired comparison. Size tests to the effect expected.
- **Win rate is the measure.** Final US lead misled us: a player that
  scores well but lets a Bot cross early has a fair lead and few wins
  (`results/us_player_v1.txt`). `tools/botcompare.py` reports paired changes
  in wins and in games reaching the final Coup.
- Same seed = same game (identical-games check on every program change).
  `--salt K` keeps a seed's event deck and changes the dice and the Bots'
  draws.

## The bars

| US player | US wins | Games reaching the final Coup | Evidence |
|---|---|---|---|
| Tru'ng US routines | about 4% | | `results/val_t1.txt` |
| Search bot | 19% (397 games) | 62% | `results/diagnostics/q1_losses.txt` |
| LLM (games 7-10) | 3 of 4 | 4 of 4 | `results/llm_vs_bot.md` |

Things that did not beat the search bot: weight tuning beyond tuned_t1/t2
(hill-climb and regression); 3 dice samples per trial; phase-dependent
weights; the US played through the human-player interface with fitted
weights (`results/us_player_v1.txt`); look-ahead playouts to the next Coup
with the Tru'ng US in the playouts (`results/lookahead_v1.txt`).

## How the search bot loses (`results/diagnostics/q1_losses.txt`)

- Of 397 games: 151 end early when a Bot crosses its line (VC 113, NVA 32,
  ARVN 6), mostly at Coups 4 and 5; 170 reach the final Coup and are lost to
  a Bot with a better margin (US about -10, the winner about 0).
- **VC crossings are not made by VC's Operations.** In campaigns that end
  with VC over its line, VC starts only 1 point below it (the previous
  Coup round's Agitation added +4.4, against +2.0 when VC stays under) and
  gains +4.6 from its shaded Events and +2.5 from Tet; its Operations add
  +1.0. US Operations take about 2.5 off VC in every campaign, crossing or
  not.
- NVA crossings are made by NVA Operations (+12.6 in the campaign, against
  +5.3 when NVA stays under).
- The US score: the Tru'ng Commitment in the first Coup round moves about
  11 US Troops from Available onto the map (-11 points; Support +8 in the
  same round). VC Events take 4-5 Support a campaign; US Operations add 3-4.

## What the LLM did differently (`results/diagnostics/q2_llm_vs_bot_checks.txt`)

- It did **not** keep the Bots further from their lines: the best rival was
  within 2 of its line at 42% of its Victory checks, against 27% for the
  search bot.
- Its own score was far higher: US -5.8 at Coup 2 (bot -16.7), -2.2 at
  Coup 4 (bot -15.0), +1.2 at the final check (bot -7.5).
- It kept US Troops in Available (20-28 after Coup 1 in games 8-10) while
  Support grew, and held each threat down just enough. Its decisions were
  worth +1.8 final lead each against the bot's in the same positions, with
  the same immediate score (`results/llm_vs_bot.md`).

## Playouts (`results/diagnostics/q3_calibration.txt`)

- Playout estimates of the risk that a Bot is over its line at the next
  Victory check are informative (Brier score a third below always guessing
  the average) and correctly ordered.
- With the Tru'ng US playing the US in the playouts they are about twice
  too pessimistic in the middle range (predicted 23% -> 8% observed,
  38% -> 17%). With the search bot playing the US in the playouts they are
  calibrated (8.7% predicted, 7.9% observed; Brier 0.038 against 0.051),
  at about 45 ms a playout against 10 ms.
- One playout's value has an sd of about 35 on a survival-first scale, so
  a few dozen playouts cannot rank candidates whose risk differs by a few
  percent.

## How much is controllable (`results/diagnostics/q4_controllability.txt`)

- With only luck varying (8 runs of each of 60 seeds), the search bot wins
  36 of 60 deals at least once and 24 never. The deal explains about 19% of
  the outcome variance; the rest is luck and how play unfolds.
- US decisions add up: a random choice on 30% of decisions (about 9 a
  game) halves the win rate (19% -> 10%), about one point of win rate per
  bad decision. Single decisions are small; there are about 30 a game.

## The first-Coup Commitment (`results/commitment_test.txt`)

- Keeping US Troops in Available at Commitment (FITL_COMMIT=hold or 20)
  raises the US score by about 10 at the Coup 2-5 checks, as predicted,
  but only by about 2.3 at the final check: the unchanged bot pulls Troops
  back in the final campaign anyway (Nixon policy, Available 20 at the final
  check). Under the final-Coup-only rule the mid-game score does not count.
- Wins: +2.6 (se 2.6) and +1.0 (se 2.5), not detectable; early ends up
  (151 -> 167 and 171, mostly VC), final-Coup losses down (170 -> 138, 143).
- So the Commitment is not where the bot loses its games. The gap to the
  LLM that counts is Support at the end: about 22 for the bot at the final
  check against 30-38 in the LLM games 7, 9 and 10.

## Open questions

- Why the bot's Support stalls at 22-25 from Coup 3 on (Coup-round
  Pacify gains fade from +8 to about 0; VC Events take 4-5 a campaign)
  while the LLM's reached 30-38?
- Can the US deny VC its Events, Tet and Coup Agitation (the measured
  causes of VC crossings) more than the search bot does, and at what cost
  in score?
- Would look-ahead with the search bot in the playouts (calibrated) and
  enough playouts help, and at what cost?
