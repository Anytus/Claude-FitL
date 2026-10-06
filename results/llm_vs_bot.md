# The LLM-played US against the US search bot

Sources: branches `claude/testgame2` to `claude/testgame10` (journals, notes,
saves, `CURRENT_US_STRATEGY.md`, `RULES_LEARNED.md`, post-mortems). The
detailed comparison uses games 7-10, the four played under the condition the
bot experiments use (the US may win only at the final Coup; ARVN Resources
tracked; the Bots treat the US as a player). The bot is the US search policy
with `policies/fit3flat.json`, the best fitted weights so far.

## 1. Record

| | US wins |
|---|---|
| LLM, games 2-10 (any Coup in 2-6, final Coup only in 7-10) | 8 of 9 |
| LLM, games 7-10 (final Coup only) | 3 of 4 (lost game 8 to VC by 2) |
| Search bot, same condition, held-out seeds 1-400 | 17-19% |

At 19%, 3 or more wins in 4 games happens about 2% of the time.

## 2. What the LLM thought it was doing

Its own distilled advice (`CURRENT_US_STRATEGY.md`, carried from game to game),
in short:

- **Score composition.** About 21-23 points sit in Available from the start;
  the rest must be Support on the map. Saigon first (pop 6, Govern cannot
  reach it), then 2-pop spaces. Durable Support (Saigon, spaces without ARVN
  cubes, spaces cleared of Guerrillas) is worth more than points the next
  Terror or Govern takes.
- **Margins, not points.** The Victory check comes first in the Coup; know
  every bot's margin two cards before a Coup can appear and spend an action
  pushing back any bot near its line. A point of your own counts against
  every rival at once.
- **Prepare the Coup Support phase** (COIN Control, US Troops and Police
  below Active Support), paid for by ARVN's fresh income: +6 and +14 in two
  games. Limited Ops with nothing better to do set it up.
- **ARVN Resources above Econ are the Pacify budget**; spend them before the
  ARVN Bot does.
- **Advise every action you can**; it removes Underground Guerrillas and
  undefended Bases for free and breaks Controls.
- **Troops are tools, not shields**: Terror and Agitate need an enemy piece,
  not a Control margin, so remove the Guerrilla rather than garrison.
- **Turn order.** Pass only when the next card's order makes the follow-up
  certain. An Op without a Special Activity closes the Event to those behind;
  on the last card before a Coup, acting to end the card denies a rival its
  turn before the Victory check.
- **Events**: weigh each against an Op + SA; Out-of-Play US pieces to the map
  are free points; deny rivals' shaded sides.

So "maximise the US score" is most of it, but with three additions: protect
what is already scored, push rivals back from their lines (Patronage transfer,
Assault), and use the sequence of play.

## 3. Decision mix

US card decisions; the LLM's from its one-line notes (keyword classification,
169 decisions in games 7-10), the bot's from 198 traced games (5852 actions).

| | LLM | Bot |
|---|---|---|
| Op + Special Activity | 64% | 56% |
| Limited Op | 17% | 12% |
| Pass | 10% | 25% |
| Event | 8% | 7% |
| Op only | 1% | 1% |

Mentions per decision (LLM) against share of actions using it (bot): Train
39% / 40%, Advise 25% / 28%, Assault 17% / 11%, Air Lift 8% / 14%, Air Strike
4% / 14%, Sweep 6% / 10%, Patrol 4% / 7%. The LLM names Pacify in 24% of its
decisions, Saigon in 28% and a Patronage transfer in 9%. The Tru'ng US
transfers Patronage only when Patronage is 17 or more, never to push ARVN off
its line. The bot passes two and a half times as often and Air Strikes three
times as often.

## 4. Branch points: the same position, the LLM's move against the bot's

