# Fire in the Lake, US faction: what the program taught me

Observed at the program's own prompts or in its narration over four games;
descriptive, not advice. Where a statement is an inference rather than an
observation, it says so.

**Still unobserved after four games:** Air Strike carried through to a hit
(the menu has been opened and aborted, never resolved); Sweep activation
ratios outside Lowland; the "add an ARVN Assault" option inside a US Assault;
Train's forced removal of ARVN cubes from the map when Available is short of
6. A US Patrol prints no Resource deduction: it is free.

## 1. Sequence of play

**Card order and eligibility.** A card names an order of four factions.
Eligible factions act in that order. A card ends when two factions have
acted, or when every Eligible faction has acted or passed. Passing keeps a
faction Eligible and pays it +3 Resources (US and ARVN). If the first
Eligible faction passes, the next faction in order is treated as first
Eligible (inferred). If every Eligible faction passes, nothing happens and
all stay Eligible.

**What the first actor allows the second.** First actor Event: the second
may take an Op with a Special Activity. First actor Op with Special
Activity: the second may take the Event or a Limited Op. First actor Op
only (no Special Activity): the second may take a Limited Op only; the
Event is closed. A US Op only closes the Event in the same way. If the
second faction passes, the same option set passes to the next Eligible
faction.

**Limited Op.** One space, no Special Activity. A Limited Op Train still
offers its final action (Pacify or Transfer patronage) in that space; a
Limited Op Patrol or Sweep may move pieces from several spaces into the one
destination.

**Eligibility after acting.** A faction that executed an Op or Event is
Ineligible on the next card; a faction that passed stays Eligible. Events
that say "stay Eligible" or "Ineligible through the next card" override
this. After a Coup round every faction is Eligible.

**Bot action choice.** Each card carries a Tru'ng marking per bot
(Critical, Performed or Ignored, with a side); the program prints each
check as it runs. A bot that is **first Eligible** takes the Event if it is
marked Critical and effective; otherwise takes an Op only (no Special
Activity) if the next Eligible faction is marked Critical on this card;
otherwise passes if it will be first Eligible on the next card and is
Critical there; otherwise takes an Op with a Special Activity. A bot that
is **second Eligible** passes if it will be first Eligible on the next card
and is Critical there and cannot execute a Critical Event now; otherwise
takes the Event if it is still available, marked Critical or Performed,
and effective; otherwise passes if it will be first Eligible on the next
card; otherwise takes a Limited Op if the first actor took an Op; otherwise
an Op with a Special Activity. So a Performed marking is acted on only from
the second-Eligible slot; a first-Eligible bot never plays a Performed
Event. Bots do not coordinate with each other.

**Pivotal events.** One per faction: VC Tet Offensive, ARVN Vietnamization,
NVA Easter Offensive, US Linebacker II; each card's text holds its
pre-condition. A pivotal may be played only by an Eligible faction whose
pre-condition is met, before the first Eligible faction has done anything,
and not while a Coup card is on deck. It replaces the current card, which
is never played; the factions then act in the pivotal card's own order.
Eligibility is not reset: whoever was Eligible before the replacement is
Eligible on the pivotal. Precedence: Tet Offensive supersedes all others,
then Vietnamization, then Easter Offensive; the US pivotal plays only if
no other faction supersedes it, and a superseded pivotal returns to its
owner. In the program the check runs at each card draw in the order VC,
ARVN, NVA, US; a bot plays its pivotal when a d6 rolls strictly lower than
the number of Coup cards in the RVN Leader box (Duong Van Minh does not
count), except that a first-Eligible bot marked Critical on the current
card keeps the card instead; the US is asked whether to play its pivotal
when it qualifies, and the prompt names the factions that could trump it.

**Monsoon** (a Coup card on deck): no Sweep, including Advise's Sweep; no
March; Air Lift and Air Strike limited to 2 spaces; no pivotal events. An
event's own free Sweep is still allowed.

