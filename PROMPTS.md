# PROMPTS.md — the program's prompt chains for US actions

Taken from the program's own output (TestGame3 and TestGame4 transcripts and
harness test runs), not from memory. Use it to write a whole action as one
`ctl.py seq` call. Read it once per session.

**How `seq` answers.** Every answer is matched against the menu when the
prompt is numbered (exact label, else unique prefix) and typed as given when
the prompt is bare. So always write the label or the name (`Train`, `Saigon`,
`Finished selecting`), never a number. Digits, `y`, `n` and `abort` go
through unchanged. The expected text `*` matches any numbered menu; the
label match is then the only guard, so use it where the menu header below
is marked *(header varies or not recorded)*.

**Forms.** `[menu]` = numbered menu, `[typed]` = bare prompt that wants a
name or a number, `[varies]` = the same prompt has been seen both ways (it
depends on how many candidates there are), `[y/n]` = bare yes/no.

**Interface facts.**

- When exactly one space is legal the program selects it and executes
  without asking, so peeking at an option can commit it.
- `abort` inside a Special Activity aborts only that activity and returns
  to the operation's menu; at an operation menu, `abort` then `y` aborts the
  whole action with no state change.
- `abort` is refused at some sub-prompts (the Pacify level menu); answer
  "Do not pacify" and abort one level up.
- The Limited Op Sweep chain includes `US Move troops to <space> from`,
  which offers one adjacent source.
- During a Coup round the board view shows the pre-Coup save; read the
  phase results from the narration.
- The game-end prompt is `Do you want to continue playing this game?
  (y/n)`; `n` ends the game for good.

**Watch for.** The same menu shrinks and renumbers as you use it (a chosen
space drops out of the list; `Perform a Special Activity` disappears once
used). Labels are stable, numbers are not. A Limited Op skips the
"select another space" menu: after the one space, the next prompt is the
final-action menu.

---

## Every action starts here

| Prompt | Form | Entries / what to type |
| --- | --- | --- |
| `(perform or ?):` | typed | `perform` |
| `Choose one:` | menu | First eligible: `Event`, `Op (May add a Special Activity)`, `Pass`. Second eligible after an Op: `Limited Op`, `Pass` (plus `Event` if the first actor took Op + Special Activity). Second eligible after an Event: `Op`, `Pass`. |
| `Choose operation:` | menu | `Train`, `Patrol`, `Sweep`, `Assault` (`Sweep` is absent in Monsoon). |
| Event, dual-use card | menu *(header not recorded)* | `Unshaded`, `Shaded`; then the card's own prompts, usually `[menu]` space lists and `How many <piece> (a - b):` `[typed]`. |
| End of an Op without a Special Activity yet | y/n | `...perform a special activity? (y/n)`: `y` or `n`. |
| `Choose special activity:` | menu | `Advise`, `Air Lift`, `Air Strike`, `Do not perform a Special Activity now`. Reached from the `Perform a Special Activity` entry of an Op's menu, or from the y/n above. |
| `Really abort (y/n)?` | y/n | after typing `abort` at any prompt inside an action; no state change. |

## Train

| Prompt | Form | Entries |
| --- | --- | --- |
| `US Training:` | menu | `Select a space to Train`, `Perform a Special Activity`, `Finished selecting spaces` |
| `Train in which space:` | menu | candidate spaces, `None of the above` |
| `Training in <space>:` | menu | `Place Irregulars`, `Place Rangers`, `Place ARVN Troops/Police`, `Do not place forces` (only the possible ones) |
| `Place how many Irregulars (0 - 2):` | typed | a number; **not asked** when only one placement is possible |
| `US Training:` again | menu | repeat, or `Finished selecting spaces`. **Limited Op: this menu does not return**; the final-action menu comes next. |
| `Choose final Train action:` | menu | `Pacify`, `Transfer patronage to ARVN resources`, `Perform a Special Activity`, `Finished with Train operation` (only the possible ones) |
| `Pacify in which space:` | menu | candidate spaces, `None of the above` |
| pacify level *(header not recorded)* | menu | `Shift 2 levels to Active Support`, `Shift 1 level to Passive Support`, `Shift 1 level to Active Support`, `Do not pacify in <space>` |
| `Choose final Train action:` again | menu | repeat for another space, or `Finished with Train operation` |

```
seq "(perform or ?)=>perform" "Choose one=>Op" "Choose operation=>Train" \
    "US Training=>Select a space" "Train in which space=>Saigon" \
    "Training in Saigon=>Place Irregulars" "how many=>2" \
    "US Training=>Finished selecting" "final Train action=>Pacify" \
    "Pacify in which space=>Saigon" "*=>Shift 1 level" \
    "final Train action=>Perform a Special" "Choose special activity=>Advise" ...
```
Limited Op Train, one space: `... "Choose one=>Limited" "Choose operation=>Train" "US Training=>Select a space" "Train in which space=>Saigon" "*=>Place Irregulars" "how many=>2" "final Train action=>Finished"`.

## Patrol

