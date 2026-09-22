# Post-mortem: TestGame4, US faction, won at the 2nd Coup (margin 6)

Companion to `RULES_LEARNED.md` (mechanics, now covering four games) and
`archive/TestGame4/journal.md` (every turn in full). This is the strategic
account: what was intended, what happened, what the next player should do
differently. It was written after the game from the journal, notes and
reports, not by the player during it. Scores are the program's, as the
Victory phases read them.

## The result in one line

The US won at the second Coup with 56 — 34 points of Support and 22 in the
force pool — against VC 30, NVA 14 and ARVN 31, the earliest win of the four
games, and it was bought in the Coup 1 Support phase by two spaces prepared
for exactly that purpose two cards earlier.

## The plan, and what it turned into

The three earlier post-mortems set the plan: Saigon and pop-2 Provinces first,
Advise every action, count the margin rather than the score, pass only when
the printed order guarantees the next card. Most of it held.

- **Card #17, the first action.** Train pacified Saigon to Active Support
  (+6 for 3 Resources) while Advise removed an undefended VC Base in
  Pleiku-Darlac and two Guerrillas in Binh Dinh. US 40 to 46, VC 27 to 26,
  and a bonus COIN Control in Quang Tri-Thua Thien from two free Irregulars.
- **Cards #116 and #26, the pass that worked.** A pass on Cadres bought the
  guaranteed first slot on LRRP, and an **Op Only** Train there closed the
  VC's Critical shaded LRRP to everyone behind. The VC drew its card and was
  held to a Limited Op. Binh Dinh went to Active Support and the US reached
  exactly 50.
- **Card #79, the Air Lift.** Two Troops into Hue made it a Train space and
  two levels of pacification took it to Active Support (+4); two more Troops
  into Binh Dinh broke NVA Control by a tie. US 54. Within the same card the
  VC's Colonel Chau took 4 points back and one NVA Bombard undid the tie.
- **The Resource wall.** From card #66 to the Coup, ARVN's Resources sat at
  or below Econ and pacification was refused outright. Three US actions in a
  row could not add a point. The two Limited Ops of that stretch (a Sweep
  into Kien Hoa-Vinh Binh, a Patrol into Kontum) were spent making those two
  spaces qualify for the Coup Support phase instead, which is what won the
  game a campaign later.
- **Campaign 2.** Train-and-pacify in Kien Hoa, Da Nang and Quang Nam, an
  Air Lift that put a real five-to-four margin into Hue and broke two NVA
  Controls, Operation Starlite for two VC Bases and four Guerrillas, a Patrol
  plus Advise to hold Saigon, and a final Limited Op whose only job was to end
  the card before the VC could act. US 52 to 58, then 56 after ARVN's Govern.

## Why the win came at the second Coup and not the first

