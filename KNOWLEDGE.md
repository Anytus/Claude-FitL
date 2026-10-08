# What we know about playing the US against the Tru'ng bots

One place for established facts, each with its evidence. Conditions unless
stated: Full scenario, the US may win only at the final Coup
(`--us-final-only`), the Bots treat the US as a player (`--us-player`:
ARVN Resources tracked, the VC Bot's priorities against a human US).
"Search bot" = `fitl.USPolicy` search with `policies/fit3flat.json`; from
the Event/Pass test on, the working baseline is `policies/fit3flat_event0.json`
(Kevin's decision; the evidence for it is a probable small gain, below).
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

## Rule changes for a paying US (under `--us-player`)

The Tru'ng US routines stand in for untracked ARVN Resources in three
places; with Resources tracked, each would be a double handicap, so the
harness removes it: the ARVN activation rolls on Train, the d3 cap on
Pacify, and (since `results/aid_test.txt`) Advise's +6 Aid being taken only
when ARVN is human. Results measured before a change say so.

## The bars

| US player | US wins | Games reaching the final Coup | Evidence |
|---|---|---|---|
| Tru'ng US routines | about 4% | | `results/val_t1.txt` |
| Search bot | 19% (397 games) | 62% | `results/diagnostics/q1_losses.txt` |
| Search bot, with +6 Aid on Advise | 39% (393 games) | 71% | `results/aid_test.txt` |
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

## Where the LLM's extra Support came from (`results/diagnostics/q5_support.txt`)

- Support per full game, LLM (4) against search bot (246): Coup rounds
  +30.0 against +21.5 (5.0 against 3.6 a Coup); US Operations +26.5 against
  +20.6 (33 actions and 4 Passes a game against about 25 and 7); VC Events
  -23.0 against -18.3; ARVN Govern -13.2 against -8.7. Net about +18
  against +8.
- Going into a Coup both have about 3 eligible Pacify spaces worth about 6
  Support, but ARVN Resources above Econ are 19.0 for the LLM against 6.6
  for the bot.
- The difference is ARVN income, not spending: US and ARVN spend about the
  same; Coup rounds add +109 ARVN Resources a game for the LLM against +72.
  ARVN income is Econ + US Aid, and US Aid at the checks rises to 40-57 in
  the LLM games while it sinks from 18 to 7 in the bot's.
- Cause: the US Tru'ng Advise routine adds the free +6 Aid only when ARVN
  is human (`Bot.US_Bot.adviseActivity`). Under `--us-player` ARVN
  Resources are tracked, so the bot gives up +6 Aid on every Advise, which
  a human US (and the LLM) takes. Same kind of stand-in as the activation
  rolls and the d3 Pacify cap.

## Advise's +6 Aid (`results/aid_test.txt`)

- Letting the US Bot take +6 Aid on Advise when ARVN Resources are tracked
  doubles its wins: 19.1% -> 39.2% (paired +20.1, se 2.8) on seeds 1-400;
  games reaching the final Coup +8.9 (se 2.9); VC wins 56% -> 37%.
- Mechanism as predicted in part: Aid at the checks rises to 52-59 (the LLM
  games: 40-57), ARVN Resources to 33-43, Support to about 29-30 (from
  24-25), the US score at the final check to -1.5 (from -7.5). Not as
  predicted: the Coup rounds' Support gain is unchanged; the extra Support
  comes from Pacify on the US's own turns. ARVN wins rise slightly (early
  ARVN wins 6 -> 11).
- All earlier results for the search bot (weights, look-ahead, the US
  player, the Commitment test) were measured without this change.

## After the +6 Aid change (`results/diagnostics/round2/`, `tools/botdiag.py`)

- Losses: 116 of 396 games end early (VC 81, NVA 24, ARVN 11); 124 are
  lost at the final Coup (NVA 48, VC 63, ARVN 13), mostly not close: the
  winner leads the US by 6.2 (NVA) and 9.3 (VC); 38 of 124 within 3 points.
- VC crossings work as before: VC starts the campaign 1 point below its
  line (Coup Agitation +4.3), then VC Events +4.1, Tet +1.5, VC Operations
  +1.2; US Operations -2.4.
- Support per full game against the LLM: US Operations +30.6 (LLM +26.5),
  Coup rounds +19.9 (LLM +30.0), VC Events and Tet -20 (LLM -23), ARVN
  Govern and Events -12.9 (LLM -13.4). Support at the final check 28.6
  (LLM about 33); US score at the final check -1.5 (LLM +1.2). Coup Pacify
  is no longer short of Resources; it runs out of eligible spaces (5.9 at
  Coup 2, 0.7 at the final Coup): spaces already at Active Support, and the
  final campaign's withdrawal leaves fewer with US Troops.
- Final-Coup games the US loses have about 10 less Support at the end than
  those it wins (23.2 against 32.9), spread over US Operations (+4.9 in
  wins), ARVN Govern (+2.5) and VC Operations (+1.6): correlation only.
- US Passes: 20% of US actions (LLM about 11%).
- The LLM's 3 of 4 is no longer clearly better than 39% on its own (3+ of 4
  at 39% happens 17% of the time), but its decisions still beat the bot's
  at the 24 branch points: +1.7 final lead each (se 0.7), as before the
  change (+1.8). The largest: Psychedelic Cookie's Event (+10.1, +5.6), Train
  and Pacify in a chosen space against Train + Advise (+8.6, +4.2), a
  Limited Op with Patronage transfer against a Pass (+7.1), a Pass to be
  first on the next card (+5.0).

