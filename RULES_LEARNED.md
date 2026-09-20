# Fire in the Lake, US faction: what the program taught me (TestGame1, 1964-65)

Written for the next playing session. Everything here was observed at the
program's own prompts during one game (cards #63 through the 3rd Coup). It is
descriptive, not advice, and it is incomplete: I never used Patrol or Air Lift,
never saw a Sweep outside an event, and never reached the later policies or
leaders. Where I am inferring, I say so.

## 1. Driving the program

- `python3 tools/ctl.py send <text>` types one answer. `advance` runs bot turns
  and Coup phases until a prompt needs you (or a card number).
- Menus take the number. **Menus renumber after every selection**: once a space
  is chosen it drops out of the list and everything below it shifts up. Never
  answer a menu from memory; print it, then answer. Three of my worst mistakes
  were numbers sent to a menu I had not read.
- The action menu is different for first and second eligible. First eligible:
  `1) Event  2) Op (May add a Special Activity)  3) Pass`. Second eligible after
  an Event: `1) Op (May add a Special Activity)  2) Pass`. Second eligible after
  Op + SA: `1) Event  2) Limited Op  3) Pass` (inferred; I only saw the first
  two forms and the Limited-Op-only form). After a first-eligible **Op Only**
  the second eligible gets `1) Limited Op  2) Pass` and cannot take the Event.
- The card prompt (`Enter the number of the next On Deck Event card:`) accepts
  only a card number. Everything else is rejected harmlessly.
- `?` at `(perform or ?)` lists: perform, show, history, rollback, inspect,
  adjust, help, quit. `show summary` prints all four scores, resources, Aid,
  Patronage, Trail, leader, cards drawn and how many remain in the pile.
- `abort` then `y` inside an action undoes the whole action and prints a
  "changes to make to the board" list (reversals). If the action began right
  after a pivotal-event prompt, abort rewinds to that prompt.
- The patched build (1.53+sbd) saves after every faction action, each card
  draw, and each adjust; a save exists while the program waits at the card
  prompt, so a container loss costs nothing. Resume goes straight to the last
  prompt. `rollback` and `adjust` work from the `(perform or ?)` prompt and
  are Kevin's tools.
- Some prompts want a typed space name instead of a number (seen once, in Air
  Strike: `Air Strike in which space:` with no list). When only one space is
  legal the program often selects it for you (Assault, Pacify, Advise).

## 2. Sequence of play, as observed

- The card names an order of four factions. Only the first two eligible
  factions that act get an action; the card then ends and the program asks for
  the next on-deck card.
- Acting makes you Ineligible on the next card; you return to Eligible the
  card after. Passing keeps you Eligible. A pass by US or ARVN adds +3 ARVN
  Resources. Bots pass sometimes (VC, ARVN, NVA all did).
- Events that say "stay Eligible" (Claymores unshaded, Medevac shaded) do
  exactly that: you act and remain Eligible.
- After a Coup round every faction is Eligible.
- Tru'ng markings on the card (Critical / Performed / Ignored, with a side)
  predict the bots: Critical was taken every time it was reachable; Performed
  was usually taken; Ignored meant an Op. A bot that cannot take its preferred
  side as second eligible may pass instead.
- **Pivotal events.** At each card draw, if a faction is Eligible and its
  condition holds, the program asks (for the US: `Does US wish to play their
  pivotal?`); bots roll a die (success seemed to need a roll no higher than the
  number of cards in the leader box). A pivotal replaces the current card; the
  playing faction acts first with the pivotal as its action, then the others
  in the pivotal's order. US Linebacker II needs 2+ cards in the leader box and
  Support + Available above 40; ARVN Vietnamization needs fewer than 20 US
  Troops on the map. The prompt did not appear on the Monsoon card with a Coup
  on deck.
- **Monsoon** (the card before a Coup): Sweep prohibited as an Op; Air Strike
  limited to 2 spaces; an event's free Sweep is still allowed.

## 3. US Operations

**Train.** Select spaces with US Troops (Bases alone were not offered). In each:
- with a US Base present, or in Saigon: place up to 6 ARVN Troops/Police from
  ARVN Available, cost 3 ARVN Resources for the space;
- otherwise: place Irregulars (from Available, cost 3) or Rangers;
- "Do not place forces" costs nothing and still counts the space as trained.
Final action, in **one** selected space: Pacify (needs COIN Control, US Troops
and ARVN Police there; 3 Resources per level under Nguyen Khanh, 4 under
Nguyen Cao Ky; up to 2 levels when Resources allow; Terror markers cost a
level each) or "Transfer patronage to ARVN resources". Pacify is refused
unless ARVN Resources exceed Econ: `Only 12 ARVN resources available and Econ
is 15`. A space used for Train cannot also be used by Advise in the same action.

**Assault.** Only spaces with US Troops and removable enemies are offered; if
one, it is chosen for you. Removes NVA Troops and Active Guerrillas; Bases
last. Hits: 2 US Troops in Saigon (with a US Base) inflicted 4; 2 cubes in
Highland inflicted 1; 4 ARVN Police in Jungle inflicted 0. Lansdale (shaded
momentum) forbids US Assault until the Coup.

