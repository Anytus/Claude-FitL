# Fire in the Lake, US faction: what the program taught me

Written for the next playing session, from two games: TestGame1 (lost to the
VC at the 3rd Coup, cards #63 to the Coup) and TestGame2 (won at the 3rd Coup
by 4, the full 1964 opening through 24 cards and three Coup rounds). Everything
here was observed at the program's own prompts or in its narration; it is
descriptive, not advice. Where a TestGame1 note turned out to be wrong, the
correction is here and the old claim is struck. Where I am inferring rather
than reporting, I say so. Still unobserved after two games: US Patrol and US
Sweep as ordinary operations, US Assault outside a City, Air Strike under Arc
Light only, the later leaders, and any US pivotal prompt in TestGame2.

## 1. Driving the program

- `python3 tools/ctl.py send <text>` types one answer and prints the reply.
  `advance` runs bot turns and Coup phases until a prompt needs you or a card
  number. `screen` prints the current prompt with its menu.
- **One send per command, and print the screen before every answer.** Menus
  renumber in three different ways: a chosen space drops out of a space list;
  an option that is not currently legal is simply omitted (the final Train menu
  drops Pacify when no selected space can be pacified, the Special Activity
  menu drops Air Strike while a ban is in force, Advise drops the removal
  option once no space qualifies); and the first-eligible / second-eligible
  action menus have different shapes. Every one of my worst mistakes in both
  games was a number sent to a menu I had not read — in TestGame2 a two-entry
  final Train menu read `1) Transfer patronage  2) Finished`, I sent 2 from the
  remembered three-entry shape, and the whole action was spent doing nothing.
  Never chain two sends with the output discarded.
- **Some space prompts come with no list at all.** `Train in which space:`
  and `Air Lift in which space:` both arrived as a bare prompt several times;
  a typed space name (`Quang Tri-Thua Thien`, `Saigon`) is accepted. The very
  same prompt arrived numbered on other occasions, and then a typed name is
  rejected: `'Saigon' is not valid. Must be one of: 1, 2, ..., or abort`. There
  is no way to tell in advance; print the screen and answer whichever form is
  there.
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
- A Limited Op is a single space with no Special Activity, but a Limited Op
  Train **does** still offer the final Train action (Pacify / Transfer
  patronage) for that one space.
- The card prompt accepts only a card number: `'perform' is not a card number`.
  Harmless.
- `?` at `(perform or ?)` lists perform, show, history, rollback, inspect,
  adjust, help, quit. `show summary` prints scores, resources, Aid, Patronage,
  Trail, leader, cards drawn.
- `abort` then `y` inside an action undoes the whole action (TestGame1).
- The patched build (1.53+sbd) saves after every faction action, each card
  draw, each pivotal substitution, and once for a whole Coup round. In
  TestGame2 the container was lost **six times**, always at the card prompt;
  `ctl.py resume TestGame2` reloaded the latest save and returned to the same
  prompt every time with nothing replayed. Two consequences: during a Coup
  round `render.py` shows the pre-Coup save, so read the phase results from the
  narration; and `transcript.log` restarts on resume, so paste narration into
  the report before the container can be lost.
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
- **Monsoon** (the card before a Coup): Sweep prohibited as an Op; Air Strike
  limited to 2 spaces; an event's free Sweep is still allowed (TestGame1).
- The render's "13 cards per campaign" is nominal: campaign 2 ran sixteen event
  cards before its Coup and campaign 3 ran two.

## 3. US Operations

**Train.** The space list is every space holding **any US piece** — Troops,
Irregulars, or a Base. ~~Spaces with US Troops (Bases alone were not
offered)~~: Quang Tri-Thua Thien was offered holding only Irregulars, and
Pleiku-Darlac holding an Irregular and a Base; Saigon was offered holding only
a US Base, though Saigon may simply always be offered. In each selected space:
- with a US Base present, or in Saigon: `Place Irregulars / Place Rangers /
  Place ARVN Troops/Police / Do not place forces`. ARVN cubes are up to 6 in
  total (`Troops (0 - 6)`, then `Police (0 - 4)` after 2 Troops) and cost 3
  ARVN Resources for the space; Rangers cost 3 too;
- without: `Place Irregulars / Do not place forces` only;
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
  Minh, Nguyen Khanh and Nguyen Van Thieu (4 under Nguyen Cao Ky in TestGame1),
  Terror markers a level each. It works from Opposition: `Shift 2 levels to
  Neutral` from Active Opposition, `Shift 2 levels to Passive Support` from
  Passive Opposition. The menu offers the whole shift as one entry. Refused
  when ARVN Resources do not exceed Econ (TestGame1: `Only 12 ARVN resources
  available and Econ is 15`). Pacify is absent from the menu when no selected
  space has a level to gain.
- **Transfer patronage to ARVN resources.** Offered **only when Saigon is one
  of the selected Train spaces** (Kevin's note, then confirmed by its absence
  on a Train that did not include Saigon). Never executed — see the menu
  mistake in section 1 — so its size is unknown. Patronage is ARVN score.
- A space used for Train cannot also be used by Advise in the same action, and
  vice versa; a space used by Advise disappears from the Train list. Air Lift
  has no such restriction: I lifted into a space and then selected it for
  Train, and also selected it for Train first and lifted into it after.

