# Claude plays Fire in the Lake

A harness in which a Claude Code session plays *Fire in the Lake* (GMT, 2nd
edition) as the **US** faction against the three Tru'ng bots implemented by
Curt Sellmer's `fitl` program, while a human observer supplies card draws,
keeps a physical board in sync, and audits the model's reasoning.

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
| `fitl/save-before-draw.patch` | The patch applied to the program: save after every action and Coup round *before* asking for the next card, and make the card draw its own saved step. |
| `tools/ctl.py` | Controller: holds the program in a persistent tmux session. `start`, `new-game`, `resume`, `send`, `enter`, `advance`, `read`, `screen`, `status`. |
| `tools/render.py` | Renders the latest save as the board view, with derived scores. |
| `tools/diff.py` | Mechanical delta between two saves plus the program's log lines. |
| `tools/fitl_state.py` | Shared save-loading, piece manifest, regions, scoring. |
| `tools/build_cards.py` | Build-time only. Produced `cards.json` from the program's source. |
| `cards.json` | All 130 cards: text, faction order, Tru'ng markings, pivotal conditions. |
| `games/<name>/` | The program's own saves (`save-NNN`, `log-NNN`). Committed after every US action. |
| `journal.md` | Full turn plans, rationales, rejections. The audit artifact. |
| `notes.md` | One line per model turn. Cross-session memory. |
| `transcript.log` | Everything the program printed, via tmux pipe-pane. |

## Running

Requirements: Java 11+, Python 3, tmux. From the repository root:

```
python3 tools/ctl.py new-game TestGame2     # first time
python3 tools/ctl.py resume TestGame2       # after a container/session loss
python3 tools/ctl.py status
python3 tools/render.py                     # board view of the latest save
python3 tools/diff.py                       # last two saves + program log
```

The program runs with the repository root as its working directory, so saves
land in `games/<name>/`.

## The patched program build

The release program saved the last action on a card, and a whole Coup round,
only after the next card number was typed. In this harness that number comes
from a human who may be away for hours, and the sandbox container can be
reclaimed in the meantime, losing the unsaved segment and forcing a replay
with fresh dice. `fitl/save-before-draw.patch` fixes that: the program now
saves as soon as an action or Coup round completes, records in the save that
a card draw is pending, and performs the draw as its own saved step at the
top of its main loop. A resumed game goes straight to the card prompt.

The jar `fire-in-the-lake_2.13-1.53-sbd.jar` was compiled from the v1.53
source with that patch using scalac 2.13.18 and reports its version as
`1.53+sbd`. To rebuild: clone github.com/sellmerfud/fitl at v1.53, apply the
patch, compile `src/main/scala/**/*.scala` against `scala-library` and
`scala-parser-combinators`, and jar the classes together with a `version`
resource file.

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
