# Fire in the Lake, US faction: what the program taught me

> **Harness notes.** Read these first; some habits recorded in earlier
> versions of this file have been replaced by tools.
>
> - **Event cards** are drawn by the harness: `ctl.py advance` answers the
>   card prompt with a fresh random draw and prints `[deck] ... -> drew #N`.
>   The deck is built as the rules say (one 1964 pile, two 1965 piles, three
>   1968 piles, 12 events plus a Coup card each); which cards appear is
>   unknown to everyone until drawn. `ctl.py send` refuses a card prompt.
> - **`advance` does three things in one call**: runs the bots, writes the
>   report file for every card it finishes (`wrote reports/...`), and prints
>   the **briefing** when it stops at the US turn: the board view, both
>   cards' full text and Tru'ng markings, scores, sequence of play, and the
>   neighbours of every space with US pieces. `ctl.py brief` prints it again
>   on demand (with this card's narration so far). There is no need to run
>   `render.py`, grep the transcript, look cards up in `cards.json` or call
>   `map.py` for your own spaces before a decision.
> - **`ctl.py commit-turn "<notes line>"`** ends a card: it appends the line
>   to `notes.md`, writes any report not yet written, commits with the line
>   as the message and pushes.
> - **Answering prompts.** `ctl.py seq "<expected>=><answer>" ...` sends a
>   whole action's answers in one call, each sent only if `<expected>` is in
>   the current prompt. Answers are matched by label when the prompt is a
>   numbered menu and typed as given when it is bare: write `Saigon`,
>   `Train`, `Finished selecting`, never a number, whichever form the program
>   uses this time. After a rejected answer the re-prompted menu is still
>   matched. `*` as the expected text matches any numbered menu (the label is
>   then the guard). **`PROMPTS.md`** lists every prompt chain seen so far,
>   with each prompt's form; write the `seq` from it.
> - **Reports.** `tools/report.py` writes the observer's report from the
>   program's own log files (narration verbatim, then the board summary) to
>   `reports/<game>/`. `advance` runs it for you at every card draw.
> - **The map.** `python3 tools/map.py <space>` lists a space's neighbours
>   and `map.py <a> <b>` says whether two spaces touch, from the program's
>   own table. Do not work from a remembered map.
> - **Program build 1.53+harness.** One program bug is known and unfixed:
>   after a **Limited Op Patrol whose destination is a City**, the program
>   offers (and with one candidate, executes without asking) the free
>   Assault in that City. Rule 3.2.2 allows it only in a LoC. Decline it
>   (`Do not Assault at one LOC`), and never plan on it.
> - **Tool calls are logged** by a hook to a file outside the tree; it
>   changes nothing.

Observed at the program's own prompts or in its narration over four games;
descriptive, not advice. Where a statement is an inference rather than an
observation, it says so.

**Still unobserved after four games:** Air Strike carried through to a hit
(the menu has been opened and aborted, never resolved); Sweep activation
ratios outside Lowland; the "add an ARVN Assault" option inside a US Assault;
Train's forced removal of ARVN cubes from the map when Available is short of
6. A US Patrol prints no Resource deduction: it is free.

## 1. Driving the program

- `python3 tools/ctl.py send <text>` types one answer and prints the reply.
  `advance` runs bot turns and Coup phases until a prompt needs you (it
  draws cards itself). `screen` prints the current prompt with its menu.
  `seq` answers a whole chain of prompts, each guarded (see the harness
  notes at the top).
- **Menus renumber**, in three ways: a chosen space drops out of a space
  list; an option that is not currently legal is simply omitted (the final
  Train menu drops Pacify when no selected space can be pacified, the
  Special Activity menu drops Air Strike while a ban is in force, Advise
  drops the removal option once no space qualifies); and the first-eligible
  and second-eligible action menus have different shapes. Answer by label,
  never by a remembered number.
- **The same space prompt is sometimes bare and sometimes numbered.**
  `Train in which space:`, `Air Lift in which space:`, `Select destination:`
  and `Sweep in which space:` have each arrived both as a bare prompt that
  takes a typed name and as a numbered menu, at which a typed name is
  rejected (`'Saigon' is not valid. Must be one of: 1, 2, ..., or abort`).
  There is no way to tell in advance; `seq` sends the right form.
- When exactly one space is legal the program selects it and executes at
  once: choosing "Use Irregular/Ranger to remove enemy pieces" with one
  qualifying space prints `Use Irregular/Ranger in which space:  Binh Dinh`
  and removes the pieces without a further prompt. Peeking at an option can
  commit it.
- The action menu shapes: first eligible `1) Event  2) Op (May add a Special
  Activity)  3) Pass`; second eligible after an Event `1) Op (May add a
  Special Activity)  2) Pass`; second eligible after an Op + Special Activity
  `1) Event  2) Limited Op  3) Pass`; second eligible after an **Op Only**
  `1) Limited Op  2) Pass`, the Event closed. A bot's Op Only therefore
  removes both the Event and any Special Activity from the faction behind
  it. The same works for you: a US **Op Only** (`n` to `Do you wish to
  perform a special activity? (y/n)`, which prints `Move the US cylinder to
  the Op Only box`) closes the Event to the whole second-eligible slot, at
  the cost of the Special Activity only. The slot passes down a pass: after
  an Event by the first actor and a pass by the second faction, the third
  still gets the full second-eligible menu.
- A Limited Op is a single space with no Special Activity, but a Limited Op
  Train still offers the final Train action (Pacify / Transfer patronage)
  for that one space. **The Limited Op skips the "Finished selecting spaces"
  step**: the final Train menu appears immediately after the one space's
  placement choice. **A Limited Op Patrol funnels every move into one
  destination**: `Select destination:` is asked once and every later `Move
  cubes` goes there without asking. **A Limited Op Sweep does move Troops**:
  `US Sweep space` -> `Sweep in which space` -> `US Sweep Troops into
  <space>` -> `US Move troops to <space> from` (adjacent spaces holding US
  Troops) -> a count.
- **abort has two scopes.** Sent inside a Special Activity it aborts only
  that Special Activity (`>>>> Aborting Air Strike special activity <<<< /
  No changes need to be made to the game board`) and returns to the
  operation's own menu. Sent at an operation menu, `abort` then `y` aborts
  the whole action with no state change, and the program prints the full
  reversal for the physical board (`The following changes should be made to
  the game board`, a `Remove from <space> to Available:` block, a `Changes
  to <space>:` block per space, a status block per space and the Available
  list). abort is rejected at some sub-prompts: at the Pacify level menu it
  prints `'abort' is not valid. Must be one of: 1 or 2`; answer "Do not
  pacify" and abort at the menu above.
- `?` at `(perform or ?)` lists perform, show, history, rollback, inspect,
  adjust, help, quit. `show summary` prints scores, resources, Aid,
  Patronage, Trail, leader, cards drawn.
- The patched build saves after every faction action, each card draw, each
  pivotal substitution, and once for a whole Coup round. A lost container is
  recovered by `ctl.py resume <game>`, which reloads the latest save and
  returns to the same prompt with nothing replayed; a loss in the middle of
  an action rolls the half-entered action back, as an abort would. Two
  consequences: during a Coup round `render.py` shows the pre-Coup save, so
  read the phase results from the narration; and `transcript.log` restarts
  on resume, but `report.py` builds the report from the saved log files, so
  nothing is lost with it.
- The game-end prompt is `Do you want to continue playing this game? (y/n)`;
  `n` prints `>>> The game has ended <<<` and drops to `(quit or ?)`.

## 2. Sequence of play, as observed

- The card names an order of four factions. A card ends when two factions
  have acted, or when every eligible faction has acted or passed. Passing
  keeps you Eligible and pays +3 ARVN Resources (for US or ARVN). After the
  first eligible passes, the next faction in order is treated as first
  eligible (inferred). If every eligible faction passes, the card resolves
  with nothing happening and everyone stays Eligible.
- **Turn order is the only reliable way to guarantee yourself an action.**
  If the factions ahead of you in the next card's order are all Ineligible,
  your action there is certain; if it depends on a bot choosing to act (so
  that it becomes Ineligible), it is not.
- Acting makes you Ineligible on the next card. Some events extend this:
  Henry Cabot Lodge shaded prints `ARVN is ineligible through the next card`
  and the sequence display shows `ARVN(-) -> Event`.
- Events that say "stay Eligible" do exactly that (Claymores unshaded,
  Medevac shaded).
- After a Coup round every faction is Eligible.
- **Tru'ng markings (Critical / Performed / Ignored, with a side) as a
  predictor.** Critical: taken every time it was reachable. Performed:
  usually taken, but it is a preference, not a commitment; a sole-eligible
  bot marked Performed has passed and banked +3 instead. Ignored: an Op
  every time. A bot marked for the shaded side takes the unshaded side if
  that is what is left, even when that removes enemy pieces or denies a bot
  ally the shaded text: bots do not coordinate. A bot marked for a side you
  also want is, for that card, on your side.
- **Pivotal events.** At a card draw the program rolls for the bots
  (`VC Bot Pivotal Event die roll: 5 [Failure] (2 cards in leader box)`,
  `ARVN Bot Pivotal Event die roll: 1 [Success] (2 cards in leader box)`);
  success needs a roll no higher than the number of cards in the leader box,
  and Duong Van Minh does not count as a card. A successful pivotal
  **replaces the current card** (`Replace the current event card with #123 -
  Vietnamization`), the playing faction acts first, and the others follow in
  the pivotal's own order with everyone Eligible. ARVN's Vietnamization needs
  fewer than 20 US Troops on the map. The US prompt reads `Pivotal Events can
  be played / Eligible: ARVN, NVA, and US / Trumped: ARVN and NVA / Does US
  wish to play their pivotal?`: it lists which factions are eligible and
  which the US pivotal trumps; a bot's failed roll at the same draw does not
  close it; answering `1` replaces the current card and `perform` then
  executes the event with no further menu. The prompt has not appeared on a
  Monsoon card with a Coup on deck, and on one occasion did not appear
  although the US seemed to qualify while a bot's roll succeeded; whether a
  bot's success pre-empts the human prompt is unresolved. Tet Offensive,
  once its roll succeeds, is the most destructive card in the game: nine
  free Terrors, a Base and two Guerrillas into each of two Cities, then free
  Attacks everywhere.
- **Monsoon** (the card before a Coup): Sweep prohibited as an Op (the
  operation menu prints `Sweep is prohibited [Not allowed in Monsoon]` and
  lists `1) Train 2) Patrol 3) Assault`; Advise's option list drops `Sweep a
  space with ARVN forces` too); Air Strike limited to 2 spaces; an event's
  free Sweep is still allowed.
- The render's "13 cards per campaign" is nominal: the number of event cards
  before a Coup varies widely (two to sixteen seen).

## 3. US Operations

**Train.** The space list is every space holding **any US piece**: Troops,
Irregulars, or a Base. In each selected space:
- with a US Base present: `Place Irregulars / Place Rangers / Place ARVN
  Troops/Police / Do not place forces`. ARVN cubes are up to 6 in total
  (`Troops (0 - 6)`, then `Police (0 - 4)` after 2 Troops) and cost 3 ARVN
  Resources for the space; Rangers cost 3 too. **Saigon is not special**:
  without a US Base it offers only `Place Irregulars / Do not place forces`;
- without a US Base: `Place Irregulars / Do not place forces` only;
- **the cube option is also gated by ARVN Resources exceeding Econ**, the
  same test as Pacify;
- **Kevin's note, not yet seen at a prompt:** US Train may place up to 6
  ARVN cubes *regardless of what is in the ARVN Available box*, taking the
  excess from anywhere on the map. This is how the US moves ARVN cubes out
  of the Saigon and Hue garrisons the bot piles up, and the fastest way to
  empty ARVN's Available box, which is one gate on its Govern activity;
- **Irregular placement costs nothing.** The cap is 2 per space and the
  prompt's upper bound is Available *plus* voluntary removals: asking for 2
  with 1 Available prints `There are not enough US Irregulars in the
  available box / You must remove 1 US Irregular from the map` and a menu of
  spaces to take one from. Answer with the same space to net +1 harmlessly.
- "Do not place forces" costs nothing and still counts the space as trained.
Final action, in **one** selected space:
- **Pacify.** Requires only that the space be COIN-controlled and one of the
  selected Train spaces (Irregulars and Police alone suffice; US Troops with
  no ARVN Police suffice). Up to 2 levels, 3 Resources per level under Duong
  Van Minh, Nguyen Khanh and Nguyen Van Thieu, 4 under Nguyen Cao Ky. It
  works from Opposition: `Shift 2 levels to Neutral` from Active Opposition,
  `Shift 2 levels to Passive Support` from Passive Opposition; the menu
  offers the whole shift as one entry. Refused when ARVN Resources do not
  exceed Econ (`Only 12 ARVN resources available and Econ is 15`). Absent
  from the menu when no selected space has a level to gain.
  - **Removing a terror marker does not count against the 2-level cap.**
    A space at Passive Opposition with one terror marker offers `1) Remove 1
    terror marker and shift 2 levels to Passive Support`, three steps for 9
    Resources. Always read the menu: the whole swing may be one entry.
  - **The number of levels offered depends on the Resource headroom above
    Econ.** At 18 Resources against Econ 13 only `Shift 1 level` is offered
    (two levels would leave 12, below Econ). Plan pacification against the
    headroom, not the total.
- **Transfer patronage to ARVN resources.** Offered only when Saigon is one
  of the selected Train spaces (also in a Limited Op Train of Saigon). The
  prompt is `Transfer how much patronage to ARVN resources (0 - 3)`: **capped
  at 3, one for one**, Patronage down and ARVN Resources up. A small,
  reliable 3 points off ARVN's score that also lifts its Resources back over
  the Econ floor; it is offered with Pacify absent whenever Resources are at
  or below Econ.
- A space used for Train cannot also be used by Advise in the same action,
  and vice versa; a space used by Advise disappears from the Train list. Air
  Lift has no such restriction, in either order.

**Assault.** Flow: `US Assault: 1) Select a space to Assault 2) Perform a
Special Activity 3) Finished selecting spaces`, then a numbered list of the
spaces that qualify; several spaces may be assaulted in one Op, and when only
one remains the program names and resolves it without a prompt (`Assault in
which space:  Da Nang`), ending with `There are no more spaces eligible for
Assault`. It costs the US no Resources. Only spaces with US Troops and
removable enemies are offered; it removes NVA Troops and Active Guerrillas,
Bases last.
Hits observed: 2 US Troops in Saigon with a US Base, 4 hits; 2 cubes in
Highland, 1 hit; 1 US Troop with a US Base in Highland, 2 hits; 1 US Troop in
a City, 1 hit. A US Base in the space roughly doubles the count.
**Underground Guerrillas shield a Base from Assault**: a space holding a VC
Base, 1 Underground VC Guerrilla and 3 US Troops is simply not on the Assault
list; a Sweep to Activate that Guerrilla is the way in. An *undefended* Base
is a legal target. The "add an ARVN Assault at cost 0" option the card tips
mention has never been prompted.

**Sweep.** The flow:
- `US Sweep space: 1) Select a Sweep space 2) Perform a Special Activity
  3) Finished selecting Sweep spaces`, then the space prompt (bare or
  numbered). Any number of spaces may be selected before anything moves, and
  a selected space with no Troops moved in still resolves (a Limited Op
  Sweep in place just prints `Flip 1 VC Underground Guerrilla in Saigon to
  ACTIVE` and ends).
- Then `US Sweep Troops into: <each selected space>`, and per destination
  `US Move troops to <space> from:` listing the **adjacent** spaces that hold
  US Troops; nothing further away is listed, so movement is one space.
- **Only US Troops move.** ARVN Troops in the same source spaces are not
  offered, so a US Sweep cannot reposition ARVN cubes (Air Lift and Train are
  the tools for that). A source stays on the list after moving 0.
- Then `Sweep activation:` with `1) Resolve all remaining Sweep spaces
  2) Perform a Special Activity 3) Resolve Sweep in <space>` per space, so
  spaces resolve one at a time. 3 US Troops moved into a Lowland Province
  flipped 3 Underground Guerrillas Active, one per Troop, with the ARVN cubes
  already in the space adding nothing. Ratios in Highland, Jungle and City
  are untested.
- Sweep is prohibited in Monsoon, and the VC's Booby Traps shaded capability
  (`Each Sweep space, VC afterward removes 1 Sweeping Troop on roll of 1-3,
  US to Casualties`) makes it expensive while in play.
Advise's "Sweep a space with ARVN forces" is a different thing: it only
Activates Guerrillas in place, and no cube movement is offered.

**Patrol.** The flow:
- `US Moving Patrol cubes: 1) Move cubes 2) Perform a Special Activity
  3) Finished moving cubes`, then `Move cubes out of which space:` listing
  every space holding US cubes.
- Per source: `These cubes can move: 3 US Troops` (US cubes only; ARVN Police
  in the same space are not offered), then a count, then `Select
  destination:` (bare or numbered).
- **Destinations are LoCs and Cities only, reachable from the source along a
  chain of adjacent LoCs and Cities**, which ends at the first space holding
  an NVA or VC piece. From Saigon the list spans most of the map because
  Saigon's LoC network does; from Kien Hoa-Vinh Binh it is Can Tho, four
  LoCs and Saigon. Typing a Province is rejected with the legal list.
- After `Finished moving cubes`: `US Patrol - Activating guerrillas on LOCs`,
  then `Choose one: 1) Assault at one LOC 2) Perform a Special Activity
  3) Do not Assault at one LOC`. The free Assault at a LoC holding 1 US Troop
  and 3 ARVN Police `inflicts 1 hit`: the US cube alone counts, not the ARVN
  Police beside it. **The `Assault at one LOC` entry appears only when a LoC
  holds your cubes**; when it appears after a Limited Op Patrol into a City
  it is the program bug in the harness notes. Decline it.
- No Resource deduction is printed: a US Patrol is free. ARVN pays 3 for its
  own.
ARVN's Patrol: cubes from Saigon onto LoCs, Guerrillas Activated on each
destination LoC, then one Assault on a LoC. It can empty Saigon of every ARVN
cube, which costs COIN Control there.

## 4. US Special Activities

**Advise.** Up to 2 spaces. The option list is built from what is legal:
`Sweep a space with ARVN forces`, `Assault a space with ARVN forces`, `Use
Irregular/Ranger to remove enemy pieces`, and options vanish once used up.
The removal is the best tool the US has:
- it needs an **Underground** US Irregular or ARVN Ranger in the space (ARVN
  Rangers count), flips that piece Active, and removes **2 enemy pieces**;
- it removes Underground Guerrillas, Active Guerrillas, NVA Troops, and an
  **undefended Base**. Bases are last: while other enemy pieces stand in the
  space the Base is not on the list;
- when several piece types are present it lets you choose: `Select 2 pieces
  among the following: 5 NVA Troops, 1 NVA Underground Guerrilla, 2 VC
  Underground Guerrillas`, then `How many NVA Troops (0 - 2):` and so on in
  order, filling the remainder from the last type automatically;
- it costs no Resources and shifts no Support;
- the piece it flips Active is then exposed to Ambush, and it stays Active
  until the Coup Reset, which disarms the space for the rest of the
  campaign: no further removal is possible there until the piece flips back.
Afterwards: `Do you wish to add +6 Aid? (y/n)`.

The other two Advise options:
- **`Sweep a space with ARVN forces`** only Activates Guerrillas in the
  space, with no movement and no roll. It is worth an Advise slot on its
  own: the NVA bot's Terror trigger is `Underground NVA Guerrillas in space
  with Support?`, so Activating the Guerrillas sitting in your Support spaces
  switches that branch off until the Coup Reset flips them back.
- **`Assault a space with ARVN forces`** prints a numbered list of every
  space where ARVN cubes face removable enemies, including LoCs. 2 ARVN
  Troops and 4 Police (6 cubes) in a City inflicted 3 hits and removed a VC
  Base that had no Guerrilla left to shield it: roughly one hit per two ARVN
  cubes in a City; 2 Police in Highland inflicted 0, so terrain matters.
  `Each insurgent base removed adds +6 Aid` fires for a Base removed by this
  ARVN Assault, and not for a Base removed by the Irregular/Ranger removal,
  which pays only Advise's own +6.

**Air Lift.** Select up to 4 spaces (`Air Lift in which space:`, bare or
numbered), then `Lift forces out of <space>` to any other selected space; the
prompt offers `Air Lift US Troops` and, where present, `Air Lift ARVN Troops`
(Irregulars/Rangers presumably likewise, not tested), then a count. **No
adjacency limit**, and **map-to-map only**: it cannot reach into Available,
so it costs no US points. Moving 2 Troops into a space with one Guerrilla
gives COIN Control at once, and the control change and score markers print
inside the Air Lift. Medevac shaded forbids it until the Coup.

**Air Strike.** Never resolved through to a hit. When a momentum prohibits it
the Special Activity menu simply omits it with a `Notes: Momentum: #22 Da
Nang prohibits Air Strike` line. The opening: **the hit die is rolled the
moment the activity starts** (`US chooses Air Strike special activity / Die
roll to determine the number of hits = 3`), then `0 spaces of 6 selected for
Air Strike`, a `You have not yet degraded the trail` reminder, and `Air
Strike: (3 hits remaining, remove up to 3 pieces) 1) Select a space to Strike
2) Degrade the trail 3) Finished with Air Strike activity`. Aborting there
rolls nothing back because nothing has happened. Up to 6 spaces (2 in
Monsoon); a struck space must contain COIN pieces except one per strike under
Arc Light; removes NVA Troops and Active Guerrillas only; "Degrade the trail"
costs 2 hits; **each populated struck space shifts one level toward Active
Opposition**. Laos and Cambodia have population 0, so the shift cannot bite
there.

## 5. Events and capabilities, mechanically

- Dual events: you choose Unshaded or Shaded. Single events have one text.
- A **capability** persists across Coups (Booby Traps shaded, Main Force Bns
  shaded). A **momentum** is removed at the Coup Reset (Medevac unshaded, Da
  Nang shaded, Rolling Thunder shaded).
- "Remove Support" sets the space to Neutral whatever its level (Da Nang
  shaded removed Active Support; Fact Finding shaded removed Passive
  Support). "Shift 1 level toward Active Opposition" moves one step (Burning
  Bonze shaded took Saigon from Active to Passive Support: -6).
- "Place any 1 VC piece" lets the bot place **Bases** (Korean War Arms
  shaded: three VC Bases in one card, +3 VC).
- "Pacifies as if Support Phase" (Honolulu Conference) applies the Support
  phase's strict test (section 6), not Train's loose one.
- Events that remove US Troops send them to Casualties (`US to
  Casualties`); ARVN pieces removed go to ARVN Available.
- "Remove pieces" events count untunneled Bases as pieces (Tribesmen).
  Event-driven moves of US pieces to Available do not trigger the Commitment
  withdrawal penalty (Senator Fulbright).
- A **pivotal event replaces the current card outright**, and the replaced
  card is never played. Half the value of playing one is what it deletes;
  check that as well as what you are casting.
- Events that bring pieces from **Out of Play** ask per space and per piece
  type: a bare `Place pieces in which space:` (typed names), then `Do you
  wish to place a base in <space>? (y/n)`. Out-of-Play pieces score nothing,
  so placing them on the map is free US points in waiting; Available pieces
  already score, so moving *those* to the map costs a point each.
- When an event makes the US lose pieces, **the US chooses which** (`Select 3
  pieces among the following: 21 US Troops, 3 US Bases`). Take Troops and
  keep Bases: Troops come back from Out of Play through several events, and
  a Base is what lets Train place ARVN cubes in a Province.
- `Each insurgent base removed adds +6 Aid` fires from Assault removals (US,
  ARVN, or ARVN through Advise) and prints as its own line; not from
  Advise's Irregular/Ranger removal.

## 6. Coup round, phase by phase

1. **Victory** comes first, before anything else in the round. Any faction
   with score above 0 wins, highest first; ties go VC, ARVN, NVA, US (`Game
   over in the 3rd Coup! round / US wins with a victory margin of 4!`).
   **Nothing the Coup itself does (pacification, casualties returning)
   counts for that Coup's check; it all counts for the next one.**
2. **Resources**: sabotage check, Trail-degrade check for COIN-controlled
   Laos/Cambodia spaces, ARVN earns Econ + Aid (`+41` with Econ 15 and Aid
   26, computed **before** the deduction that follows), then **Aid drops by 3
   per piece in the Casualties box** (12 Troops + 1 Irregular: `Decrease US
   Aid by -39 to 0`, floored at 0). **Econ is re-set each Coup from the
   unsabotaged LoCs** (`Set Econ marker to 13`). A low Econ is good for the
   US, since it is the floor that Pacify must stay above: the sabotage the
   VC does to spite ARVN's income widens your pacification headroom.
3. **Support**: US pacifies first, up to 4 spaces, in spaces with **COIN
   Control, US Troops and ARVN Police**, the strict test; Irregulars do not
   count as Troops here, and a space with Troops but no Police is refused.
   Prompt: `US Pacification (4 spaces remaining, 72 ARVN resources, Econ is
   15)`; with no eligible space it prints `US does not pacify any spaces`
   without asking. Up to 2 levels per space as one menu entry. Then ARVN
   pacifies (it can take a space from Passive Opposition to Passive Support
   in one go), then the VC spends its Agitate Total, 1 per level, in spaces
   holding VC Guerrillas.
4. **Redeploy**: ARVN behaviour varies: it has moved Police out of Cities
   into contested Provinces (a gift), and it has pulled Troops off LoCs and
   out of a contested Province into Saigon. NVA rolls `3d6 for number of
   troops per destination` and may move Troops from Laos/North Vietnam into
   South Vietnam, taking Control after the Victory check.
5. **Commitment**: Base casualties and one third of Troop casualties go Out
   of Play, Irregular casualties to Available; under **Medevac unshaded** all
   Troop casualties go to Available instead (`US Troops in the Casualties
   box move to available: [Momentum: #15 Medevac (unshaded)]`). **The
   remaining Troop casualties are then placed on the map by you**:
   `ROTATION: Place the remaining US Troop Casualties on the map / 4 Troop
   casualties remaining to place on the map`, with a numbered list of every
   COIN-controlled space, every LoC and Saigon, asking a count per space
   (with 2 Troops in the box none went Out of Play and both were placed;
   with 5 Troops and 2 Irregulars, 1 Troop went Out of Play, both
   Irregulars to Available, 4 Troops placed). These arrive free, so
   casualties are a redeployment you control, and Aid has already been
   charged for them in the Resources phase. **Each Troop placed this way
   reduces the move allowance that follows** (`up to 8` after two
   placements, `up to 6` after four). Then `Move up to 10 US Troops and up to
   2 bases among Available box, COIN controlled spaces, LoCs and Saigon`: the
   prompt asks the **source** first (Available plus spaces already holding
   US Troops), then the destination from a list of every COIN-controlled
   space, every LoC and Saigon; an Uncontrolled space is not on it. **This is
   the only way pieces leave Available**; Air Lift cannot. Each piece moved
   out costs 1 US point. Withdrawal: for every 2 US pieces moved to Available
   the VC shifts 1 population one level toward Active Opposition; the prompt
   prints even for 0 pieces.
6. **Reset**: the Trail moves toward the middle (0 -> 1, 4 -> 3); one terror
   marker per space is removed (not all of them); all Active Guerrillas
   **and Active US Irregulars and ARVN Rangers** flip Underground; momentum
   removed; all factions Eligible; Agitate Total set by d3; Tru'ng deck
   reshuffled.

The Coup card goes into the RVN Leader box "on top of the stack", and the
**count of cards in that box is the bots' pivotal-event roll target**, so
each Coup makes every pivotal one point more likely; Duong Van Minh does not
count. Leader effects seen: Nguyen Khanh (Transport max 1 LoC space; pacify
3), Nguyen Van Thieu (no effect printed; pacify 3), Nguyen Cao Ky
(pacification 4 per level), Young Turks (no effect printed; pacify 3), Failed
Attempt (ARVN removes 1 in 3 cubes per space). The cost line names the leader
when one applies: `The cost to pacify is 4 per level/terror marker [Leader:
Nguyen Cao Ky]`.

## 7. Scoring and control facts

- US = Total Support + US Troops and Bases in Available. Irregulars,
  Casualties and Out of Play count nothing. Active Support is population x2,
  Passive x1.
- VC = Total Opposition (same doubling) + VC Bases on the map. Guerrillas
  count nothing, so removing them changes the VC score only through Control.
- NVA = NVA Control (population) + NVA Bases anywhere on the map. Six pop-2
  Controls and 7 Bases is 19 = +1; one Control break (-2) undoes it.
- ARVN = COIN Control (population) + Patronage. **Every COIN Control you
  create is ARVN score.**
- Control needs strictly more pieces than every other faction combined; at
  equality the marker comes off (NVA 6 v COIN 6). A Base counts as a piece
  for this.
- **Support and Opposition persist through changes of Control.** Control
  matters only at the instant of pacification. Only Terror, Agitate, Govern
  and events move the marker downward.
- Pacifying an Opposition space is a double swing: Active Opposition ->
  Neutral is -4 VC at pop 2, and the next two levels are +4 US.
- Terror markers show in the render as `terror 1` and cost a level each to
  pacify through.

## 8. What the bots did (their operations, as narrated)

The Tru'ng narration prints the bot's checks; they are reliable predictors.

**NVA.** `Trung: NVA - S`, `Any 2-Pop space without COIN Control?` -> Rally
(place Guerrillas, or place a Base by removing 2 Guerrillas), then `improves
the trail` by 1 (`No trail improvement. The Trail is at 4.` at the cap), then
Infiltrate (Troops into Laos/North Vietnam, or **replace a VC Base with an
NVA Base** in a shared space). `Trung: NVA - N/NN`, `8+ NVA Troops in a space
outside the South?` -> Infiltrate then **March**: 20 Troops can leave Laos in
one card into three Provinces, with activation rolls between destinations.
`Trung: NVA - T`, `6+ NVA Troops in any space with COIN Troops or COIN Base?`
-> **Attack with Troops**: removes every US Troop in the space, never the
Irregulars or Police beside them, and loses the same number of NVA Troops to
Attrition; then Ambush from an adjacent LoC (`Ambushes in LOC Kontum -- Dak
To, targeting Binh Dinh`, 1 Active piece removed). `Trung: NVA - R/RR`,
`Underground NVA Guerrillas in space with Support?` -> **Terror**: flips one
Guerrilla Active, adds a terror marker, drops Support one level (Passive ->
Neutral), and can run through six spaces in one Op. Its Special Activity
whenever `3d6 <= Available NVA Troops` fails is **Bombard**: 1 Troop removed
from each of 2 spaces, spaces holding no NVA piece at all (US Troops to
Casualties, ARVN Troops to Available); when that check fails and there is
nothing to Ambush from, it takes an Op Only instead. Its Redeploy is in
section 6.
`Trung: NVA - R` opens with **`Support + Available >= 42?`**: that is *your*
score marker, so leading the game is itself the trigger that turns the NVA
toward you, producing Marches into South Vietnam and Bombards against Saigon.
`Trung: NVA - Q/QQ` runs `2d6 <= Available NVA Guerrillas`, then `d3 >= the
Trail`, then the Attack check, so a **low Trail makes the NVA Rally rather
than Attack**. When a branch cannot be executed the program says so and
draws again (`No spaces found for NVA Attack / The operation for Trung: NVA -
Q would be ineffective.`), which is a free look at the bot's whole priority
list. **At Trail 4 the NVA Marches for free outside South Vietnam** (Kevin's
note), so a stack in the Parrot's Beak can cross the map into Quang Tin in
one March. Degrading the Trail is worth more than its one box of NVA score.

**VC.** Critical/Performed shaded events whenever reachable. `Trung: VC - W`,
`Underground VC Guerrillas in space with US Troops?` -> Rally (4 Guerrillas
into a Base space at a time) then **Subvert** when `Patronage >= 17`: in each
of 2 spaces, remove an ARVN Police and place a VC Guerrilla, then Patronage
-1, which undoes a COIN Control built on ARVN Police. `Trung: VC - V/VV`, `3+
VC Guerrillas in any spaces with US Troops and no VC Base?` -> **Attack**:
`Die roll 3 Guerrillas): 1 [Success!]`, flips the Guerrillas Active, removes
2 US Troops, loses 2 Guerrillas to Attrition. Agitate in the Coup as in
section 6. A VC space with only a Base and no Guerrillas is a free Advise
target, and an Attack that loses both its Guerrillas to Attrition creates
exactly that. **Tax** (`Trung: VC - Z`, `15+ VC Guerrillas on the map?`;
`Spaces exist that can be Taxed?` and `2d6 > Agitate Total`): each Tax flips a
Guerrilla Active, shifts the space **one level toward Support** and adds 2 to
the Agitate Total (1 on a LoC). That looks like a gift and is not: it converts
board Opposition, which you can pacify away, into an Agitate Total that is
spent in the Coup Support phase **after** the Victory check, where you cannot
answer it. `Trung: VC - U`, `3+ VC Guerrillas in any space?` and `Underground
VC Guerrillas in space not at Active Opposition?` -> **Terror**; `Trung: VC -
X`, `Any 2+ Pop space without VC Guerrillas?` -> Rally; `Trung: VC - Y/YY`
and `Trung: VC - Z` -> Rally or March.

**ARVN.** Train (3 Troops + 3 Police into Saigon and Hue, 3 Resources each,
activation roll against 3), Patrol as in section 3, **Govern** (`Transfer
population value from Aid to Patronage`: Aid -pop, Patronage +pop, and the
space's Active Support **flips to Passive**, one level, not removal; needs a
COIN-controlled space with ARVN cubes outside Saigon; with Aid at 0 there is
nothing to transfer, but whether the program then skips Govern is untested),
**Transport** when `5+ ARVN Troops + Rangers in any one space` (moves Troops
and Rangers to an adjacent Province, then `Flip all Rangers underground`),
**Raid** (a Ranger moves in from an adjacent space, flips Active and removes
up to 2 pieces including an undefended Base, the same removal the US gets
from Advise), Redeploy as in section 6, and its pivotal at the first draw
where it qualifies. It has passed when sole eligible with only a Performed
marking. The chain that does the US most harm: `Trung: ARVN - M`, `NVA
Control + NVA Bases >= 14?` -> `3d6 <= Available ARVN pieces` -> on failure
`Trung: ARVN - MM`, `All routes from Can Tho to Hue blocked?` -> **Patrol,
then Govern**. Two lessons. **Govern arrives through the Patrol branch even
when the Available-pieces check has failed**, so emptying ARVN's Available
box (by Training its cubes onto the map) closes only some of the doors to
Govern. And the Can Tho-to-Hue route test means **enemy pieces sitting on
your LoCs steer ARVN into Patrol**, which can empty Saigon of every ARVN cube
and cost COIN Control there. Govern can take 8 points of US Support in two
cards at pop-2 spaces; it needs ARVN cubes in the space, so Support built
where only US pieces stand is immune.

- The Trail: NVA Rally improves it 1 box per Rally (2 under SA-2s); Air
  Strike degrades it 1 box for 2 hits; at Reset it moves toward the middle
  (0 -> 1, 4 -> 3). **At 4 the NVA Marches free outside South Vietnam**,
  which turns its Laos and Cambodia sanctuaries into one connected staging
  area; at 0-1 it Rallies instead of Attacking. ARVN's unshaded Rolling
  Thunder and Wild Weasels each degrade it 2 boxes.
- The Agitate Total is not score; Tax adds to it and the Coup Support phase
  spends it.
