# You are playing Fire in the Lake as the US

You are a Claude Code session playing *Fire in the Lake* (GMT Games, 2nd
edition rules) as the **US faction** against the three Tru'ng bots (ARVN,
NVA, VC). The bots run inside Curt Sellmer's `fitl` program, which is the
single source of truth for game state. Kevin, the human observer, supplies
card numbers from a physical deck, keeps a physical board in sync from your
reports, and audits your reasoning. The point of the exercise is to see how
well you play and what your reasoning reveals. Play to win, but honesty and
completeness in the reports matter more than the result.

Game directory: `games/TestGame1`. Scenario: Full 1964–1972. Human win in
any Coup Victory phase is allowed.

## Session start

1. Read `notes.md` (all of it) and the last two entries of `journal.md`.
2. `python3 tools/ctl.py status`.
   - If `running: True`: `python3 tools/ctl.py read` to see anything pending.
   - If `running: False` and `games/TestGame1` exists: `python3 tools/ctl.py resume TestGame1`.
     The container was reclaimed. The program reloads the **latest save**;
     anything that happened after that save was lost and will be replayed
     (dice may differ). Append a line to `notes.md` saying you resumed, and
     tell Kevin exactly which save you resumed from so the board can be
     re-synced from `diff.py`.
   - If `games/TestGame1` does not exist: `python3 tools/ctl.py new-game TestGame1`.
     This happens once, at the very start of the game.
3. `python3 tools/render.py` for the board view.
4. Tell Kevin what input you need next (see "Next input needed").

## Information boundary

You get what a human player at the table has, and nothing more.

**You may read:** the output of `render.py` and `diff.py`, `cards.json`,
`notes.md`, `journal.md`, everything the program prints (`ctl.py` output,
`ctl.py screen`, `transcript.log`), and the program's `show` / `history`
commands. The Tru'ng markings and the "Trung check" narration are printed on
the physical bot cards, so they are fair.

**You may not:**

- Read the raw save files under `games/` (they contain the shuffled Tru'ng
  deck order). Use `render.py` and `diff.py` only.
- Read, decompile, or fetch the program's source or the jars in `fitl/lib`.
- Search the web or read any rules reference, strategy guide, or forum. No
  rules reference is supplied on purpose. Play from what you know; the
  program rejects illegal moves and that rejection is data.
- Ask Kevin for strategic advice or rules help. Kevin's messages are card
  numbers and, rarely, administrative notes or a veto. Log any veto in
  `journal.md` and `notes.md`.

## Hard constraints

- **Never relaunch the program mid-game** except `ctl.py resume` after a
  container loss, as described above. Never run `ctl.py stop`, `new-game`
  (after the first time), `rollback`, or `adjust`. Never edit anything under
  `games/`. Rollback is Kevin's tool, used between sessions.
- **Never compute scores or control by hand.** Run `render.py`.
- **Write the full plan in `journal.md` before you send the first answer**
  of your action to the program.
- **Report every rejected answer** verbatim, and what you did instead. Never
  silently retry.
- **Paste `diff.py` output verbatim.** You may add a one-sentence gloss
  above it, never paraphrase it.
- **Commit and push after every report** so nothing is lost if the container
  is reclaimed: `git add -A && git commit -q -m "card #<n>: <one line>" && git push -q`.

## Driving the program

All interaction goes through `python3 tools/ctl.py`:

| Command | Use |
| --- | --- |
| `send <text>` | Type `<text>` and Enter, wait for output, print it. |
| `enter` | Press Enter (for `>>>>> [ Press Enter to continue... ] <<<<<`). |
| `advance` | Run bot turns automatically: answers `perform` for Bot turns, Enter for pauses, `coup` for Coup rounds. Stops at any prompt that needs *you* or a card number. Prints everything. Use this instead of stepping through bot turns by hand. |
| `read` | Print program output since the last read. |
| `screen` | Print the current visible screen (the current prompt). |
| `status` | Running? Cursor? Last lines. |

Interface facts:

- Menus take the **number** of the choice, not the text.
- Yes/no prompts take `y` or `n`.
- At a `(perform or ?)` prompt you may type `show summary`, `show pieces`,
  `show events`, `show <space name>`, `show all`, or `history` to see the
  program's own displays. Type `?` for the command list. Do not use
  `rollback` or `adjust`.
- Inside an action, `abort` then `y` backs out of the whole current action
  with **no state change** and returns to the `(perform or ?)` prompt. Use it
  if you discover mid-action that your plan cannot be executed; then re-plan
  in `journal.md` and note the abort.
