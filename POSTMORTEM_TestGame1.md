# Post-mortem: TestGame1, US faction, lost to the VC at the 3rd Coup (margin 2)

Companion to `RULES_LEARNED.md` (mechanics) and `journal.md` (every turn in
full). This is the strategic account: what I intended, what happened, what I
would do differently. Scores are the program's, from `render.py`.

## The result in one line

The US sat at or near its threshold for two Coups (50 at Coup 1, 49 before
Commitment at Coup 2) and lost at the third with 44, because the plan that
produced those numbers produced nothing that could stop the VC once it moved.

## The plan, and the flaw in it

I played de-escalation from the first card: keep the Troops and Bases in
Available, where each is a point, and buy Support cheaply where I already had
Troops and Police (Saigon to Active Support before Coup 1, Da Nang and Kontum
in both Coup Support phases). Score-wise it worked: 37 to 50 by Coup 1 with
almost nothing on the map.

The flaw was that 26 to 28 of those points lived in a box and only 14 to 22
lived in people, and the people were three cities. Two things then happened
that the plan had no answer for. ARVN's Govern took Support out of every
COIN-controlled space it could reach, nine points across the second campaign,
and drained Aid doing it. The VC then converted a quiet Agitate Total into ten
points of Opposition in one Coup Support phase, from 28 to 38, and was above
its threshold before I had taken a single piece off it. A pool of Troops in
Available cannot pacify, cannot kill a Base, and cannot hold a Province. I had
built a score, not a position.

## What went right

- **Card-sequencing plays.** Passing on Colonel Chau to take Senator Fulbright
  (+4, and a permanent Base loss denied), passing on Gulf of Tonkin to take
  Tribesmen (three VC Bases removed, the shaded side denied), Claymores' "stay
  Eligible" (which then killed four marching VC Guerrillas for free), and
  passing on Arc Light so ARVN would execute it and leave me first on ROKs.
  Each was correct on its own terms and the journal shows the reasoning held.
- **Air power.** Aces took six NVA Troops off the Parrot's Beak and two boxes
  off the Trail; Wild Weasels removed SA-2s; the Arc Light capability let me
  break NVA Control in Quang Tin with one strike. The NVA finished at 13.
- **Reading the on-deck card.** Every Pass was made with the next card's
  markings in hand, and the bots' Critical markings proved a reliable
  predictor. This is the one skill I would tell the next player to keep.

## What went wrong, in order of cost

1. **No engine for Support.** I never put Troops and Police together in a
   pop-2 Province until Coup 2, and never had a second US Base on the map to
   let Train place Police outside Saigon. Every pacification I made was in a
   pop-1 city already at or near its ceiling. The one pop-2 space I finally
   worked, Quang Tri, produced 4 VC points in the last two cards; started at
   Coup 1 with a Base and Police, it and Binh Dinh would have been Support by
   Coup 2 and Govern-proof if held by US rather than ARVN cubes.
2. **Card denial ate my tempo.** Of my fourteen actions, six were Events and
   three were Passes. The Events were good Events, but only Tribesmen touched
   the VC score, and the VC score was the game. Denying a bot a card is worth
   what the card was worth; it is not worth more than building the thing the
   bot cannot take away.
3. **Rules learned by rejection, too late.** Pacification needs ARVN Resources
   above Econ (learned at card #15, when a whole Train was wasted and aborted).
   Advise's real menu (learned at the last card, from Kevin). "Op Only" leaves
   the second eligible a Limited Op (learned at card #68, where I had planned
   to take Green Berets). The withdrawal penalty (learned at Coup 1 by paying
   it). Degrading the Trail costs 2 hits and vanishes at 1 (learned mid-strike).
   None of these is obscure; each cost a turn.
4. **Menus answered from memory.** Quang Tri instead of Pleiku at card #63; two
   US Bases dropped into Hue during the adjust; declining a Special Activity by
   sending "3" to a three-entry menu; and, decisively, sending "2" to the
   two-entry second-eligible menu on Vietnamization, which passed the turn in
   which I meant to pacify Quang Tri. That Train was worth 2 to 4 VC points.
   The VC won by 2.
5. **Exposed pieces.** The lone Troop and Police I swept into Binh Dinh under
   ROKs were ambushed the same card; the single Police left in Da Nang was
   killed and an Active Support city fell under NVA Control to one Guerrilla.
   Small garrisons next to insurgent stacks are gifts.

## The decisive stretch

The game turned between cards #105 and #23. The VC's Rural Pressure undid my
Quang Tri pacification and put it at +9 with the Coup 8 cards away at most.
From there I needed roughly 6 VC points in 3 to 4 actions. I got 4 from Quang
Tri and the NVA gave me 3 by infiltrating Tay Ninh. The accidental pass cost
the one action that would have covered the gap; Attleboro's shaded side then
took two Saigon Troops for nothing. I do not think the position was winnable
for the US at that Coup in the sense of a US victory, but it was holdable, and
holding it was one clean turn away.

## What the next player should do differently

- **Decide what the score will be made of.** The pool is worth
  points in every era (the "US policy: JFK" label in render.py is a
  non-player-US marker with no effect on a human US), but plan from the start
  for Support to carry the total by Coup 2:
  that means a second US Base on the map early (Commitment phase is free), in
  a COIN-controlled pop-2 Province with Troops, so Train can place Police
  there and pacify two levels a card while ARVN Resources exceed Econ.
- **Manage ARVN's Resources as your own.** Pacification is paid in ARVN
  Resources and gated by Econ. Advise's +6 Aid raises the Coup income; ARVN
  passes add 3; the bot's Train and Patrol spend them. Track the number every
  card and never plan a pacification you cannot afford.
- **Watch the VC number, not yours.** The VC's Agitate Total (Tax adds 2 per
  space) is a delayed hit that lands in the Coup Support phase after the
  Victory check has already passed once but before the next; and Terror
  compounds it. Count what the VC will score at the next Victory phase, not
  what it scores today.
- **Use Bases as shields, not just points.** With 15 COIN pieces beside it the
  Quang Tri Base was never attacked; with none beside it the Pleiku Base would
  have been. Bases on the map also unlock Police placement, which unlocks
  pacification. Two of my three Bases spent the whole game in the box.
- **Read the menu, every time.** Print it, then answer. The interface renumbers
  after every choice and changes shape by eligibility; the program never warns.
- **Keep the sequencing habit, but price it.** Ask each card: what does the
  event deny, what does it build, and what would an Op + Special Activity
  build instead? Take the event only when the denial or the effect beats the
  build. Half my events would have failed that test.

## Numbers for the record

| Coup | US | VC | NVA | ARVN | Note |
| --- | --- | --- | --- | --- | --- |
| 1 (card 2) | 51 | 29 | 5 | 42 | Saigon Active, Da Nang/Kontum pacified |
| 2 (card 15) | 47 | 38 | 12 | 44 | VC crosses 35 via Agitate; NVA offensive follows |
| 3 (card 24) | 44 | 37 | 13 | 33 | VC wins by 2 |

Fourteen US actions: 6 Events, 5 Op + SA (one aborted and redone), 3 Passes
(one by mistake). Two Coup Support phases pacified 4 levels each; the
Commitment phases moved 1 Troop out and 1 Base + 1 Troop in. Pieces lost: 3
Troops and 1 Irregular to Casualties. Enemy pieces removed by US action: 3 VC
Bases, 17 NVA Troops, 12 Guerrillas, 2 NVA Guerrillas.