## The Event and Pass bonuses (`results/event_pass_test.txt`)

- fit3flat (fitted by regression before the +6 Aid change) gives an Event
  -0.71 and a Pass +0.23, against +0.40 for a point of US score.
- Event bonus 0 (`policies/fit3flat_event0.json`): the bot takes Events
  twice as often (6% -> 12% of US actions); wins +5.4 (se 2.6) on seeds
  1-400, +2.0 (se 3.0) on 401-800, pooled +3.7 (se 2.0). Probably a small
  gain; not established.
- Pass bonus 0: passes 20% -> 9% (Limited Ops 13% -> 22%), wins +1.3
  (se 2.9); with both at 0, +1.8 (se 2.8), less than the Event change
  alone. No sign that passing less helps.

## How much the weights are known

- Evidence supports weight *packages*, not individual weights. Packages
  that differ widely (tune-start, tuned_t1/t2, fit3flat, fit3phase) win
  within a few points of each other; the large gains came from the search
  structure (Tru'ng US 4% -> tuned_t1 39%, old rules) and rule fixes (+6 Aid,
  +20). The regression's coefficients are associations from games played
  by one policy, fitted to a proxy target (survival-floored lead, CV R2
  0.27, most of it the controls), under the old Aid rule; the Event
  coefficient's sign was not borne out by a direct test.

## Playout labels of single decisions (`results/teacher/`)

- Playing each candidate to the end of the game (the search bot playing on)
  costs about 0.24 s a playout on one core. Two playouts from different
  candidates on the same seed are barely alike (correlation of wins 0.19
  even with the dice reset at every step), so one decision's difference at
  200 playouts per candidate has se about 4 points of win chance; ranking a
  close call to se 2 needs about 750 per candidate.
- In 52 decisions with the Event on offer (pilot), most candidates are
  within a few points of each other; 7 of 52 decisions have candidates
  more than 20 points apart. The policy's score correlates 0.22 with the
  playouts' differences; its first choice beats its second by about 2-4
  points on average.
- Where Event weight 0 and fit3flat disagree (32), the Event is no better on
  a typical decision (median +0.2, mean without the largest -1.3, se 1.4);
  one decision, Americal in the final campaign, is +92.5 for the Event.
  So the pilot neither confirms nor refutes the Event result by itself.

## Screening all US decisions (`results/teacher/screen_results.txt`, corrected by `reanalysis.txt`)

- 343 sampled US decisions, each with the bot's pick and the best-scoring
  candidate of up to 3 other kinds, played to the end 100 times each.
- Which kind of action matters: the true spread of the alternatives
  against the bot's pick is about 4-6 points of win chance (sd; split-half
  estimate), the average alternative 2.2 points worse than the pick. A
  perfect chooser among those few alternatives would gain about 2-4 points
  a decision. (The screen's own measure, held-out regret +0.2, is what a
  chooser with 50 noisy playouts gains; it was first misread as "nothing to
  gain".)
- The policy's score predicts which candidate is better only weakly
  (correlation 0.16), and 100 playouts leave about 5 points of noise per
  comparison: the bot cannot tell which alternative is better.
- Coup! Failed Attempt on deck: its ARVN Desertion is resolved before the
  Victory phase. In one game the bot's pick then put NVA over its line (lost
  every playout; alternatives won 34-46%). The bot's features do not see the
  Coup card's own effect (1 game in 122).

## Space choice (`results/teacher/space_results.txt`, corrected by `reanalysis.txt`)

- One space pick of a US action changed to another space that pick was
  offered: typical changes are truly near-equal (true sd 0.3 points without
  the extreme 1%), a random change costs 0.8 (se 0.2), and the spread is in
  a few decisive positions (2 found in about 730 labelled decisions: the
  last US action before a Victory check, where the chosen action leaves a
  rival over its line and an alternative the search did not compare would
  not).
- Coup Support-phase Pacify: where the US Pacifies matters broadly, about 3
  points (sd) per alternative; the Tru'ng ordering is no better than a random
  eligible space (+0.5, se 0.5); a perfect choice among 2-3 random
  alternatives would gain about 2.5-3 points a Coup.
- Long runs survive only while this session is active: the container was
  reclaimed twice within minutes of the session going idle, taking the
  background jobs with it.

## What US actions accomplish, open spaces, turn economy (`results/breadth/results.txt`)

- Per Op+SA the LLM (4 games) did not accomplish more than the bot: about
  the same enemy removed (3.3 against 3.1), COIN Control (0.6 against 0.7),
  Support (+1.4 against +1.25) and rival pushed back (-1.0 against -0.9), in
  fewer spaces (3.1 against 4.2; the bot places many more ARVN cubes). Per
  game the bot's own actions do more (21 Op+SA against 15; Support +35
  against +26).
- Spaces open to US Operations: the bot has as many early; late in the game
  the LLM had about twice as many for Sweep and Coup Pacify (the bot takes US
  pieces off the map in the final campaign).
- Turn economy: the LLM passed far more often when a pass left it first
  eligible on the next card (31% against 3% with full options, 80% against 0%
  after an Op); the bot's pass rate does not depend on it at all (it has no
  notion of next-card eligibility).

## Open questions

- With +6 Aid in, which gaps to the LLM remain (Support, Passes, VC Events,
  Govern)? The diagnostics should be rerun on the new baseline.
- Can the US deny VC its Events, Tet and Coup Agitation (the measured
  causes of VC crossings) more than the search bot does, and at what cost
  in score?
- Would look-ahead with the search bot in the playouts (calibrated) and
  enough playouts help, and at what cost?