| Coup | US | ARVN | VC | NVA | Outcome |
| --- | --- | --- | --- | --- | --- |
| 1 (#126 Young Turks) | **50** | 40 | 29 | 16 | nobody above 0 |
| 2 (#125 Nguyen Khanh) | **56** | 31 | 30 | 14 | **US wins by 6** |

Fifty again. TestGame3 sat on exactly 50 at its second Coup and this game sat
on exactly 50 at its first, and the journal saw it coming from card #26
onward ("the target is 51"). The point was not found, and the reasons are
worth separating:

- **ARVN's Resources, not the board, were the gate.** The bot spent itself
  down to 12 against Econ 15 by card #75, and the program refuses any
  pacification and any ARVN cube placement unless Resources exceed Econ. The
  last three US actions before the Coup had no pacification available at any
  price. The lesson from TestGame3 ("plan against the headroom, not the
  total") was known and still not enough, because the headroom went to zero
  on the bot's turn, not mine.
- **The pass on #75 rested on a habit.** Economic Aid's unshaded side would
  have put two Out-of-Play US Bases into Available for +2, and the plan
  needed the NVA to take an Op with a Special Activity so the Event stayed
  open. It had done so on every card of the game; on this one its Special
  Activity check failed and it took an Op Only, closing the Event. The pass
  was still the right price (a Limited Op at 12 Resources could do nothing),
  but the point it was buying was a probability, not a rule.
- **The tie in Binh Dinh** bought with the Air Lift on #79 was undone by a
  single Bombard the same card. Two points of NVA denial for one card.

What did work was reading the Coup's phase order: Victory first, so nothing on
the last card can win it; Support third, before Commitment, so pacification
targets must already hold US Troops and ARVN Police under COIN Control when
the Coup card turns. Kontum and Kien Hoa-Vinh Binh were manufactured for that
and paid +6 in the Support phase, then a free casualty placement and one Base
from Available turned Kien Hoa into the strongest position on the map. That
+6 is the whole winning margin.

## What went right

- **Op Only as a denial.** Confirmed at the prompts and in the bot's own
  narration: an Op with no Special Activity closes the Event to the whole
  second-eligible slot. It cost one Advise and stopped a Critical VC card.
- **Ending the card on purpose.** Twice (cards #43 and #67) the US took a
  Limited Op it did not need so that two factions had acted and the VC never
  got a turn before the Victory check. On #67 a pass would have given the VC
  a free action against a US total one Saigon Terror away from 50.
- **Real margins over ties.** After Binh Dinh, the Hue Air Lift on #86 sent
  two Troops rather than one, five against four, and that Control held.
- **Advise on the pieces that matter.** An undefended VC Base on turn one,
  then the Guerrilla and Base in Binh Dinh that restored Control of four
  points of Active Support, then Quang Nam's Troops for a broken NVA Control.
  The VC finished the game with no Bases in Available, so every Base removed
  stayed removed.
- **Operation Starlite over an Advise.** Two VC Bases and four Guerrillas
  from a faction with no Bases to replace them, taken with the reasoning
  that "Advise keeps and an Event does not".
- **The Patronage transfer, tested at last.** Capped at 3, one for one; ARVN
  34 to 31 on a card where nothing else could be gained.
- **Recovering from the interface.** One container loss, resumed from the
  save at the card prompt with nothing lost.

## What went wrong, in order of cost

1. **Fifty at Coup 1.** Covered above. A whole extra campaign, and every
   bot event in it, came from the one point that was not there.
2. **Support built where ARVN's Govern could reach it.** Kien Hoa-Vinh Binh,
   the pop-2 space the game was built around, held ARVN Police from the
   start; ARVN Governed it back a level on the last card before the Coup, US
   58 to 56. The same leak as TestGame3, again in the best space on the map.
3. **The Advise engine lost to one NVA Attack.** Three Underground
   Irregulars stacked in Quang Tri-Thua Thien, next to Laos and North
   Vietnam, were all taken in one operation on card #43. The Coup's Rotation
   returned them, but the engine was dark for the last three cards of the
   campaign. Irregulars should be spread, and not kept in the space with the
   most NVA Troops adjacent.
4. **Eighty-seven single-step `seq` calls.** The player used the guarded
   multi-answer tool one prompt at a time, because the same prompt is a
   numbered menu on one card and a bare typed prompt on another and a
   rejected answer left it unable to resolve labels. Nothing was lost to it
   this time, but it doubled the cost of every action. Fixed in the harness
   before TestGame5: answers are matched by label or typed as the prompt
   requires, and `PROMPTS.md` gives the chains.
5. **One wasted Troop move.** A Limited Op Patrol funnels every move into
   the one destination; the second Troop meant for Qui Nhon went to Kontum.
   The guard caught the next step, so the cost was one Troop out of place.
6. **A Patrol assault that should not have happened.** The Limited Op
   Patrol into Kontum was followed by an Assault in Kontum, a City. That is
   a program bug, now logged, and it removed nothing, but the journal built
   a plan on it two cards later (Patrol into Saigon expecting the free
   Assault) and got nothing. The rule is Assault in a LoC only.

## What the next player should do differently

- **Watch ARVN's Resources against Econ from the middle of each campaign,
  and buy points while the gate is open.** The bot can close it on its own
  turn with a four-space Sweep. When Resources are within one pacification
  of Econ, take the pacification now; there may be no later.
- **Manufacture Coup Support-phase targets deliberately, two cards before
  the Coup card can appear.** Neutral or Passive spaces under COIN Control
  holding US Troops and ARVN Police, one per available slot. They paid +6
  here and cost two Limited Ops that had nothing better to do.
- **A pass that depends on a bot's habit is a bet, not a plan.** Only the
  printed order guarantees a slot. The NVA's Op Only on #43 was the second
  time in four games a bot's Op Only closed the card the US was saving for.
- **Prefer removing pieces to tying stacks.** A tie is one Bombard wide.
  Where a tie is all you can afford, expect it to last one bot action.
- **Spread the Irregulars.** Two spaces of two beats one space of three, and
  never in the Province adjacent to North Vietnam and Laos.
- **End the card yourself on the last event card of a campaign.** A Limited
  Op that ends the card is worth more than a pass when the score is above
  the threshold and a rival is still eligible.
- **Write `seq` calls from `PROMPTS.md`, whole actions at a time.** The
  form problem that drove the single-step habit is gone.

## Numbers for the record

Twenty-six cards over two campaigns (24 events and 2 Coups). Thirteen US
turns: 6 Op + Special Activity, 1 Op Only, 3 Limited Ops, 1 Event, 2
Passes. Eleven event cards with no US action, all through ineligibility or turn
order. Pacification: 14 levels in 7 spaces (Saigon, Binh Dinh, Hue, Kien
Hoa-Vinh Binh twice, Kontum, Da Nang, Quang Nam); Total Support 17 to 34.
Enemy pieces removed by US action: 3 VC Bases, 4 VC Guerrillas by Advise or
ARVN Assault through Advise, 4 NVA Troops and 1 NVA Guerrilla by Advise, plus
Operation Starlite's 2 Bases and 4 Guerrillas. US losses: 5 Troops and 3
Irregulars to Casualties before Coup 1 (1 Troop rotated Out of Play, the
Irregulars returned), no Base lost. Coup decisions: one Support phase (2
spaces, 4 levels, 12 Resources), one Commitment phase (4 casualty Troops
placed free, 1 Base to Kien Hoa-Vinh Binh). Container losses: 1.
