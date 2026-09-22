# Fire in the Lake, US faction: what the program taught me

Observed at the program's own prompts or in its narration over five games;
descriptive, not advice. Where a statement is an inference rather than an
observation, it says so.

**Still unobserved after five games:** Air Strike carried through to a hit
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

**Advise.** Up to 2 spaces; no Resource cost, no Support shift. Whichever
options are taken, the US may afterwards voluntarily add +6 Aid. In each
space one of:
- **Irregular/Ranger removal.** Needs an Underground US Irregular or ARVN
  Ranger in the space; flips it Active and removes 2 enemy pieces of the
  US's choice among NVA Troops and Guerrillas (Underground or Active); a
  Base only when no other enemy piece remains in the space.
- **ARVN Sweep.** Activates Guerrillas in the space; no movement, no roll.
- **ARVN Assault.** An Assault by the ARVN cubes in the space, LoCs
  included: about 1 hit per 2 ARVN cubes in a City, fewer in Highland; an
  undefended Base is a legal target.

A space used for Advise cannot be used for Train in the same action.

**Air Lift.** Up to 4 spaces (2 in Monsoon), any distance apart. Moves US
Troops and ARVN Troops between the selected spaces (Irregulars and Rangers
untested); map to map only, never to or from Available. Control changes
take effect at once.

**Air Strike.** Never carried through to a hit. The number of hits is rolled
when the activity starts. Up to 6 spaces (2 in Monsoon); a struck space must
contain COIN pieces. Removes NVA Troops and Active Guerrillas only.
Degrading the Trail costs 2 hits. Each populated struck space shifts one
level toward Active Opposition (Laos and Cambodia have population 0).

## 4. Events and capabilities, mechanically

- Dual events: the executing faction chooses Unshaded or Shaded. Single
  events have one text.
- A **capability** persists across Coups. A **momentum** is removed at the
  Coup Reset.
- "Remove Support" sets the space to Neutral whatever its level. "Shift 1
  level toward Active Opposition" moves one step.
- "Place any 1 VC piece" lets the bot place a Base.
- "Pacifies as if Support Phase" (Honolulu Conference) applies the Support
  phase's strict test (section 5), not Train's.
- US pieces removed by an event go to Casualties, Available or Out of Play
  as that event's text says; ARVN pieces removed go to ARVN Available.
- "Remove pieces" events count untunneled Bases as pieces. Event-driven
  moves of US pieces to Available do not trigger the Commitment withdrawal
  penalty.
- Events that bring pieces from Out of Play ask per space and per piece
  type, including whether to place a Base.
- When an event makes the US lose pieces, the US chooses which.
- Any ARVN Assault that removes a Base adds +6 Aid, whether the Assault
  comes from an ARVN Op, an Advise, or an event.

## 5. Coup round, phase by phase

1. **Victory.** Any faction with score above 0 wins, highest first; ties go
   VC, ARVN, NVA, US. The check is made before anything else in the round,
   so nothing the Coup itself does counts until the next Coup.
2. **Resources.** Sabotage check; Trail-degrade check for COIN-controlled
   Laos and Cambodia spaces; ARVN gains Econ plus Aid, computed before the
   next step; then Aid drops by 3 per piece in the Casualties box, floored
   at 0. Econ is re-set from the unsabotaged LoCs.
3. **Support.** The US pacifies first, in up to 4 spaces that have COIN
   Control, US Troops and ARVN Police (Irregulars do not count as Troops).
   Up to 2 levels per space at the same cost as Train, from ARVN Resources
   above Econ. Then ARVN pacifies, then the VC spends its Agitate Total, 1
   per level, in spaces holding VC Guerrillas.
4. **Redeploy.** ARVN must redeploy its Troops to Cities or to spaces with
   a US or ARVN Base, then may redeploy Police to any COIN-controlled space;
   Control is not re-evaluated between the two, so the first never limits
   the second. The NVA may move Troops from Laos and North Vietnam into
   South Vietnam, taking Control there.
5. **Commitment.** US Base casualties and one third of Troop casualties go
   Out of Play; Irregular casualties go to Available; the remaining Troop
   casualties must be placed on the map, on COIN-controlled spaces, LoCs or
   Saigon of the US's choosing. Then the US may move up to 10 Troops and 2
   Bases among Available, COIN-controlled spaces, LoCs and Saigon, the
   Troop allowance reduced by the casualties just placed. Withdrawal: for
   every 2 US pieces moved to Available the VC shifts 1 population one level
   toward Active Opposition.
6. **Reset.** The Trail improves from 0 to 1 or degrades from 4 to 3 and is
   otherwise unchanged; terror markers are removed; all Active Guerrillas,
   Irregulars and Rangers flip Underground; momentum is removed; all
   factions become Eligible; the Agitate Total is set by a d3; the Tru'ng
   deck is reshuffled.

The Coup card goes into the RVN Leader box and its leader effect applies
from then on; the card text says what.

## 6. Scoring and control

- **US** = Total Support + US Troops and Bases in Available. Irregulars,
  Casualties and Out of Play count nothing.
- **ARVN** = population under COIN Control + Patronage.
- **NVA** = population under NVA Control + NVA Bases on the map.
- **VC** = Total Opposition + VC Bases on the map.
- Support and Opposition count population x2 at Active, x1 at Passive.
- **COIN Control**: US and ARVN pieces together outnumber NVA and VC pieces
  together. **NVA Control**: NVA pieces outnumber all other pieces together.
  At equality neither holds. Bases count as pieces. The VC never has
  Control.
- Support and Opposition persist through changes of Control.

## 7. What the bots can do

**NVA.**
- **Rally**: places Guerrillas, or a Base in place of 2 Guerrillas; improves
  the Trail by 1.
- **Infiltrate**: adds Troops in Laos and North Vietnam, or replaces a VC
  Base with an NVA Base in a shared space.
- **March**: moves Troops and Guerrillas, several destinations in one Op. At
  Trail 4 it marches free outside South Vietnam, so every sanctuary is one
  move from the border.
- **Attack**: removes COIN pieces, losing Troops to attrition. **Ambush**
  can strike from an adjacent LoC, removing 1 piece.
- **Terror**: adds a terror marker and drops Support one level, never below
  Neutral.
- **Bombard**: removes 1 COIN Troop in each of up to 2 spaces, including
  spaces holding NVA Troops.

**VC.**
- **Rally**: places Guerrillas, or a Base in place of 2 Guerrillas.
- **Terror**: adds a terror marker and shifts the space one level toward
  Active Opposition.
- **Attack**: removes COIN pieces, losing Guerrillas to attrition, which can
  leave a Base undefended.
- **Subvert**: replaces ARVN cubes with VC Guerrillas, which can break a
  COIN Control built on ARVN cubes.
- **Tax**: shifts the space one level toward Support and adds to the Agitate
  Total. The Agitate Total is spent in the Coup Support phase, after the
  Victory check, one level toward Opposition per point.

**ARVN.**
- **Train**, **Sweep**, **Assault**, and **Patrol** (cubes onto LoCs, then
  one Assault on a LoC).
- **Govern**, in COIN-controlled Support spaces with ARVN cubes outside
  Saigon: either adds Aid, or transfers population from Aid to Patronage
  and shifts Active Support to Passive.
- **Transport** Troops and Rangers to another space; **Raid** with a Ranger,
  removing up to 2 pieces including an undefended Base.
