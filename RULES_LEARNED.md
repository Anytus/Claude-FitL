# Fire in the Lake, US faction: what the program taught me

> **Harness changes before TestGame5.** Read these first; some of the
> working habits recorded below have been replaced by tools.
>
> - **Event cards** are drawn by the harness: `ctl.py advance` answers the
>   card prompt with a fresh random draw and prints `[deck] ... -> drew #N`.
>   The deck is built as the rules say (one 1964 pile, two 1965 piles, three
>   1968 piles, 12 events plus a Coup card each); which cards appear is
>   unknown to everyone until drawn. `ctl.py send` refuses a card prompt.
> - **`advance` now does three things in one call**: runs the bots, writes
>   the report file for every card it finishes (`wrote reports/...`), and
>   prints the **briefing** when it stops at the US turn: the board view,
>   both cards' full text and Tru'ng markings, scores, sequence of play, and
>   the neighbours of every space with US pieces. `ctl.py brief` prints it
>   again on demand (with this card's narration so far). There is no need
>   to run `render.py`, grep the transcript, look cards up in `cards.json`
>   or call `map.py` for your own spaces before a decision.
> - **`ctl.py commit-turn "<notes line>"`** ends a card: it appends the line
>   to `notes.md`, writes any report not yet written, commits with the line
>   as the message and pushes. One call replaces notes, report, commit, push.
> - **Answering prompts.** `ctl.py seq "<expected>=><answer>" ...` sends a
>   whole action's answers in one call, each sent only if `<expected>` is in
>   the current prompt. **Answers are matched by label when the prompt is a
>   numbered menu and typed as given when it is bare**, so the "bare or
>   numbered?" guessing recorded in section 1 is over: write `Saigon`,
>   `Train`, `Finished selecting`, never a number, whichever form the program
>   uses this time. After a rejected answer the re-prompted menu is still
>   matched. `*` as the expected text matches any numbered menu (the label is
>   then the guard). **`PROMPTS.md`** lists every prompt chain seen so far,
>   with each prompt's form; write the `seq` from it. TestGame4 used `seq`
>   one prompt per call 87 times, which is what these changes remove.
> - **Reports.** `tools/report.py` writes the observer's report from the
>   program's own log files (narration verbatim, then the board summary)
>   to `reports/<game>/`. `advance` runs it for you at every card draw.
> - **The map.** `python3 tools/map.py <space>` lists a space's neighbours
>   and `map.py <a> <b>` says whether two spaces touch, from the program's
>   own table (three one-way entries in the release table are two-way in
>   this build, as rule 1.3.6 requires; the author has since fixed them
>   upstream). Do not work from a remembered map.
> - **Program build 1.53+harness**, unchanged since TestGame4. One program
>   bug is known and unfixed: after a **Limited Op Patrol whose destination
>   is a City**, the program offers (and with one candidate, executes without
>   asking) the free Assault in that City. Rule 3.2.2 allows it only in a
>   LoC. Decline it (`Do not Assault at one LOC`), and never plan on it.
>   That is what happened on TestGame4's card #43 (Kontum); the absence of
>   the option on card #14 (Saigon, a full Op) was the program being right.
> - **Tool calls are logged** by a hook to a file outside the tree; it
>   changes nothing.
>
> Everything below about the program's prompts, operations, Coup phases and
> bot behaviour still holds.

Written for the next playing session, from four games: TestGame1 (lost to the
VC at the 3rd Coup, cards #63 to the Coup), TestGame2 (won at the 3rd Coup by
4, the full 1964 opening through 24 cards and three Coup rounds), TestGame3
(won at the 3rd Coup by 8, the full 1964 opening through 39 cards, then
continued past the win for rules exploration) and TestGame4 (won at the 2nd
Coup by 6, 26 cards, harness-drawn deck). Everything here was observed at
the program's own prompts or in its narration; it is descriptive, not advice.
Where an earlier note turned out to be wrong, the correction is here and the
old claim is struck. Where I am inferring rather than reporting, I say so.

**Still unobserved after four games:** Air Strike carried through to a hit
(the menu has been opened and aborted, never resolved); Sweep activation
ratios outside Lowland; the "add an ARVN Assault" option inside a US Assault,
which has never been prompted; Train's forced removal of ARVN cubes from the
map when Available is short of 6. ~~The Train "Transfer patronage to ARVN
resources" action~~ was executed in TestGame4 at last (section 3). A US
Patrol printed no Resource deduction in TestGame4 either: it is free.

## 1. Driving the program

- `python3 tools/ctl.py send <text>` types one answer and prints the reply.
  `advance` runs bot turns and Coup phases until a prompt needs you (it
  draws cards itself). `screen` prints the current prompt with its menu.
  `seq` answers a whole chain of prompts, each guarded (see the harness
  note at the top).
- ~~**One send per command, and print the screen before every answer.**~~
  **Superseded before TestGame4 by `seq` with `#label` answers**, which
  checks each prompt and resolves labels against the current menu. The
  history that follows is why that matters. Menus
  renumber in three different ways: a chosen space drops out of a space list;
  an option that is not currently legal is simply omitted (the final Train menu
  drops Pacify when no selected space can be pacified, the Special Activity
  menu drops Air Strike while a ban is in force, Advise drops the removal
  option once no space qualifies); and the first-eligible / second-eligible
  action menus have different shapes. Every one of my worst mistakes in both
  games was a number sent to a menu I had not read — in TestGame2 a two-entry
  final Train menu read `1) Transfer patronage  2) Finished`, I sent 2 from the
  remembered three-entry shape, and the whole action was spent doing nothing.
  Never chain two sends with the output discarded. **TestGame3 repeated it
  twice**: a "2" chained into a Special Activity menu that had dropped Advise
  opened Air Strike instead of Air Lift, and a "2" chained into a Limited Op's
  final Train menu hit `Finished` instead of `Transfer patronage`, wasting the
  action. Three games, three actions lost to the same habit.
- **Some space prompts come with no list at all.** `Train in which space:`
  and `Air Lift in which space:` both arrived as a bare prompt several times;
  a typed space name (`Quang Tri-Thua Thien`, `Saigon`) is accepted. The very
  same prompt arrived numbered on other occasions, and then a typed name is
  rejected: `'Saigon' is not valid. Must be one of: 1, 2, ..., or abort`. There
  is no way to tell in advance. TestGame4 met it again: `Select
  destination:` (Patrol) was bare on card #43 and numbered on card #14, and
  `Sweep in which space:` was numbered where TestGame3 had it bare.
  **Superseded before TestGame5:** `seq` now sends the number when the
  prompt is a menu and the text when it is bare, from the same answer, so
  give the name and stop worrying about the form.
- When exactly one space is legal the program selects it and executes at once
  — choosing "Use Irregular/Ranger to remove enemy pieces" with one qualifying
  space printed `Use Irregular/Ranger in which space:  Binh Dinh` and removed
  the pieces without a further prompt. Peeking at an option can commit it.
- The action menu shapes, all now observed rather than inferred:
  first eligible `1) Event  2) Op (May add a Special Activity)  3) Pass`;
  second eligible after an Event `1) Op (May add a Special Activity)  2) Pass`;
  second eligible after an Op + Special Activity `1) Event  2) Limited Op
  3) Pass`; second eligible after an **Op Only** `1) Limited Op  2) Pass` —
  the Event is closed. A bot's Op Only therefore removes both the Event and any
  Special Activity from the faction behind it; this happened twice.
  **TestGame4 used this the other way round:** a US **Op Only** (Train with
  no Special Activity, `n` to `Do you wish to perform a special activity?
  (y/n)`, which prints `Move the US cylinder to the Op Only box`) closed a
  VC Critical shaded Event to the whole second-eligible slot on card #26 —
  the VC drew its Tru'ng card and was held to a Limited Op. The slot also
  survives a pass: on #118 the VC took the Event, ARVN passed, and the NVA
  still got the full second-eligible menu. So Op Only denies the Event to
  everyone behind you, and it costs only the Special Activity.
- A Limited Op is a single space with no Special Activity, but a Limited Op
  Train **does** still offer the final Train action (Pacify / Transfer
  patronage) for that one space. **The Limited Op skips the "Finished
  selecting spaces" step**: the final Train menu appears immediately after the
  one space's placement choice, so the answer you would have spent on
  "Finished" lands on the final menu instead. That is what cost TestGame3 an
  action on card #108. (A `seq` step expecting `US Training` stops here
  instead, since that text never appears; this exact case was tested.)
  **A Limited Op Patrol funnels every move into one destination**: the
  program asks `Select destination:` once and every later `Move cubes`
  goes there without asking (TestGame4 card #43 wasted a second Troop
  finding this out). **A Limited Op Sweep does move Troops**: `US Sweep
  space` -> `Sweep in which space` -> `US Sweep Troops into <space>` ->
  `US Move troops to <space> from` (adjacent spaces holding US Troops) ->
  a count; only one source was offered (TestGame4 card #66).
- **abort has two different scopes.** Sent inside a Special Activity it aborts
  **only that Special Activity** (`>>>> Aborting Air Strike special activity
  <<<< / No changes need to be made to the game board`) and returns to the
  operation's own menu, not to `(perform or ?)`. Sent at an operation menu it
  aborts the whole action, and the program then prints the full reversal for
  the physical board — `The following changes should be made to the game
  board`, a `Remove from <space> to Available:` block, a `Changes to <space>:`
  block per space, a status block per space and the Available list. A TestGame3
  Sweep aborted that way left `render.py` identical to before. abort is
  **rejected at some sub-prompts**: at the Pacify level menu it printed
  `'abort' is not valid. Must be one of: 1 or 2`, and the way out was to answer
  "Do not pacify" and then abort at the menu above.
- **The container was lost three times in TestGame3**, twice at a
  `(perform or ?)` prompt and once in the middle of a Patrol. `ctl.py resume
  TestGame3` reloaded the latest save each time. The mid-action loss simply
  rolled the half-entered Patrol back to the save taken before it, exactly as
  an abort would have.
- The card prompt accepts only a card number: `'perform' is not a card number`.
  Harmless.
- `?` at `(perform or ?)` lists perform, show, history, rollback, inspect,
  adjust, help, quit. `show summary` prints scores, resources, Aid, Patronage,
  Trail, leader, cards drawn.
- `abort` then `y` inside an action undoes the whole action (TestGame1).
- The patched build (1.53+harness, formerly 1.53+sbd) saves after every
  faction action, each card draw, each pivotal substitution, and once for
  a whole Coup round. In
  TestGame2 the container was lost **six times**, always at the card prompt;
  `ctl.py resume TestGame2` reloaded the latest save and returned to the same
  prompt every time with nothing replayed. Two consequences: during a Coup
  round `render.py` shows the pre-Coup save, so read the phase results from the
  narration; and `transcript.log` restarts on resume, but `report.py` builds
  the report from the saved log files, so nothing is lost with it.
- The game-end prompt is `Do you want to continue playing this game? (y/n)`;
  `n` prints `>>> The game has ended <<<` and drops to `(quit or ?)`.

## 2. Sequence of play, as observed

- The card names an order of four factions. A card ends when two factions have
  acted, or when every eligible faction has acted or passed. Passing keeps you
  Eligible and pays +3 ARVN Resources (for US or ARVN). After the first
  eligible passes, the next faction in order is treated as first eligible
  (inferred: the ARVN bot's marking pointed it at the Event after my pass on
  Tribesmen; it passed instead, so I never saw its menu). Both eligible
  factions passed on that card and it resolved with nothing happening;
  everyone stayed Eligible.
- **Turn order is the only reliable way to guarantee yourself an action.** If
  the factions ahead of you in the next card's order are all Ineligible, your
  action there is certain; if it depends on a bot choosing to act (so that it
  becomes Ineligible), it is not. Both cases happened, and the second one cost
  a card.
- Acting makes you Ineligible on the next card. Some events extend this:
  Henry Cabot Lodge shaded printed `ARVN is ineligible through the next card`
  and the sequence display showed `ARVN(-) -> Event`.
- Events that say "stay Eligible" do exactly that (TestGame1: Claymores
  unshaded, Medevac shaded).
- After a Coup round every faction is Eligible.
- **Tru'ng markings (Critical / Performed / Ignored, with a side) as a
  predictor, over both games.** Critical: taken every time it was reachable
  (TestGame2: VC 6 of 6, ARVN 3 of 3). Performed: usually taken, but it is a
  preference, not a commitment — ARVN, sole eligible and marked Performed on
  Tribesmen, passed and banked +3 instead. Ignored: an Op every time. A bot
  marked for the shaded side will take the unshaded side if that is what is
  left (ARVN took Nam Dong, Operation Starlite and Annam unshaded, each time
  removing enemy pieces or denying a bot ally the shaded text — bots do not
  coordinate).
- The ARVN bot's events did a large share of the US's work in TestGame2
  (Economic Aid, Nam Dong, Medevac, Operation Starlite, Annam); a bot marked
  for a side you also want is, for that card, on your side.
- **Pivotal events.** At a card draw the program rolled for the bots in the
  order VC, then ARVN: `VC Bot Pivotal Event die roll: 5 [Failure] (2 cards in
  leader box)`, `ARVN Bot Pivotal Event die roll: 1 [Success] (2 cards in
  leader box)` — consistent with success needing a roll no higher than the
  number of cards in the leader box. The successful pivotal **replaced the
  current card** (`Replace the current event card with #123 - Vietnamization`),
  the playing faction acted first, and the others followed in the pivotal's
  own order with everyone Eligible. Duong Van Minh does not count as a card.
  ARVN's Vietnamization needs fewer than 20 US Troops on the map; it fired
  with 9. **The US was not asked about Linebacker II at that draw** although I
  was Eligible, two cards were in the box and Support + Available was 54; in
  TestGame1 the prompt `Does US wish to play their pivotal?` did appear. I do
  not know whether a bot's success pre-empts the human prompt or whether the
  program's US condition has a part the card text does not show. Also: the
  prompt did not appear on a Monsoon card with a Coup on deck (TestGame1).
  **TestGame3 saw all four pivotals fire.** The US prompt did appear, at the
  draw right after Coup 2 and right after the NVA's roll failed:
  `NVA Bot Pivotal Event die roll: 2 [Failure] (2 cards in leader box)` then
  `Pivotal Events can be played / Eligible: ARVN, NVA, and US / Trumped: ARVN
  and NVA / Does US wish to play their pivotal?` — so the program prints which
  factions are eligible and which the US's own pivotal trumps, and a bot's
  failed roll does not close the human prompt. Answering `1` replaced the
  current card; `perform` then executed the event with no further menu.
  Later the NVA's roll succeeded (Easter Offensive), then ARVN's
  (Vietnamization), then the VC's (Tet Offensive) — each replacing the current
  card. Tet Offensive, played after three cards were in the leader box, was the
  single most destructive card of the game: nine free Terrors, a Base and two
  Guerrillas into each of two Cities, then free Attacks everywhere.
- **Monsoon** (the card before a Coup): Sweep prohibited as an Op; Air Strike
  limited to 2 spaces; an event's free Sweep is still allowed (TestGame1). In
  TestGame3 the operation menu printed `Sweep is prohibited [Not allowed in
  Monsoon]` and simply listed `1) Train 2) Patrol 3) Assault`, and Advise's
  own option list dropped its `Sweep a space with ARVN forces` entry too.
- The render's "13 cards per campaign" is nominal: campaign 2 ran sixteen event
  cards before its Coup and campaign 3 ran two.

## 3. US Operations

**Train.** The space list is every space holding **any US piece** — Troops,
Irregulars, or a Base. ~~Spaces with US Troops (Bases alone were not
offered)~~: Quang Tri-Thua Thien was offered holding only Irregulars, and
Pleiku-Darlac holding an Irregular and a Base; Saigon was offered holding only
a US Base, though Saigon may simply always be offered. In each selected space:
- with a US Base present ~~, or in Saigon~~: `Place Irregulars / Place Rangers
  / Place ARVN Troops/Police / Do not place forces`. ARVN cubes are up to 6 in
  total (`Troops (0 - 6)`, then `Police (0 - 4)` after 2 Troops) and cost 3
  ARVN Resources for the space; Rangers cost 3 too. **Saigon is not special**:
  in TestGame3, with 81 Resources against Econ 10 and a full ARVN Available
  box, Saigon with no US Base offered only `Place Irregulars / Do not place
  forces`. The TestGame2 Saigon that offered cubes had a US Base in it;
- without a US Base: `Place Irregulars / Do not place forces` only;
- **the cube option is also gated by ARVN Resources exceeding Econ**, the same
  test as Pacify. Pleiku-Darlac held a US Base and offered no cubes at 12
  Resources against Econ 15; the same space offered them at 18 against 13.
- **Kevin's note, not yet seen at a prompt:** US Train may place up to 6 ARVN
  cubes *regardless of what is in the ARVN Available box*, taking the excess
  from anywhere on the map. In TestGame3 Available always held enough (6 Troops
  into Quang Tri, 5 Troops and 1 Police into Binh Dinh), so the removal menu
  has still never appeared. This matters: it is how the US moves ARVN cubes out
  of the Saigon and Hue garrisons the bot piles up, and it is also the fastest
  way to empty ARVN's Available box, which is the gate on its Govern activity;
- **Irregular placement costs nothing.** The cap is 2 per space and the
  prompt's upper bound is Available *plus* voluntary removals: asking for 2
  with 1 Available produced `There are not enough US Irregulars in the
  available box / You must remove 1 US Irregular from the map` and a menu of
  spaces to take one from. Answer with the same space to net +1 harmlessly.
- "Do not place forces" costs nothing and still counts the space as trained.
Final action, in **one** selected space:
- **Pacify.** Requires only that the space be COIN-controlled and one of the
  selected Train spaces. ~~needs US Troops and ARVN Police there~~: it pacified
  Quang Tri-Thua Thien with nothing but Irregulars and Police, Pleiku-Darlac
  with an Irregular and a Base, and Kien Hoa-Vinh Binh twice with US Troops and
  no ARVN Police at all. Up to 2 levels, 3 Resources per level under Duong Van
  Minh, Nguyen Khanh and Nguyen Van Thieu (4 under Nguyen Cao Ky, in TestGame1
  and again in TestGame3). It works from Opposition: `Shift 2 levels to
  Neutral` from Active Opposition, `Shift 2 levels to Passive Support` from
  Passive Opposition. The menu offers the whole shift as one entry. Refused
  when ARVN Resources do not exceed Econ (TestGame1: `Only 12 ARVN resources
  available and Econ is 15`). Pacify is absent from the menu when no selected
  space has a level to gain. Two corrections from TestGame3:
  - ~~Terror markers cost a level each~~ — **removing a terror marker does not
    count against the 2-level cap**. Saigon at Passive Opposition with one
    terror marker offered `1) Remove 1 terror marker and shift 2 levels to
    Passive Support`, three steps for 9 Resources, and took a pop-6 City from
    6 VC points to 6 US points in one action. Always read the menu: the whole
    swing may be one entry.
  - **The number of levels offered depends on how much Resource headroom is
    left above Econ.** At 18 Resources against Econ 13, Quang Tri offered only
    `Shift 1 level to Passive Support` (one level would leave 15, two would
    leave 12, below Econ); at 42 against 13 the same leader offered two. Plan
    pacification against the headroom, not the total.
- **Transfer patronage to ARVN resources.** Offered **only when Saigon is one
  of the selected Train spaces**, now confirmed three ways: absent on Trains
  without Saigon, present as `2) Transfer patronage to ARVN resources` in a
  three-entry final menu with Saigon selected, and present in a Limited Op
  Train of Saigon. **Executed in TestGame4 (card #67):** the prompt is
  `Transfer how much patronage to ARVN resources (0 - 3)`, so it is **capped
  at 3, one for one** — Patronage 14 -> 11, ARVN Resources 11 -> 14, ARVN
  score 34 -> 31. A small, reliable 3 points off ARVN that also lifts its
  Resources back over the Econ floor for your own pacification; never worth
  more than a pacification, and it is offered with Pacify absent whenever
  Resources are at or below Econ.
- A space used for Train cannot also be used by Advise in the same action, and
  vice versa; a space used by Advise disappears from the Train list. Air Lift
  has no such restriction: I lifted into a space and then selected it for
  Train, and also selected it for Train first and lifted into it after.

**Assault.** Flow: `US Assault: 1) Select a space to Assault 2) Perform a
Special Activity 3) Finished selecting spaces`, then a numbered space list of
the spaces that qualify; several spaces may be assaulted in one Op, and when
only one remains the program names and resolves it without a prompt
(`Assault in which space:  Da Nang`), ending with `There are no more spaces
eligible for Assault`. **It costs the US no Resources** — no deduction was ever
printed. Only spaces with US Troops and removable enemies are offered; it
removes NVA Troops and Active Guerrillas, Bases last.
Hits observed, all four data points: 2 US Troops in Saigon with a US Base, 4
hits (TestGame1); 2 cubes in Highland, 1 hit (TestGame1); **1 US Troop with a
US Base in Highland, 2 hits; 1 US Troop in a City, 1 hit** (TestGame3). A US
Base in the space roughly doubles the count.
**Underground Guerrillas shield a Base from Assault.** Saigon, holding a VC
Base, 1 Underground VC Guerrilla and 3 US Troops, was simply not on the
Assault list; a Sweep to Activate that Guerrilla is the way in. An
*undefended* Base is a legal target (see Advise's ARVN Assault below).
The "add an ARVN Assault at cost 0" option the card tips mention has never been
prompted in three games.

**Sweep.** Used in TestGame3, both in place (a Limited Op in Saigon, which
just printed `Flip 1 VC Underground Guerrilla in Saigon to ACTIVE` and ended)
and as a full Op explored and then aborted. The flow:
- `US Sweep space: 1) Select a Sweep space 2) Perform a Special Activity
  3) Finished selecting Sweep spaces`. The space prompt is **bare** (typed
  names). Any number of spaces may be selected before anything moves, and a
  selected space with no Troops moved in still resolves.
- Then `US Sweep Troops into: <each selected space>`, and per destination
  `US Move troops to <space> from:` listing the **adjacent** spaces that hold
  US Troops. Quang Nam offered Da Nang and Quang Tri-Thua Thien, both adjacent;
  nothing further away was listed, so movement is one space.
- **Only US Troops move.** The ARVN Troops standing in the same source spaces
  were never offered, so a US Sweep cannot reposition ARVN cubes (Air Lift and
  Train are the tools for that). A source stays on the list after moving 0.
- Then `Sweep activation:` with `1) Resolve all remaining Sweep spaces
  2) Perform a Special Activity 3) Resolve Sweep in <space>` per space, so
  spaces resolve one at a time. **3 US Troops moved into a Lowland Province
  flipped 3 Underground Guerrillas Active**: one per Troop, with the ARVN cubes
  already in the space adding nothing. Ratios in Highland, Jungle and City are
  still untested.
- Sweep is prohibited in Monsoon and the VC's Booby Traps shaded capability
  (`Each Sweep space, VC afterward removes 1 Sweeping Troop on roll of 1-3, US
  to Casualties`) makes it expensive while in play.
Advise's "Sweep a space with ARVN forces" is a different thing: it only
Activates Guerrillas in place, and no cube movement is offered.

**Patrol.** Explored in TestGame3 (the container was lost mid-action and the
resume rolled it back, which is the only reason it does not appear in that
game's log). The flow:
- `US Moving Patrol cubes: 1) Move cubes 2) Perform a Special Activity
  3) Finished moving cubes`, then `Move cubes out of which space:` listing
  every space holding US cubes, numbered.
- Per source: `These cubes can move: 3 US Troops` — **US cubes only**, the ARVN
  Police in the same space was not offered — then a count, then
  `Select destination:` as a **bare** prompt.
- **Destinations are LoCs and Cities only,** ~~anywhere on the map~~
  **reachable from the source along a chain of adjacent LoCs and Cities**,
  which ends at the first space holding an NVA or VC piece. TestGame3's list
  from Saigon spanned most of the map because Saigon's LoC network does;
  TestGame4's list from Kien Hoa-Vinh Binh was `Can Tho, four LoCs, Saigon`
  (card #14). Typing a Province is rejected with the legal list.
- After `Finished moving cubes`: `US Patrol - Activating guerrillas on LOCs`,
  then `Choose one: 1) Assault at one LOC 2) Perform a Special Activity
  3) Do not Assault at one LOC`. The free Assault at a LoC holding 1 US Troop
  and 3 ARVN Police `inflicts 1 hit` — the US cube alone counted, not the ARVN
  Police beside it — and removed an NVA Active Guerrilla. **The `Assault at
  one LOC` entry appears only when a LoC holds your cubes** (TestGame4 card
  #14: Patrol into Saigon, no LoC touched, no Assault offered — correct).
  When it appears after a **Limited Op Patrol into a City** it is the
  program bug in the harness note: TestGame4 card #43 printed `US assaults
  in Kontum` for 2 hits. Decline it.
- **No Resource deduction was printed**, so a US Patrol appears to be free;
  ARVN pays 3 per destination for its own.
ARVN's Patrol, seen often: cubes from Saigon onto LoCs, Guerrillas Activated on
each destination LoC, then one Assault on a LoC. In TestGame3 the bot used it
to empty Saigon of every cube twice, which cost COIN Control there.

## 4. US Special Activities

**Advise.** Up to 2 spaces. The option list is built from what is legal:
`Sweep a space with ARVN forces`, `Assault a space with ARVN forces`, `Use
Irregular/Ranger to remove enemy pieces`, and options vanish once used up.
The removal is the best tool the US has and the TestGame1 note about it was
wrong: ~~the pieces offered were Troops and an Active Guerrilla, not
Underground ones~~. Observed:
- it needs an **Underground** US Irregular or ARVN Ranger in the space (ARVN
  Rangers count — a pair ARVN had Transported into Binh Dinh let me break NVA
  Control there), flips that piece Active, and removes **2 enemy pieces**;
- it removes **Underground Guerrillas** (2 VC in Binh Dinh, 2 VC in Quang
  Tri), **Active Guerrillas** (3 NVA Active were listed beside 2 NVA Troops in
  Da Nang, correcting the TestGame2 implication that only Underground ones
  qualify), NVA Troops, and an **undefended Base** (the lone VC Base in
  Pleiku-Darlac). Bases are last: while other enemy pieces stand in the space
  the Base is not on the list;
- when several piece types are present it lets you choose: `Select 2 pieces
  among the following: 5 NVA Troops, 1 NVA Underground Guerrilla, 2 VC
  Underground Guerrillas`, then `How many NVA Troops (0 - 2):` and so on in
  order, filling the remainder from the last type automatically;
- it costs no Resources and shifts no Support;
- the piece it flips Active is then exposed — an Active Irregular was Ambushed
  the same card. It also stops flipping back until the Coup Reset, which
  disarms the space for the rest of the campaign: in TestGame3 the Irregulars
  in Da Nang and Binh Dinh were Active for six cards and no removal was
  possible there.
Afterwards: `Do you wish to add +6 Aid? (y/n)`.

The other two Advise options, both now used:
- **`Sweep a space with ARVN forces`** only Activates Guerrillas in the space,
  with no movement and no roll. It is worth an Advise slot on its own: the NVA
  bot's Terror trigger is `Underground NVA Guerrillas in space with Support?`,
  so Activating the Guerrillas sitting in your Support spaces switches that
  branch off until the Coup Reset flips them back.
- **`Assault a space with ARVN forces`** prints a numbered list of every space
  where ARVN cubes face removable enemies, including LoCs. In TestGame3, Hue
  with **2 ARVN Troops and 4 Police (6 cubes) in a City inflicted 3 hits** and
  removed a VC Base that had no Guerrilla left to shield it — so an undefended
  Base is a legal Assault target, and a City gives roughly one hit per two ARVN
  cubes. TestGame1's 2 Police in Highland inflicted 0, so terrain matters.
  ~~**Removing an insurgent Base pays +6 Aid on top of Advise's own +6**~~:
  `Each insurgent base removed adds +6 Aid` fired there for an **ARVN
  Assault** through Advise. In TestGame4 (card #17) an **Irregular/Ranger
  removal** of a VC Base printed no such line and Aid moved only by
  Advise's own +6; the Base bonus attaches to Assault removals, not to the
  Irregular/Ranger removal. Either way an undefended Base is a legal target
  and the removal costs no Resources and no US piece.

**Air Lift.** ~~Not used.~~ Select up to 4 spaces (bare prompt, typed names),
then `Lift forces out of <space>` to any other selected space; the prompt
offers `Air Lift US Troops` and, where present, `Air Lift ARVN Troops`
(Irregulars/Rangers presumably likewise, not tested), then a count. **No
adjacency limit** — Da Nang and Kontum lifted straight into IV Corps — and
**map-to-map only**: it cannot reach into Available, so it costs no US points.
Moving 2 Troops into a space with one Guerrilla gave COIN Control at once and
the control change and score markers printed inside the Air Lift. Medevac
shaded forbids it until the Coup (TestGame1).

**Air Strike.** Still never resolved. Banned for most of TestGame2 (the shaded
Da Nang momentum, then the shaded Rolling Thunder momentum), and the Special
Activity menu simply omits it with a `Notes: Momentum: #22 Da Nang prohibits
Air Strike` line. Opened once by accident in TestGame3 and aborted, which
showed the opening: **the hit die is rolled the moment the activity starts**
(`US chooses Air Strike special activity / Die roll to determine the number of
hits = 3`), then `0 spaces of 6 selected for Air Strike`, a `You have not yet
degraded the trail` reminder, and
`Air Strike: (3 hits remaining, remove up to 3 pieces) 1) Select a space to
Strike 2) Degrade the trail 3) Finished with Air Strike activity`. Aborting
there rolled nothing back because nothing had happened.
TestGame1: up to 6 spaces (2 in Monsoon); a struck space must contain COIN
pieces except one per strike under Arc Light; removes NVA Troops and Active
Guerrillas only; "Degrade the trail" costs 2 hits; **each populated struck
space shifts one level toward Active Opposition**, which is why it stayed
unused in two games where the VC was the faction to beat. Use it on Laos and
Cambodia, where the population is 0 and the shift cannot bite.

## 5. Events and capabilities, mechanically

- Dual events: you choose Unshaded or Shaded. Single events have one text.
- A **capability** persists across Coups (TestGame2: Booby Traps shaded, Main
  Force Bns shaded, both VC). A **momentum** is removed at the Coup Reset
  (Medevac unshaded, Da Nang shaded, Rolling Thunder shaded).
- "Remove Support" sets the space to Neutral whatever its level (Da Nang
  shaded removed Active Support; Fact Finding shaded removed Passive Support).
  "Shift 1 level toward Active Opposition" moves one step (Burning Bonze
  shaded took Saigon from Active to Passive Support: -6).
- "Place any 1 VC piece" lets the bot place **Bases** (Korean War Arms shaded:
  three VC Bases in one card, +3 VC).
- "Pacifies as if Support Phase" (Honolulu Conference) applies the Support
  phase's strict test (section 6), not Train's loose one.
- Events that remove US Troops send them to Casualties (`US to Casualties`);
  ARVN pieces removed go to ARVN Available.
- "Remove pieces" events count untunneled Bases as pieces (TestGame1:
  Tribesmen). Event-driven moves of US pieces to Available do not trigger the
  Commitment withdrawal penalty (TestGame1: Senator Fulbright).
- A **pivotal event replaces the current card outright**, and the replaced card
  is never played. That is half the value of playing one: TestGame3's
  Linebacker II erased a VC Critical card aimed at four Police-held Support
  spaces, and the NVA's Easter Offensive erased a VC Critical card aimed at
  Da Nang. Check what you are deleting as well as what you are casting.
- Events that bring pieces from **Out of Play** ask per space and per piece
  type: a bare `Place pieces in which space:` (typed names), then
  `Do you wish to place a base in <space>? (y/n)`. Out-of-Play pieces score
  nothing, so placing them on the map is free US points in waiting; Available
  pieces already score, so moving *those* to the map costs a point each.
- When an event makes the US lose pieces, **the US chooses which** (`Select 3
  pieces among the following: 21 US Troops, 3 US Bases`). Take Troops and keep
  Bases: Troops come back from Out of Play through several events, and a Base
  is what lets Train place ARVN cubes in a Province.
- `Each insurgent base removed adds +6 Aid` fires from Assault removals
  (US, ARVN, or ARVN through Advise) and prints as its own line; **not**
  from Advise's Irregular/Ranger removal (TestGame4).

## 6. Coup round, phase by phase

1. **Victory** comes first, before anything else in the round. Any faction
   with score above 0 wins, highest first; ties go VC, ARVN, NVA, US. `Game
   over in the 3rd Coup! round / US wins with a victory margin of 4!` — so
   **nothing the Coup itself does (pacification, casualties returning) counts
   for that Coup's check; it all counts for the next one.** In TestGame2 that
   meant 12 Troops returning at Coup 2 were worth +12 only at Coup 3.
2. **Resources**: sabotage check, Trail-degrade check for COIN-controlled
   Laos/Cambodia spaces, ARVN earns Econ + Aid (`+41` with Econ 15 and Aid 26,
   computed **before** the deduction that follows), then **Aid drops by 3 per
   piece in the Casualties box** (12 Troops + 1 Irregular: `Decrease US Aid by
   -39 to 0`, floored at 0). **Econ is re-set each Coup from the unsabotaged
   LoCs**: `Set Econ marker to 13`, then 15, then 10 across TestGame3's three
   Coups as the VC's sabotage came and went. A low Econ is good for the US —
   it is the floor that Pacify must stay above — so the sabotage the VC does to
   spite ARVN's income also widens your pacification headroom.
3. **Support**: US pacifies first, up to 4 spaces, in spaces with **COIN
   Control, US Troops and ARVN Police** — the strict test; Irregulars do not
   count as Troops here, and a space with Troops but no Police is refused.
   Prompt: `US Pacification (4 spaces remaining, 72 ARVN resources, Econ is
   15)`; with no eligible space it prints `US does not pacify any spaces`
   without asking. Up to 2 levels per space as one menu entry. Then ARVN
   pacifies (it took Qui Nhon from Passive Opposition to Passive Support in
   one go), then the VC spends its Agitate Total, 1 per level (both spaces it
   chose held VC Guerrillas).
4. **Redeploy**: ARVN behaviour varied — at Coup 1 it moved Police *out of*
   Cities *into* contested Provinces (a gift); at Coup 2 it pulled Troops off
   LoCs and out of a contested Province into Saigon. NVA rolls `3d6 for number
   of troops per destination` and may move Troops **from Laos/North Vietnam
   into South Vietnam** — it took Binh Dinh back and +2 that way, after the
   Victory check.
5. **Commitment**: Base casualties and one third of Troop casualties go Out of
   Play, Irregular casualties to Available; under **Medevac unshaded** all
   Troop casualties go to Available instead (`US Troops in the Casualties box
   move to available: [Momentum: #15 Medevac (unshaded)]`). **The remaining
   Troop casualties are then placed on the map by you**, a step TestGame2 never
   saw because its casualties all went Out of Play or to Available:
   `ROTATION: Place the remaining US Troop Casualties on the map / 4 Troop
   casualties remaining to place on the map`, with a numbered list of every
   COIN-controlled space, every LoC and Saigon, asking a count per space. With
   2 Troops in the box none went Out of Play and both were placed; with 5
   Troops and 2 Irregulars, 1 Troop went Out of Play, both Irregulars went to
   Available and 4 Troops were placed. These arrive free, so casualties are
   not a pure loss: they are a redeployment you control, and Aid has already
   been charged for them in the Resources phase. **Each Troop placed this way
   reduces the move allowance that follows**, which read `up to 8` after two
   placements and `up to 6` after four. Then `Move up to 10 US Troops and up to
   2 bases among Available box, COIN controlled spaces, LoCs and Saigon`: the prompt asks the **source** first (Available plus spaces
   already holding US Troops), then the destination from a list of every
   COIN-controlled space, every LoC and Saigon — an Uncontrolled space is not
   on it. **This is the only way pieces leave Available**; Air Lift cannot.
   Each piece moved out costs 1 US point. Withdrawal: for every 2 US pieces
   moved to Available the VC shifts 1 population one level toward Active
   Opposition; the prompt prints even for 0 pieces.
6. **Reset**: the Trail was improved from 0 to 1 (TestGame1 and again in
   TestGame3) and degraded from 4 to 3 (TestGame2 and TestGame3) — four data
   points, consistent with "toward the middle" — one terror marker per space
   removed (TestGame3 Coup 3 cleared a single marker, not all of them), all Active Guerrillas **and Active US
   Irregulars and ARVN Rangers** flip Underground, momentum removed, all
   factions Eligible, Agitate Total set by d3, Tru'ng deck reshuffled.

The Coup card goes into the RVN Leader box "on top of the stack", and the
**count of cards in that box is the bots' pivotal-event roll target**, so each
Coup makes every pivotal one point more likely: Duong Van Minh does not count,
and at three cards the VC's Tet Offensive came up on a 2. Leader effects seen:
Nguyen Khanh (Transport max 1 LoC space; pacify 3), Nguyen Van Thieu (no effect
printed; pacify 3), Nguyen Cao Ky (pacification 4 per level, TestGame1 and
TestGame3), Young Turks (no effect printed; pacify 3), Failed Attempt (ARVN
removes 1 in 3 cubes per space, TestGame1). The cost line names the leader when
one applies: `The cost to pacify is 4 per level/terror marker [Leader: Nguyen
Cao Ky]`.

## 7. Scoring and control facts

- US = Total Support + US Troops and Bases in Available. Irregulars, Casualties
  and Out of Play count nothing. Active Support is population x2, Passive x1.
- VC = Total Opposition (same doubling) + VC Bases on the map. Guerrillas count
  nothing, so removing them changes the VC score only through Control.
- NVA = NVA Control (population) + NVA Bases anywhere on the map. Six pop-2
  Controls and 7 Bases put it at 19 = +1 twice in TestGame2; one Control break
  (-2) undid it each time.
- ARVN = COIN Control (population) + Patronage. **Every COIN Control you
  create is ARVN score**: taking Kien Hoa-Vinh Binh moved ARVN 46 -> 48.
- Control needs strictly more pieces than every other faction combined; at
  equality the marker comes off (NVA 6 v COIN 6 in Binh Dinh). A Base counts
  as a piece for this.
- **Support and Opposition persist through changes of Control** — Quang Tri
  kept Passive Support under NVA Control; Kien Hoa kept its Neutral and then
  its Passive Support after losing Control. Control matters only at the
  instant of pacification. Only Terror, Agitate, Govern and events move the
  marker downward.
- Pacifying an Opposition space is a double swing: Active Opposition -> Neutral
  is -4 VC at pop 2, and the next two levels are +4 US.
- Terror markers show in the render as `terror 1` and cost a level each to
  pacify through.

## 8. What the bots did (their operations, as narrated)

The Tru'ng narration prints the bot's checks; these were reliable predictors.

**NVA.** `Trung: NVA - S`, `Any 2-Pop space without COIN Control?` -> Rally
(place Guerrillas, or place a Base by removing 2 Guerrillas), then `improves
the trail` by 1 (`No trail improvement. The Trail is at 4.` at the cap), then
Infiltrate (Troops into Laos/North Vietnam, or **replace a VC Base with an NVA
Base** in a shared space). `Trung: NVA - N/NN`, `8+ NVA Troops in a space
outside the South?` -> Infiltrate then **March**: 20 Troops left Laos in one
card into three Provinces, with activation rolls between destinations.
`Trung: NVA - T`, `6+ NVA Troops in any space with COIN Troops or COIN Base?`
-> **Attack with Troops**: removed every US Troop in the space (2, then 4),
never the Irregulars or Police beside them, and lost the same number of NVA
Troops to Attrition; then Ambush from an adjacent LoC (`Ambushes in LOC Kontum
-- Dak To, targeting Binh Dinh`, 1 Active piece removed). `Trung: NVA - R/RR`,
`Underground NVA Guerrillas in space with Support?` -> **Terror**: flips one
Guerrilla Active, adds a terror marker, drops Support one level (Passive ->
Neutral), and it ran through six spaces in one Op. Its Special Activity
whenever `3d6 <= Available NVA Troops` failed (four times, paired with March
or Terror) was **Bombard**: 1 Troop removed from each of 2 spaces, every one
of them a space holding no NVA piece at all (Saigon, Hue, Pleiku, Kien Hoa;
US Troops to Casualties, ARVN Troops to Available). Its Redeploy is described
in section 6.
TestGame3 added two branches. `Trung: NVA - R` opens with
**`Support + Available >= 42?`** — that is *your* score marker, so leading the
game is itself the trigger that turns the NVA toward you; it fired on five
separate cards once the US passed 42 and produced Marches into South Vietnam
and Bombards against Saigon. `Trung: NVA - Q/QQ` ran
`2d6 <= Available NVA Guerrillas`, then `d3 >= the Trail`, then the Attack
check, so a **low Trail makes the NVA Rally rather than Attack**. When a
branch cannot be executed the program says so and draws again
(`No spaces found for NVA Attack / The operation for Trung: NVA - Q would be
ineffective.`), which is a free look at the bot's whole priority list.
**At Trail 4 the NVA Marches for free outside South Vietnam** (Kevin's note):
that is how a stack in the Parrot's Beak crossed the map into Quang Tin in one
March. Degrading the Trail is worth more than its one box of NVA score.

**VC.** Critical/Performed shaded events whenever reachable. `Trung: VC - W`,
`Underground VC Guerrillas in space with US Troops?` -> Rally (4 Guerrillas
into a Base space at a time) then **Subvert** when `Patronage >= 17`: in each
of 2 spaces, remove an ARVN Police and place a VC Guerrilla, then Patronage -1
— this is what undid a COIN Control I had built on ARVN Police. `Trung: VC -
V/VV`, `3+ VC Guerrillas in any spaces with US Troops and no VC Base?` ->
**Attack**: `Die roll 3 Guerrillas): 1 [Success!]`, flips the Guerrillas
Active, removes 2 US Troops, loses 2 Guerrillas to Attrition. Agitate in the
Coup as in section 6. A VC space with only a Base and no Guerrillas is a free
Advise target — and in TestGame3 an Attack that lost both its Guerrillas to
Attrition created exactly that, a Base in Hue with nothing left to shield it,
killed the same turn by Advise's ARVN Assault.
TestGame3's VC ran on **Tax** (`Trung: VC - Z`, `15+ VC Guerrillas on the
map?`; `Spaces exist that can be Taxed?` and `2d6 > Agitate Total`): each Tax
flips a Guerrilla Active, shifts the space **one level toward Support** and
adds 2 to the Agitate Total (1 on a LoC). That looks like a gift and is not:
it converts board Opposition, which you can pacify away, into an Agitate Total
that is spent in the Coup Support phase **after** the Victory check, where you
cannot answer it. The VC banked 18 that way and cashed 8 of it at Coup 3.
`Trung: VC - U`, `3+ VC Guerrillas in any space?` and `Underground VC
Guerrillas in space not at Active Opposition?` -> **Terror**; `Trung: VC - X`,
`Any 2+ Pop space without VC Guerrillas?` -> Rally; `Trung: VC - Y/YY` and
`Trung: VC - Z` -> Rally or March.

**ARVN.** Train (3 Troops + 3 Police into Saigon and Hue, 3 Resources each,
activation roll against 3), Patrol as in section 3, **Govern** (`Transfer
population value from Aid to Patronage`: Aid -pop, Patronage +pop, and the
space's Active Support **flips to Passive** — one level, not removal; needs a
COIN-controlled space with ARVN cubes outside Saigon; with Aid at 0 there is
nothing to transfer, but whether the program then skips Govern is **untested**
— ARVN spent the only such window on its pivotal), **Transport** when `5+ ARVN Troops + Rangers in any
one space` (moved 2 Troops + 2 Rangers to an adjacent Province, then `Flip
all Rangers underground`), Redeploy as in section 6, and its pivotal at the
first draw where it qualified. It passed once when it was sole eligible with
only a Performed marking.
TestGame3 added **Raid** (a Ranger moves in from an adjacent space, flips
Active and removes up to 2 pieces including an undefended Base — the same
removal the US gets from Advise) and showed the chain that does the US most
harm: `Trung: ARVN - M`, `NVA Control + NVA Bases >= 14?` -> `3d6 <= Available
ARVN pieces` -> on failure `Trung: ARVN - MM`, `All routes from Can Tho to Hue
blocked?` -> **Patrol, then Govern**. Two lessons. **Govern arrived through
the Patrol branch even though the Available-pieces check had failed**, so
emptying ARVN's Available box (by Training its cubes onto the map) only closes
*some* of the doors to Govern, not all. And the Can Tho-to-Hue route test means
**enemy pieces sitting on your LoCs steer ARVN into Patrol**, which in
TestGame3 emptied Saigon of every ARVN cube twice and cost COIN Control there.
Govern took 8 points of US Support in two cards at pop-2 spaces; it needs ARVN
cubes in the space, so Support built where only US pieces stand is immune.

- The Trail: NVA Rally improves it 1 box per Rally (2 under SA-2s in
  TestGame1); Air Strike degrades it 1 box for 2 hits; at Reset it moves toward
  the middle (0 -> 1, 4 -> 3). **At 4 the NVA Marches free outside South
  Vietnam**, which turns its Laos and Cambodia sanctuaries into one connected
  staging area; at 0-1 it Rallies instead of Attacking. ARVN's unshaded
  Rolling Thunder and Wild Weasels each degraded it 2 boxes for me.
- The Agitate Total is not score; Tax adds to it (not seen from the VC in
  TestGame2) and the Coup Support phase spends it.