**Sweep.** Only seen inside events. Moving cubes Activated one Guerrilla per
cube in Highland (2 cubes, 2 Activated). Under ROKs the movement sources were
only spaces holding US Troops.

**Patrol.** Not used by me. ARVN's version: cubes move onto LoCs, Guerrillas
on those LoCs Activate, one Assault on a LoC.

## 4. US Special Activities

**Air Strike.** Hits = one d6 rolled at the start. Up to 6 spaces (2 in
Monsoon). A struck space must contain COIN pieces, except one space per strike
under the Arc Light capability (which is how I reached NVA stacks in Provinces
with no COIN pieces). Removes NVA Troops and Active Guerrillas only;
Underground Guerrillas and covered Bases are untouchable. "Degrade the trail"
costs 2 hits and disappears from the menu once fewer than 2 remain, so do it
first. Each populated struck space shifts one level toward Active Opposition
("No shift" if already there); LoCs have no population and shift nothing.
Aces (event) gave a fixed 6-hit strike on one space outside the South.

**Advise.** Up to 2 spaces, each either "Assault a space with ARVN forces" (ARVN
Assault with its own hit rates, free) or "Use Irregular/Ranger to remove enemy
pieces" (flips one Underground Irregular or Ranger Active in its own space and
removes 2 enemy pieces there; the pieces offered were Troops and an Active
Guerrilla, not Underground ones). Afterwards: `Do you wish to add +6 Aid?`.

**Air Lift.** Not used. Medevac (shaded momentum) forbids it until the Coup.

## 5. Events and capabilities, mechanically

- Dual events: you choose Unshaded or Shaded. Single events have one text.
- A "capability" persists (Arc Light for me; SA-2s for NVA until Wild Weasels
  removed it). A "momentum" lasts until the Coup Reset removes it.
- "Remove pieces" events count untunneled Bases as pieces (Tribesmen let me
  take three VC Bases). Event-driven moves of US pieces to Available do not
  trigger the Commitment withdrawal penalty (Senator Fulbright).

## 6. Coup round, phase by phase

1. **Victory** comes first. Any faction with score above 0 wins; the program
   printed `Game over in the 3rd Coup! round / VC wins with a victory margin
   of 2!` and asked whether to continue. Bots can win at any Coup.
2. **Resources**: sabotage check, Trail degrade check for COIN-controlled
   Laos/Cambodia spaces, ARVN earns Econ + Aid, Casualties reduce Aid.
3. **Support**: US pacifies first in spaces with COIN Control, US Troops and
   ARVN Police (up to 2 levels per space, 3 or 4 Resources per level; the
   prompt shows `(N spaces remaining, R ARVN resources, Econ is E)`); then
   ARVN pacifies; then the VC spends its Agitate Total (1 per level).
4. **Redeploy**: ARVN cubes leave LoCs and concentrate; NVA Troops may move
   home to Bases but need not (Kevin's clarification; the bot chose to once and
   not the other time).
5. **Commitment**: Base casualties and one third of Troop casualties go Out of
   Play, Irregular casualties to Available; then move up to 10 Troops and 2
   Bases among Available, COIN-controlled spaces, LoCs and Saigon. **Withdrawal:
   for every 2 US pieces moved to Available, the VC shifts 1 population one
   level toward Active Opposition.** One piece moved is penalty-free.
6. **Reset**: Terror markers removed, Active Guerrillas flip Underground,
   momentum cards removed, all factions Eligible, Agitate Total set by d3,
   Tru'ng deck reshuffled, Trail improved if at 0.

Coup card effects seen: Nguyen Khanh (Transport max 1 LoC), Nguyen Cao Ky
(pacification 4 per level), Failed Attempt (ARVN removes 1 in 3 cubes per
space, no leader change, card goes under the stack).

## 7. Scoring and control facts

- US = Total Support + US Troops and Bases in Available. Irregulars in Available
  do not count. Active Support counts population twice, Passive once.
- VC = Total Opposition (same doubling) + VC Bases on the map. The Agitate Total
  is not score; Tax adds 2 to it per space and it is spent in the Coup.
- NVA = NVA Control (population) + NVA Bases anywhere on the map, Laos and
  Cambodia included. ARVN = COIN Control (population) + Patronage.
- Control needs strictly more pieces than every other faction combined; at
  equality the marker comes off (NVA lost Binh Dinh at 5 versus 5).
- Support and Opposition persist in a space that changes Control.
- VC Rally with a Base present flips Active Guerrillas Underground; Rally without
  one places Guerrillas. VC Subvert removes ARVN cubes from spaces with VC
  Guerrillas and costs Patronage. ARVN Govern removes Support from a
  COIN-controlled space holding ARVN cubes, outside Saigon, and moves its
  population value from Aid to Patronage.
- The Trail: NVA Rally improves it (2 boxes under SA-2s); Air Strike degrades
  it one box for 2 hits; the Coup Reset improves it from 0 to 1.