**Assault.** Not used in TestGame2 (no US Troops ever shared a space with a
removable enemy). TestGame1: only spaces with US Troops and removable enemies
are offered; removes NVA Troops and Active Guerrillas, Bases last; 2 US Troops
in Saigon with a US Base inflicted 4 hits, 2 cubes in Highland 1. Advise's
ARVN Assault with 2 Police in Highland inflicted 0.

**Sweep.** Not used as an Op in either game. The VC's Booby Traps shaded
capability (`Each Sweep space, VC afterward removes 1 Sweeping Troop on roll of
1-3, US to Casualties`) made it unattractive for the whole of TestGame2.
Advise's "Sweep a space with ARVN forces" only Activated the Guerrilla in
place; no cube movement was offered.

**Patrol.** Not used by me. ARVN's: moved a Troop and a Police from Saigon
onto a LoC, Activated Guerrillas on three LoCs, then one Assault on a LoC for
1 hit.

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
  Tri), NVA Troops, and an **undefended Base** (the lone VC Base in
  Pleiku-Darlac). Bases are last: while other enemy pieces stand in the space
  the Base is not on the list;
- when several piece types are present it lets you choose: `Select 2 pieces
  among the following: 5 NVA Troops, 1 NVA Underground Guerrilla, 2 VC
  Underground Guerrillas`, then `How many NVA Troops (0 - 2):` and so on in
  order, filling the remainder from the last type automatically;
- it costs no Resources and shifts no Support;
- the piece it flips Active is then exposed — an Active Irregular was Ambushed
  the same card.
Afterwards: `Do you wish to add +6 Aid? (y/n)`.

**Air Lift.** ~~Not used.~~ Select up to 4 spaces (bare prompt, typed names),
then `Lift forces out of <space>` to any other selected space; the prompt
offers `Air Lift US Troops` and, where present, `Air Lift ARVN Troops`
(Irregulars/Rangers presumably likewise, not tested), then a count. **No
adjacency limit** — Da Nang and Kontum lifted straight into IV Corps — and
**map-to-map only**: it cannot reach into Available, so it costs no US points.
Moving 2 Troops into a space with one Guerrilla gave COIN Control at once and
the control change and score markers printed inside the Air Lift. Medevac
shaded forbids it until the Coup (TestGame1).

**Air Strike.** Never used in TestGame2: the shaded Da Nang momentum and then
the shaded Rolling Thunder momentum each banned it until the Coup, and the
Special Activity menu simply omitted it with a `Notes: Momentum: #22 Da Nang
prohibits Air Strike` line. TestGame1: hits = one d6; up to 6 spaces (2 in
Monsoon); a struck space must contain COIN pieces except one per strike under
Arc Light; removes NVA Troops and Active Guerrillas only; "Degrade the trail"
costs 2 hits; **each populated struck space shifts one level toward Active
Opposition**, which in TestGame2 would have paid the VC 2 points per space and
is why I never wanted it.

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
   -39 to 0`, floored at 0).
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
   move to available: [Momentum: #15 Medevac (unshaded)]`). Then `Move up to
   10 US Troops and up to 2 bases among Available box, COIN controlled spaces,
   LoCs and Saigon`: the prompt asks the **source** first (Available plus spaces
   already holding US Troops), then the destination from a list of every
   COIN-controlled space, every LoC and Saigon — an Uncontrolled space is not
   on it. **This is the only way pieces leave Available**; Air Lift cannot.
   Each piece moved out costs 1 US point. Withdrawal: for every 2 US pieces
   moved to Available the VC shifts 1 population one level toward Active
   Opposition; the prompt prints even for 0 pieces.
6. **Reset**: the Trail was improved from 0 to 1 (TestGame1) and degraded
   from 4 to 3 (TestGame2) — two data points, consistent with "toward the
   middle" — Terror markers removed, all Active Guerrillas **and Active US
   Irregulars and ARVN Rangers** flip Underground, momentum removed, all
   factions Eligible, Agitate Total set by d3, Tru'ng deck reshuffled.

The Coup card goes into the RVN Leader box "on top of the stack". Leader
effects seen: Nguyen Khanh (Transport max 1 LoC), Nguyen Van Thieu (no effect
printed; pacify still 3), Nguyen Cao Ky (pacification 4 per level, TestGame1),
Failed Attempt (ARVN removes 1 in 3 cubes per space, TestGame1).

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

**VC.** Critical/Performed shaded events whenever reachable. `Trung: VC - W`,
`Underground VC Guerrillas in space with US Troops?` -> Rally (4 Guerrillas
into a Base space at a time) then **Subvert** when `Patronage >= 17`: in each
of 2 spaces, remove an ARVN Police and place a VC Guerrilla, then Patronage -1
— this is what undid a COIN Control I had built on ARVN Police. `Trung: VC -
V/VV`, `3+ VC Guerrillas in any spaces with US Troops and no VC Base?` ->
**Attack**: `Die roll 3 Guerrillas): 1 [Success!]`, flips the Guerrillas
Active, removes 2 US Troops, loses 2 Guerrillas to Attrition. Agitate in the
Coup as in section 6. A VC space with only a Base and no Guerrillas is a free
Advise target.

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

- The Trail: NVA Rally improves it 1 box per Rally (2 under SA-2s in
  TestGame1); Air Strike degrades it 1 box for 2 hits; at Reset it went 0 -> 1
  and 4 -> 3.
- The Agitate Total is not score; Tax adds to it (not seen from the VC in
  TestGame2) and the Coup Support phase spends it.