**Deck structure.** Each pile of 13 is 12 event cards and 1 Coup card
shuffled together, so exactly one Coup lies somewhere in positions 1 to 13,
one in 14 to 26, and so on. A campaign (the cards between two Coups) can
therefore run from 0 to 24 event cards.

## 2. US Operations

**ARVN Resources.** The US may spend ARVN Resources only above the Econ
level: any Train placement or pacification that would leave Resources at
or below Econ is not offered.

**Train.** May be done in any space holding a US piece (Troops, Irregulars
or a Base). In each selected space:
- Up to 2 US Irregulars may be placed, at no cost.
- With a US Base present, ARVN Rangers or up to 6 ARVN cubes (Troops and
  Police) may be placed instead, for 3 ARVN Resources. Saigon gets no
  special treatment: without a US Base it offers Irregulars only.
- Pieces placed by Train are not limited to what is Available: if more are
  placed than Available holds, pieces on the map are voluntarily removed to
  make up the difference.
- Placing nothing still counts the space as trained.
Then one final action in one selected space:
- **Pacify**, in a COIN-controlled selected space; no other pieces are
  required. 3 ARVN Resources to remove a terror marker first, then 3 per
  level shifted toward Support, up to 2 levels (4 per marker or level under
  Nguyen Cao Ky). Works from Opposition as well as from Neutral.
- **Transfer patronage** to ARVN Resources, offered only when Saigon is a
  selected space: up to 3, one for one.
A space used for Train cannot be used for Advise in the same action, and
vice versa. Air Lift may share a space with Train.

**Assault.** Any number of spaces holding US Troops and removable enemy
pieces; no Resource cost. Removes NVA Troops and Active Guerrillas, then
Bases. An Underground Guerrilla shields the Base in its space; an undefended
Base is a legal target. Hits: 2 per US Troop if a US Base is present;
otherwise 1 per US Troop, or 1 per 2 US Troops in Highland. The "add an
ARVN Assault" option has never been offered.

**Sweep.** Any number of destination spaces, selected before anything moves;
a selected space with no Troops moved in still resolves. Only US Troops
move, from adjacent spaces only; ARVN cubes are never offered. Each space
resolves separately. In Lowland one Underground Guerrilla is activated per
US Troop; ARVN cubes add nothing; other terrains untested. Not allowed in
Monsoon.

**Patrol.** Free for the US (ARVN pays 3). Moves US cubes only, each along a
chain of adjacent LoCs and Cities that ends at the first space holding an
enemy piece; a Province is never a destination. Then Guerrillas on LoCs are
activated, one per US cube there, and one free Assault may follow in a LoC
holding US cubes, at one hit per US cube (ARVN Police in the LoC do not
count). The Assault is offered only when such a LoC exists; when it is
offered after a Limited Op Patrol into a City, that is the program bug
listed in PROMPTS.md, and it should be declined.

## 3. US Special Activities

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

## 4. Events and capabilities, mechanically

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
  phase's strict test (section 5), not Train's loose one.
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

## 5. Coup round, phase by phase

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

## 6. Scoring and control facts

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

## 7. What the bots did (their operations, as narrated)

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
section 5.
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
section 5. A VC space with only a Base and no Guerrillas is a free Advise
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
activation roll against 3), Patrol as in section 2, **Govern** (`Transfer
population value from Aid to Patronage`: Aid -pop, Patronage +pop, and the
space's Active Support **flips to Passive**, one level, not removal; needs a
COIN-controlled space with ARVN cubes outside Saigon; with Aid at 0 there is
nothing to transfer, but whether the program then skips Govern is untested),
**Transport** when `5+ ARVN Troops + Rangers in any one space` (moves Troops
and Rangers to an adjacent Province, then `Flip all Rangers underground`),
**Raid** (a Ranger moves in from an adjacent space, flips Active and removes
up to 2 pieces including an undefended Base, the same removal the US gets
from Advise), Redeploy as in section 5, and its pivotal at the first draw
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
