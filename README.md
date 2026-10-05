# Claude plays Fire in the Lake

A harness in which a Claude Code session plays *Fire in the Lake* (GMT, 2nd
edition) as the **US** faction against the three Tru'ng bots implemented by
Curt Sellmer's `fitl` program, while a human observer sets the pace, keeps a
physical board in sync, and audits the model's reasoning. Event cards are
drawn by the harness at the moment the program asks for them.

The design document this implements lives in the project owner's notes; the
short version:

- The **program is the single source of truth** for game state. The model
  never tracks the board in its head; it reads a rendered view of the saves.
- The model **writes a full turn plan** (with rationale) into `journal.md`
  before it sends the first answer to the program.
- The model reports **every state change** (a mechanical diff plus the
  program's own log lines) so the observer can update the physical board.
- **No rules reference** is supplied. The program's validation is the only
  backstop; legal-but-wrong moves are the interesting data.

## Layout

| Path | What |
| --- | --- |
| `CLAUDE.md` | Standing instructions for the *playing* session. Read it first. |
| `fitl/lib/` | `fitl` v1.53 jars (MIT, github.com/sellmerfud/fitl) with one patch applied, see below. No build step to run. |
| `fitl/fitl-1.53-harness.patch` | The patch applied to the program (against v1.53): save after every action and Coup round *before* asking for the next card, make the card draw its own saved step, close the adjacency table under symmetry, and add the headless `fitl.Autoplay` entry point. `save-before-draw.patch` is the first half, kept for reference. |
| `tools/botrun.py` | Plays many seeded all-Bot games headless and in parallel through `fitl.Autoplay`, one JSON line per game, and summarises them. See "All-Bot games" below. |
| `tools/botattrib.py` | For a `botrun.py --trace` run: each score component's change per game, by the faction and kind of action that made it, and by Coup rounds. |
| `tools/botcompare.py` | Compares two `botrun.py` runs on their shared seeds: winner shares, mean margins, and the paired change in the US margin with its standard error. |
| `tools/bottune.py` | Tunes a search policy's weights with an evolution strategy against the Bots; resumable. See "Tuning" below. |
| `policies/` | US policy files for `botrun.py --us-policy` (see "US policy" below). |
| `results/` | All-Bot run results: one JSONL file per run, and the printed summary beside it. |
| `tools/ctl.py` | Controller: holds the program in a persistent tmux session. `start`, `new-game`, `resume`, `send`, `seq`, `enter`, `advance`, `brief`, `commit-turn`, `read`, `screen`, `status`. `advance` also draws event cards, writes the report file at each draw and prints the briefing at the US turn; `seq` answers a whole action's prompts in one guarded call, by label or name whichever form the prompt takes; `commit-turn` does the end-of-card bookkeeping (notes line, report, commit, push). |
| `tools/deck.py` | Lazy event-card draws: uniform over what can legally be next in the current pile, decided at request time with the OS random source. `selftest` simulates thousands of decks. |
| `tools/apply_periods.py` | Records each card's period marking (1964/1965/1968) in `cards.json`. |
| `tools/render.py` | Renders the latest save as the board view, with derived scores. Brief by default; `--full` adds every LoC and the adjacency table. |
| `tools/brief.py` | The decision briefing: the board view, this card's narration so far, and the neighbours of every space with US pieces. One call replaces render, transcript greps, card lookups and map queries. |
| `tools/diff.py` | Mechanical delta between two saves (`--log` adds the program's lines). |
| `tools/report.py` | Writes the observer's report for every save since the last one: the program's narration verbatim plus the board summary, under `reports/<game>/`. |
| `tools/fitl_state.py` | Shared save-loading, piece manifest, regions, scoring. |
| `tools/build_cards.py` | Build-time only. Produced `cards.json` from the program's source. |
| `cards.json` | All 130 cards: text, faction order, Tru'ng markings, pivotal conditions, period marking. |
| `map.json` | The static board: every space's type, population or econ, coastal flag, and neighbours. Built once from the program's adjacency table. |
| `tools/map.py` | Adjacency queries: one space's neighbours, whether two spaces touch, the whole map. |
| `tools/build_map.py` | Build-time only. Produced `map.json` from the program's source and reports one-way entries. |
| `games/<name>/` | The program's own saves (`save-NNN`, `log-NNN`). Committed after every US action. |
| `reports/<game>/` | One file per report: the program's narration for every save since the last report, plus the board summary. Written by `report.py`; what the observer updates the board from. |
| `PROMPTS.md` | The program's prompt chains for every US Op, Special Activity and Coup decision, from its own transcripts, with each prompt's form (menu / typed / varies). What the model writes `seq` calls from. |
| `journal.md` | Full turn plans, rationales, rejections. The audit artifact. |
| `BUG_REPORTS.md` | Program bugs found while playing, each written up as a ready-to-post upstream issue with its status. Presented upstream in batches. |
| `notes.md` | One line per model turn. Cross-session memory. |
| `transcript.log` | Everything the program printed, via tmux pipe-pane. |

## Running

Requirements: Java 11+, Python 3, tmux. From the repository root:

```
python3 tools/ctl.py new-game TestGame1     # first time
python3 tools/ctl.py resume TestGame1       # after a container/session loss
python3 tools/ctl.py status
python3 tools/ctl.py advance                # bots, card draws, report, briefing
python3 tools/ctl.py brief                  # the briefing on demand
python3 tools/ctl.py commit-turn "<line>"   # notes line, report, commit, push
python3 tools/render.py                     # board view of the latest save
python3 tools/diff.py                       # last two saves + program log
```

The program runs with the repository root as its working directory, so saves
land in `games/<name>/`.

## Token cost

The playing session's cost is dominated by cache reads, which scale with
the number of tool calls times the length of the conversation, so the cost
of a game grows faster than linearly with its length. Measured on TestGame3
(37 cards): 186 million cache-read tokens against 0.67 million output
tokens, with the context reaching 581 thousand tokens.

What the harness does about it: `report.py` writes the observer's report
from the program's own logs so the model never retypes narration; `diff.py`
no longer repeats the log lines; `render.py` is brief by default; and
`ctl.py seq` answers a whole action's prompts in one guarded call instead of
one call per menu. After TestGame4 (about 190 calls over 27 cards, 7 per
card) three more folds: `advance` writes the report at each card draw and
prints the briefing at the US turn, `brief` replaces the render, transcript
grep, card lookup and map calls with one, and `commit-turn` replaces the
notes, commit and push calls with one. The floor is now about four calls
per card (advance, journal entry, action, commit-turn), roughly half of
TestGame4; the reasoning tokens per card do not shrink with the call count.

TestGame4 also showed `seq` being used one prompt per call (87 calls, 7 of
them with more than one step) because the model could not predict whether
the next prompt would be a numbered menu or a bare typed prompt, and a
rejected answer left it unable to resolve labels. `seq` now matches an
answer against the menu when there is one and types it otherwise, keeps the
last menu for the re-prompt after a rejection, accepts `*` as "any menu"
for steps guarded by their label alone, and `PROMPTS.md` gives the model
the chains from the program's own transcripts.

Every tool call is logged by a `PostToolUse` hook (`.claude/settings.json`
runs `tools/usage_hook.py`) to `~/.fitl-usage.log`, outside the working
tree, one line per call with the input and output size. `report.py` copies
it to `reports/<game>/usage.log` each time it runs, so it is committed with
the game without ever making the tree dirty on its own (a commit is itself a
tool call, which is why the log cannot live in the tree). `python3
tools/usage_report.py` summarises it by kind of call.

What the operator should do about it: **start a fresh session at every
Coup round.** The game, journal and notes live in the repo, so nothing is
lost, and a session that never grows past one campaign keeps the context,
and therefore every subsequent call, several times cheaper.

## The map

State alone does not tell a player what is next to what. `render.py` ends
with an adjacency section and `tools/map.py` answers single questions. The
data is the program's own adjacency table, which is what it uses to decide
legal moves, closed under symmetry.

The release table listed three junction adjacencies in one direction only:
`LOC Cam Ranh -- Da Lat` to Quang Duc-Long Khanh (via Da Lat), `LOC Da Nang
-- Dak To` to `LOC Kontum -- Dak To` (via Dak To), and `LOC Saigon -- An Loc
-- Ban Me Thuot` to Khanh Hoa (via Ban Me Thuot). Rules 1.3.6 makes "LoCs or
Provinces separated by Towns" adjacent, and its own example is the Da Lat
case, so those are adjacencies with the mirror entry missing. The effect in
the release program was that pieces could move from each road into the space
but not from the space onto the road. The harness build of the program
closes the table under symmetry (see the patch), and `map.json` matches it.

## The event deck

The program asks a human to type each card number. Here `ctl.py advance`
answers those prompts itself by calling `tools/deck.py`. There is no
shuffled deck stored anywhere. For each request the generator takes the
cards drawn so far (from the program's latest save), works out which pile
the next card comes from, and picks uniformly at random, using the OS
cryptographic random source, among the cards that can legally be next:

- Full 1964–1972 scenario: six piles of 13, stacked 1964, 1965, 1965,
  1968, 1968, 1968. Each pile holds 12 event cards of its period, none
  repeated across piles, plus one of the six Coup! cards, each used once.
  The periods hold 24, 48 and 48 cards, so a game uses only 12, 24 and 36
  of them: no event is guaranteed to appear.
- Within a pile, the Coup card is one of the 13 - e - c remaining physical
  cards (e events and c Coup drawn so far from the pile), so it is equally
  likely in every position. Event candidates are the period's cards not yet
  drawn, weighted so that the pile's remaining event slots are a uniform
  subset of them.
- Pivotal events (#121–124) are never drawn.

Drawing uniformly without replacement from a set is the same distribution
as dealing from a shuffled deck, so the model faces exactly the deck a
table would produce, and nobody, including the harness, can know a card
before it is drawn. `python3 tools/deck.py selftest` simulates 2,000 full
decks and checks every constraint plus the Coup position distribution.

`ctl.py send` refuses to answer a card prompt. Setting `FITL_MANUAL_DECK=1`
restores manual entry (the observer types the numbers), for use only when
a human is supplying a physical deck.

## The patched program build

The release program saved the last action on a card, and a whole Coup round,
only after the next card number was typed. In this harness that number comes
from a human who may be away for hours, and the sandbox container can be
reclaimed in the meantime, losing the unsaved segment and forcing a replay
with fresh dice. `fitl/save-before-draw.patch` fixes that: the program now
saves as soon as an action or Coup round completes, records in the save that
a card draw is pending, and performs the draw as its own saved step at the
top of its main loop. A resumed game goes straight to the card prompt.

The jar `fire-in-the-lake_2.13-1.53-harness.jar` was compiled from the v1.53
source with `fitl/fitl-1.53-harness.patch` (save timing, symmetric
adjacency, and `fitl.Autoplay`) using scalac 2.13.18 and reports its version as `1.53+harness`. To rebuild: clone github.com/sellmerfud/fitl at v1.53, apply the
patch, compile `src/main/scala/**/*.scala` against `scala-library` and
`scala-parser-combinators`, and jar the classes together with a `version`
resource file.

## All-Bot games

`fitl.Autoplay` plays a Full-scenario game with all four factions as the
program's Tru'ng Bots, with no console: about 0.2 s a game, against 3.6 min
through `ctl.py`. Prompts are answered by a scripted reader (card numbers,
pauses, "continue playing? n"), so the program's own game logic runs
unchanged. Each game is seeded: the seed sets the program's single random
generator (dice, Tru'ng deck, Bot choices) and a separate generator built
from it lays out the event deck by the Full-scenario pile rules. The same
seed always plays the same game, so two variants can be compared on the
same seeds.

```
python3 tools/botrun.py --games 1000 --seed 1 --workers 4 --out results/run.jsonl
python3 tools/botrun.py --games 1000 --seed 1 --us-final-only --out results/run_fco.jsonl
python3 tools/botrun.py --summary results/run.jsonl
```

`--us-final-only` stops the US Bot winning before the final Coup (the
program's `noEarlyWin` hook), matching the human-US games' condition.
`--via-main` plays each game through the program's own interactive main loop
instead; 40 seeds gave identical games both ways, which is the check that
the Autoplay loop is faithful. About 3% of seeds hit a program bug (a Bot
loop that never ends, or a placement assertion; see `BUG_REPORTS.md`); a
watchdog records those as failures and the run carries on. As in the
program's own human-win option, the US is also blocked at the final Coup's
Victory phase, so a Bot above zero there wins; otherwise the highest margin
after Redeploy wins.

First calibration (seeds 1-1000, 4 workers, about 1 min a run): winners VC
69%, ARVN 16%, NVA 8%, US 8% (5% with `--us-final-only`); final US margin
-18 (sd 11). Summaries in `results/calib_*.txt`.

`--trace` adds every Bot action (card, faction, action, operations and
special activities, Event side, change in each score component) and each
Coup round's change to the record; `tools/botattrib.py` sums them by source
(`results/attrib_standard.txt` for seeds 1-1000). Same games as untraced.

### US policy

`--us-policy FILE` replaces the Tru'ng US cards with `fitl.USPolicy`
(`USPolicy.scala` in the patch). The program's own US Bot routines still
carry out every action, so the rules stay the program's; only the choice
changes. Modes:

- `trung` (`policies/trung.json`): the Tru'ng cards through the same hook.
  Seeds 1-1000 give games identical to no policy at all.
- `search` (`policies/search.json`): one-ply search. Candidates are Pass,
  the Event, and each US Operation with each Special Activity it may take
  (and Op only / Limited Op where the sequence of play allows), each also
  with a space "focus" (opposition, vc, nva, population) put in front of
  the US Bot's space priorities. Each is tried on a copy of the game on
  `samples` fresh dice streams and scored as a weighted sum of features
  (margins, how close each rival is to winning, more so before a Coup,
  insurgent pieces, Casualties, Resources, Aid, Trail, Terror, a bonus for
  Pass and for Critical/Performed Events). The best is carried out on dice
  no trial used. Weights and focuses come from the file; the defaults and
  feature names are in `USPolicy.scala`.

A trial that throws or runs past `trial_ms` (default 250) is discarded: the
program's Air Lift planning can loop forever (`BUG_REPORTS.md` #3), and the
search tries Air Lift often. That limit is wall-clock time, so a run under
heavy load can differ slightly from the same run unloaded.

First result, `search` with the default weights, seeds 1-200 (5 s a game):
US wins 46% (11% for the Tru'ng US on the same seeds), or 36% against 6%
with `--us-final-only`; the paired change in the final US margin is +12.4
(se 1.0). Summaries in `results/search_v1_*.txt`.

### Tuning

`tools/bottune.py --start policies/tune-start.json --name t1` tunes the
weights (and `hinge_buffer`). Each generation plays the current weights and
`--pairs` mirrored random perturbations of them on one fresh block of
`--games` seeds (the same seeds for all, so differences are paired), scores
each by its mean US lead (final US margin minus the best rival's), and steps
along the rank-weighted perturbations. Games use `--us-final-only` unless
`--all-wins`. Training seeds start at `--seed-base` (20000) and never repeat;
validate on other seeds with `botrun.py` and `botcompare.py`. Progress goes to
`results/tune_<name>.jsonl` (resumed from on restart) and the current weights
to `policies/tuned_<name>.json`. `policies/tune-start.json` is the search
default with the faster settings (1 dice sample, 60 ms trials, focuses
default/opposition/vc/nva: 2.7 s a game, no worse on a 60-seed check).

First run, `t1` (15 generations, 4 pairs, 80 seeds, about 2 hours): on
held-out seeds 1-400 with `--us-final-only`, `policies/tuned_t1.json` wins 40%
against 31% for `tune-start` (US lead +2.6, se 0.8) and 4% for the Tru'ng US
(lead +18.9, se 0.8). VC wins fell from 54% to 40%, NVA wins rose from 11% to
19%. Details in `results/val_t1.txt`.

Features added after `t1` (default weight 0, so older policy files play as
before; `policies/tune2-start.json` starts them from `tuned_t1`):
`tet_live`/`tet_near` and `easter_live`/`easter_near` (the VC and NVA pivotal
Events: playable now, and how close their conditions are), `agitate_exposure`
(what VC could Agitate at the next Coup) and `rival_hinge_coup_soon` (the
rival threat times the chance of a Coup in the 2 cards after the on-deck card,
from the pile structure). `FITL_POLICY_DEBUG=1` prints the features at each US
decision to stderr. `tools/botlosses.py` is the loss analysis that led to them
(`results/losses_t1.txt`).

Second run, `t2` (from `tune2-start`, seeds from 40000): on held-out seeds
1-400, `policies/tuned_t2.json` wins 43% against 39% for `tuned_t1` (US lead
+2.4, se 0.8). The new features with hand-set weights alone gave +0.9 (se
0.6); tuning added +1.6 (se 0.7). Tet and Easter Offensive are played as often
as before (about 0.9 a game each): the gain is in fewer early VC wins (77
against 101) and less Opposition from Coup rounds. `results/val_t2.txt`.

`FITL_POLICY_DESIGN=PREFIX` makes the search write, at each US decision, every
candidate's value and features to `PREFIX.<pid>`; `tools/botdesign.py POLICY
PREFIX.*` turns that into the within-decision design matrix (features minus
the decision's mean, since only differences between candidates matter): how
often each feature differs between candidates, its typical push on the
ranking, VIFs, correlations, and how often zeroing a weight or a group
changes the choice. `results/design_t2.txt` is the one for `tuned_t2`.

## Information boundary

The playing session may read: the rendered board view, `cards.json`,
`notes.md`, `journal.md`, the program's screen output and log lines. It may
**not** read the program's source, the bot logic, or the raw save files
(they contain the shuffled Tru'ng deck order). The source clone used to
build `cards.json` was kept outside this repository and deleted afterwards.

## Verification done during the build

- Program starts on plain Java 21 and reaches the scenario menu.
- `ctl.py new-game` reaches the first card prompt; the controller survives
  across separate shell invocations (tmux).
- `render.py` scores matched the program's `show summary` exactly at the
  checked points of a throwaway game (all four factions).
- `diff.py` output matched the program's own log narration for bot turns.
- With the patched build: a save exists for the last actor on a card, and
  for a Coup round, while the card prompt is waiting; stop and resume at
  that point goes straight to the card prompt with nothing replayed.