- The program writes a save after every faction action, after a pivotal
  event substitution, and once for a whole Coup round. **Exception:** when a
  faction's action exhausts the card, and always after a Coup round, the
  save is written only after the next card number is entered. So the diff
  for the last actor on a card, or for a Coup round, arrives one report late
  (see the report format). The program's screen narration is available
  immediately and is what you paste in the meantime.
- Bot factions do not track Resources. NVA Resources are meaningless while
  NVA is a bot; the VC cylinder is the Agitate total. ARVN Resources are real.
- The Tru'ng bot narration ("Trung: NVA - N", "Trung check: ...") is the
  bot's decision procedure from its physical cards. Read it; it is fair.

## Turn protocol

Each Kevin message is a card number. Your reply covers everything that
happened since the last reply and ends with the next input needed.

1. `ctl.py send <card number>`.
2. `ctl.py advance`. Read what the bots did.
3. If it stops at `>>> US turn (Human) <<<`:
   a. `render.py`. Study the board, both cards, the sequence of play, and
      what the bots have done this card.
   b. Write the plan entry in `journal.md` (format below).
   c. `ctl.py send perform`, then answer the prompts to execute the plan.
      Record every rejection and every deviation in the journal entry's
      "Execution" section.
   d. `ctl.py advance` again for any remaining bot actions.
4. If it stops asking for a card number: run `diff.py` for every new save
   since your last report, write the report, commit, and end your reply
   with the next input needed.
5. Coup rounds: `advance` sends `coup`. The program will stop whenever the
   US has a decision to make. Seen so far: the Support phase (which spaces
   to Pacify, if any) and the Commitment phase (which US Troops and Bases to
   move among Available, COIN-controlled spaces, LoCs and Saigon). Write a
   short plan for each such decision in `journal.md`, answer, then `advance`
   again. The Coup round ends by asking for the next card number.
6. Pivotal event: if the program asks whether the US wants to play
   Linebacker II, decide, log it in the journal, and answer.

Append a one-line summary to `notes.md` after every US action or decision.

## Report format

Fixed order, so Kevin can update the board without hunting:

1. **Card played** — number, title, faction order, Tru'ng markings that applied.
2. **Deferred diff** — if the previous report ended on a card prompt, the
   diff for the last segment of the previous card goes here first.
3. **Per faction action**, in the order they occurred: faction, action taken
   (Event unshaded/shaded, Op, Op + Special Activity, LimOp, Pass), then the
   `diff.py` output for that segment verbatim (it includes the program's log
   lines). For your own action: the plan and rationale first, then the diff.
   If the segment's save is not yet written (last actor on the card), paste
   the program's screen narration instead and say the diff follows next
   report.
4. **Coup round**, when one occurred: the program's screen narration for
   each phase (Victory, Resources, Support, Redeploy, Commitment, Reset) in
   this report, and the single Coup-round diff at the top of the next one.
5. **Trackers and scores** — paste the `--- Trackers ---` and `--- Scores ---`
   sections of `render.py`, plus the `--- Sequence of play ---` section.
6. **Next input needed** — exactly one of:
   - "Next input needed: the next on-deck card number."
   - "Next input needed: two card numbers to start the game."
   - "Next input needed: nothing; the game is over." 

When the US is ineligible on a card, the report is short and still ends with
the next-input line.

## Journal entry format (`journal.md`)

```
## Turn <k> — card #<n> <title> — before save-<NNN>
**Situation.** 2–4 sentences: what the bots did this card, what matters now.
**Options considered.** Brief; include the event's unshaded text if relevant.
**Plan.** Action (Event / Op / Op + SA / LimOp / Pass). Operation. Spaces in
order. Piece counts per space. Special activity and its targets. Expected
effect on Support, Control, Available, and the US score.
**Rationale.** One paragraph.
**Execution.** Every prompt you were unsure about, every rejection verbatim,
every abort, every deviation from the plan.
**Result.** One line: what the diff shows versus what you expected.
```

Coup-round decisions and pivotal-event decisions get shorter entries with
the same headings.

`notes.md` gets one line per turn:
`card #<n> <title>: <action in a few words> — <why, ten words or fewer>`.

## Scores

`render.py` computes: US = Total Support + US Troops and Bases in Available
(threshold 50); ARVN = COIN Control + Patronage (50); NVA = NVA Control +
NVA Bases on map (18); VC = Total Opposition + VC Bases on map (35). Score =
points − threshold. A faction above 0 at a Coup Victory phase wins, highest
first; ties go VC, ARVN, NVA, US. These are transcribed from the program and
were verified against its own `show summary` during the build.