| Prompt | Form | Entries |
| --- | --- | --- |
| `US Moving Patrol cubes:` | menu | `Move cubes`, `Perform a Special Activity`, `Finished moving cubes` |
| `Move cubes out of which space:` | menu | candidate spaces, `None of the above` |
| `Move how many cubes out of <space> (0 - n):` | typed | a number |
| `Select destination:` | typed | a space name (any LoC or City reachable along LoCs/Cities). **Limited Op: asked once**; every later move goes to the same destination without asking. |
| `US Moving Patrol cubes:` again | menu | repeat or `Finished moving cubes`; then the program activates guerrillas on LoCs by itself |
| `Choose one:` | menu | `Assault at one LOC`, `Perform a Special Activity`, `Do not Assault at one LOC` (absent if no LoC holds your cubes) |
| `Assault in which LOC:` | menu | candidate LoCs; **skipped when there is one candidate**. Known program bug: after a Limited Op Patrol into a City the City is offered here; decline it (rule 3.2.2 allows the Assault only in a LoC). |

## Sweep

| Prompt | Form | Entries |
| --- | --- | --- |
| `US Sweep space:` | menu | `Select a Sweep space`, `Perform a Special Activity`, `Finished selecting Sweep spaces` |
| `Sweep in which space:` | varies | a space name (typed) or a numbered candidate list |
| `US Sweep Troops into <space>:` *(and follow-ups)* | menu | which adjacent spaces to move Troops from and how many; entries name the source spaces |
| `US Sweep space:` again | menu | repeat or `Finished selecting Sweep spaces` |

## Assault

| Prompt | Form | Entries |
| --- | --- | --- |
| `US Assault:` | menu | `Select a space to Assault`, `Perform a Special Activity`, `Finished selecting spaces` |
| `Assault in which space:` | menu | candidate spaces, `None of the above` |
| ARVN participation, extra prompts | varies | asked only when ARVN cubes are present in the space |
| `US Assault:` again | menu | repeat or `Finished selecting spaces` |

## Advise (Special Activity)

| Prompt | Form | Entries |
| --- | --- | --- |
| `Choose Advise option:` | menu | `Sweep a space with ARVN forces`, `Assault a space with ARVN forces`, `Use Irregular/Ranger to remove enemy pieces`, `Finished selecting Advise spaces` (only the possible ones) |
| `Use Irregular/Ranger in which space:` | menu | candidate spaces, `None of the above` |
| `How many NVA Troops (0 - 1):`, `How many NVA Underground Guerrillas:`, ... | typed | numbers, one prompt per piece type present |
| `<Sweep/Assault> ... in which space:` | menu | candidate spaces, `None of the above` |
| `Do you wish to add +6 Aid? (y/n)` | y/n | asked once, after the second Advise space |
| `Choose Advise option:` again | menu | repeat (max 2 spaces) or `Finished selecting Advise spaces` |

## Air Lift (Special Activity)

| Prompt | Form | Entries |
| --- | --- | --- |
| `Select one:` | menu | `Select an Air Lift space`, `Lift forces out of <space>` (one per selected space), `Finished with Air Lift` |
| `Air Lift in which space:` | varies | a space name (typed in TestGame3) |
| `Lift forces to which space:` | menu | the other selected spaces, `Do not move forces now` |
| `Choose one:` | menu | `Air Lift US Troops`, `Air Lift ARVN Troops`, `Air Lift <Irregulars/Rangers>`, `Finished moving forces out of <space>` |
| `Move how many US Troops (…):` | typed | a number |
| `Select one:` again | menu | repeat or `Finished with Air Lift` |

Select all the spaces first (origins and destinations alike), then lift.

## Air Strike (Special Activity)

| Prompt | Form | Entries |
| --- | --- | --- |
| `Air Strike: (n hits remaining, remove up to n pieces)` | menu | `Select a space to Strike`, `Degrade the trail`, `Finished with Air Strike activity` |
| space and piece prompts | varies | space list `[menu]`, then which pieces `[menu]` / how many `[typed]` |

## Coup round decisions

| Prompt | Form | Entries |
| --- | --- | --- |
| `Choose space to pacify:` (Support phase; header line `US Pacification (n spaces remaining, r ARVN resources, Econ is e)`) | menu | candidate spaces, `Finished pacifying spaces` |
| `Pacify:` | menu | `Shift 2 levels to Active Support`, `Shift 1 level to Passive Support`, `Shift 1 level to Active Support`, `Do not pacify in <space>` |
| `Choose one:` (Commitment phase; header line `Moved so far: t/10 troops and b/2 bases`) | menu | `Move troops`, `Move a base`, `Finished moving pieces` |
| from-space *(header not recorded)* | menu | `Available box`, then spaces with the pieces |
| to-space *(header not recorded)* | menu | `Available box`, then COIN-controlled spaces, LoCs, Saigon |
| how many troops | typed | a number (when moving troops) |

## Pivotal event

`>>> US turn (Human) [PIVOTAL EVENT] <<<` then a y/n whether to play Linebacker II.