**Method** (`fitl.Branch`, `tools/botbranch.py`). Six branch points per game
in games 7-10, fixed before any were run: the US decisions at evenly spaced
quantiles of each game's "US is up" saves (`llm_vs_bot/branch_plan.json`).
At each, the saved position before the US action is loaded and the bot makes
its own decision; the save after the LLM's action is the LLM's position. Both
are then played to the end 30 times with all four factions as Bots (the US by
the bot), each pair on the same seed and the same continuation of the event
deck (drawn as the piles allow, given the cards already seen). The score is
the paired difference in final US lead (US margin minus the best rival's),
LLM minus bot. 228 s of wall time for all 24 points.

What this measures: the value of one decision when the bot plays everything
after it. Plans of the LLM's that needed its own follow-up are not carried
out, so this probably understates the LLM.

**Result.** Over 24 points the LLM's decision is worth **+1.8 points of final
US lead** (se 0.6 across points). It is better at 15 points and worse at 8.
At 2 standard errors it is better at 7 and worse at none. The immediate
effect is the same: the US score straight after the decision differs by
+0.05 on average, the US lead by +0.15.

| Point | LLM | Bot | Lead now | Final lead (se) |
|---|---|---|---|---|
| G7 #20 Laser Guided Bombs | Train + Pacify Kien Giang; Advise Hue (2 VC), Quang Tri (2 NVA Troops) | Train (ARVN <= 1) + Advise | +3.0 | **+7.7** (1.8) |
| G8 #31 AAA | Patrol a LoC + Advise Pleiku, Binh Dinh: strip VC from Support spaces | Sweep + Air Strike | -0.5 | **+6.9** (2.4) |
| G9 #9 Psychedelic Cookie | Event: 3 Out-of-Play Troops to Available; deny VC the shaded side | Train + Advise | +1.0 | **+6.3** (2.8) |
| G7 #84 To Quoc | LimOp Train Saigon + transfer 3 Patronage (ARVN 52 to 49) | Pass | +3.0 | **+5.9** (1.5) |
| G9 #74 Lam Son 719 | LimOp Assault Saigon + ARVN follow-up: COIN Control back | Pass | 0.0 | **+4.5** (1.5) |
| G7 #9 Psychedelic Cookie | Event: 3 Out-of-Play Troops; deny NVA the shaded side | Train + Advise | +3.0 | **+4.2** (1.3) |
| G8 #4 Top Gun | Train + Pacify Da Nang 2 levels; Advise Kien Giang, Binh Dinh | Train + Advise | +2.0 | **+2.5** (1.2) |
| G10 #61 Armored Cavalry | Patrol 3 Troops to set up Coup Pacify (Hue, Qui Nhon, Kontum); Advise VC out of two Agitate targets | Train + Advise | -1.0 | +4.4 (2.4) |
| G8 #70 ROKs | Pass, to be first eligible next card | Train LimOp | 0.0 | +4.2 (2.7) |
| ... 11 more between -1 and +2 | | | | |
| G7 #104 Main Force Bns | Air Lift + Assault, 11 NVA Troops | Assault + Air Lift | -1.0 | -2.1 (2.3) |
| G7 #63 Fact Finding | Train + Pacify Kien Giang; Advise | Train + Advise | -2.4 | -3.0 (2.7) |

All 24 rows: `llm_vs_bot/branch_table.txt`.

The seven clear wins fall into four kinds:

1. **Same Operation, different spaces and Pacify** (G7 #20, G8 #4). The bot
   chose Train + Advise too, but the Tru'ng priorities picked where; the LLM
   pacified a chosen space and Advised against the Guerrillas threatening
   Support.
2. **Acting where the bot passes** (G7 #84, G9 #74). A Limited Op in Saigon:
   a Patronage transfer that pushes ARVN back from its line, or an Assault
   that restores Control. The bot's menu has "Train LimOp", but the Tru'ng
   Train in Saigon transfers Patronage only at 17+, so the option the LLM used
   is not on the bot's menu at all.
3. **Events with free points or denial** (G7 #9, G9 #9). Psychedelic Cookie's
   unshaded side puts Out-of-Play Troops into Available (+3 US) and keeps the
   shaded side from a rival. The bot scored the Event below Train + Advise.
4. **A different Operation chosen for protection** (G8 #31): Patrol + Advise
   to remove VC from Support spaces, instead of Sweep + Air Strike.

## 5. What it means

- The LLM does not win by getting more US score out of each action: straight
  after the decision the two are level. Its decisions pay off later, through
  where the points are (durable spaces, cleared of Guerrillas), through rival
  margins (Patronage transfer, Assault) and through events and turn order.
- Most of the difference is in things the bot cannot choose, because the
  Tru'ng routines make those choices: which spaces to Train, Pacify and
  Advise in; whether a Train in Saigon transfers Patronage; what to do in the
  Coup round. That matches the earlier finding that better weights stop
  helping: the menu is the limit.
- +1.8 points of final lead per decision is large. A game has about 30 US
  decisions; the effects do not simply add, but even a fraction of that
  separates a 17% bot from a 75% player.

## 6. What a non-Tru'ng US bot needs, in order

1. **Choose its own spaces.** Train and Pacify targets by population, Support
   level and how durable the Support is (Saigon; no ARVN cubes for Govern to
   reach; no Guerrillas for Terror or Agitate); Advise targets among the
   Guerrillas and undefended Bases that threaten Support or Control.
2. **Patronage transfer as a lever on ARVN's margin**, whenever ARVN is near
   its line, not only at Patronage 17+.
3. **Coup-round decisions**: set up the Support phase's Pacify (COIN Control,
   US Troops, Police) and plan Commitment, instead of the Tru'ng routine.
4. **Sequence of play**: act (a Limited Op or an Op without SA) to end a card
   or to hold the next faction to one space before a Coup; pass only when the
   next card's order guarantees the follow-up. The bot now passes 25% of the
   time against the LLM's 10%.
5. **Events**: score free points (Out-of-Play pieces to Available) and the
   denial of a rival's shaded side.
6. **Rival margins in the score**, with a look-ahead to the next Victory
   check, and spend actions pushing back a rival near its line.

## 7. Caveats

- 24 branch points, 30 runs each; 7 clearly better, none clearly worse. The
  per-point estimates are noisy (se about 2); the overall +1.8 (se 0.6) is
  the reliable number.
- The rollouts play on with the bot as US, so a decision whose value depended
  on the LLM's own follow-up is undervalued, and one that only works with the
  bot's style could be overvalued.
- The LLM's notes are the source for its decision mix (a keyword count over
  one line per card).
- The branch points come from four games the LLM mostly won; the points
  themselves were chosen by position in the game, not by outcome.
