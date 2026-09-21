# journal.md — full turn plans and rationales (TestGame4)

This is the audit artifact. Every US action, Coup-round decision, and
pivotal-event decision gets an entry here **before** the first answer is
sent to the program, in the format given in `CLAUDE.md`. Rejections by the
program, aborts, and deviations from the plan are recorded verbatim in the
entry's Execution section. Previous games' journals are under `archive/`.


## Turn 1 — card #17 Claymores — before save-003
**Situation.** Opening card #48 Nam Dong: the NVA rallied two Bases into the
Parrot's Beak and Southern Laos, improved the Trail to 2 and Infiltrated
4 Troops each into Central Laos and North Vietnam; ARVN played Nam Dong
unshaded, clearing Pleiku-Darlac of its two VC Guerrillas and putting it at
Active Support. That gift is the thing that matters: **Pleiku-Darlac now holds
a VC Base with no Guerrilla to shield it**, and my Underground Irregular is
standing in the space. On #17 I am first in order and only the VC is also
eligible (ARVN and NVA are Ineligible). Scores: US 40 (-10), VC 27 (-8),
ARVN 36 (-14), NVA 6 (-12). Every insurgent piece on the map is Underground,
so Assault has no targets anywhere.

**Options considered.**
- *Claymores unshaded* ("Stay Eligible. Until Coup, no Ambush; remove 1
  Guerrilla each Marching group that Activates"). Denial value is nil: the
  shaded side needs a space holding both a COIN Base and an Underground
  Insurgent, and no such space exists (Pleiku has a US Base but the VC piece
  there is a Base, not a Guerrilla; Saigon has no insurgents), so the VC
  cannot cast it. Staying Eligible buys little either — on deck is #118 in
  the order VC, ARVN, NVA, US, where I am last and two bots will act before
  me. A bot marked shaded takes the unshaded side when that is what is left,
  so the VC may well hand me this momentum for free.
- *Op Only* (Op with no Special Activity) to cut the VC down to a Limited Op.
  Rejected: the Event I would be denying is unplayable for the VC anyway, and
  leaving the Event on its menu is if anything *good* for me — a VC that
  burns its eligibility on #17 is not there to cast Korean War Arms shaded
  (Critical, three VC pieces placed) on #118.
- *Op + Special Activity.* Taken.

**Plan.** **Op: Train. Special Activity: Advise.**
- Train spaces: **Quang Tri-Thua Thien** (place Irregulars, max offered — free,
  they score nothing in Available) and **Saigon** (do not place forces).
- Final Train action: **Pacify Saigon one level**, Passive Support -> Active
  Support, 3 ARVN Resources (30 against Econ 15, ample headroom).
- Advise in **Pleiku-Darlac** (Irregular/Ranger removal: the undefended VC
  Base) and **Binh Dinh** (removal: the 2 VC Underground Guerrillas). Accept
  the +6 Aid at the end.
Expected: Total Support 17 -> 23, US 40 -> 46. VC Bases on map 7 -> 6, VC
27 -> 26. Binh Dinh becomes COIN-controlled (US Troop + Active Irregular = 2
against the lone VC Base), so ARVN 36 -> 38. Aid 15 -> 27 (+6 for the Base
removed, +6 for Advise). ARVN Resources 30 -> 27.

**Rationale.** Saigon is the largest and safest point purchase on the board:
pop 6, COIN-controlled, already Passive Support, and the one Support space
ARVN's Govern cannot reach. Six US points for three of ARVN's Resources is a
price I will not see again. For the Advise I chose durability over volume.
Removing Guerrillas is never time-critical — the VC has 16 in Available and
Rallies them straight back — but **removing a Base is close to permanent**: the
VC holds only 2 Bases in Available and must strip 2 Guerrillas from a space to
place one. The Pleiku Base is undefended *now* and the VC's own Rally branch
("4 Guerrillas into a Base space") can close that window on its very next
action, so this is the piece to take while it is takeable, and it pays +6 Aid
on top of Advise's own +6 — Aid being the pacification budget for the rest of
the campaign. The second slot goes to Binh Dinh rather than Quang Tri because
Binh Dinh's COIN Control is the one that will survive: Quang Tri-Thua Thien
touches both North Vietnam and Central Laos, with 8 NVA Troops one March away,
while Binh Dinh touches Kontum, Qui Nhon, Phu Bon and four LoCs and can be
reinforced by land. Quang Tri instead takes the free Irregular, so that next
action it has a fresh Underground piece to Advise with while Binh Dinh's has
gone Active — the alternating Train/Advise engine the last post-mortem asked
for, given that a space used for Train cannot also be Advised in the same
action.

**Execution.** No rejection, no abort, no deviation from the plan. Four
things worth recording. (1) The Irregular prompt in Quang Tri-Thua Thien read
`Place how many Irregulars (0 - 2)` with 3 in Available and 1 already in the
space, so the 2 is a per-space Train limit, not a stacking cap; placing both
took COIN Control there at once (4 COIN pieces against 3 VC), which the plan
had not counted on. (2) The Advise option menu offered only `Use
Irregular/Ranger to remove enemy pieces` — no ARVN Sweep or Assault entry,
consistent with every insurgent piece on the map being Underground and no
ARVN cubes facing a removable enemy. (3) After the Advise returned, the Train
menu had **renumbered** from three entries to `1) Select a space to Train
2) Finished selecting spaces`, the Special Activity entry having dropped out
— the exact shape that cost an action in each of the three previous games.
The label answer resolved it correctly. (4) **Correction to RULES_LEARNED:**
removing the VC Base by Advise printed no `Each insurgent base removed adds
+6 Aid` line; Aid moved only 15 -> 21, the +6 from Advise's own prompt. That
bonus appears to attach to Assault removals, not to the Advise removal.
`Transfer patronage to ARVN resources` was offered in the final Train menu
(Saigon selected) and declined: it would have cost the 6-point Saigon
pacification, and Patronage 15 with ARVN at -10 is not yet the target. It is
still the one untested US tool.

**Result.** As planned, plus a bonus Control. US 40 -> 46 (Total Support
17 -> 23, Saigon Active Support). VC 27 -> 26 (Base removed from
Pleiku-Darlac). ARVN 36 -> 40 (COIN Control 21 -> 25: Quang Tri-Thua Thien
from the Irregulars, Binh Dinh from the Advise). Aid 15 -> 21, ARVN
Resources 30 -> 27, US Irregulars Available 3 -> 1. Four VC pieces off the
map for no US loss beyond two Irregulars flipped Active.

## Turn 2 — card #116 Cadres — before save-011
**Situation.** Three cards since my last action. On #17 the VC **passed** rather
than take Claymores unshaded, which I had thought it might; it banked its
eligibility and cast its Critical shaded Korean War Arms on #118, placing VC
Bases in Tay Ninh, Quang Tin-Quang Ngai and Quang Tri-Thua Thien — VC 26 -> 29
and my new Quang Tri Control gone to a 4-4 tie. ARVN passed; the NVA Rallied
Guerrillas into all four sanctuaries, improved the Trail to 3, then Infiltrated
them into 8 Troops each in Southern Laos and the Parrot's Beak. On #116 ARVN
took Cadres **unshaded** as a Capability — "VC to Terror or Agitate must remove
2 VC Guerrillas per space" — which taxes the VC's whole Opposition engine,
including its Agitate in the Coup Support phase, for the rest of the game. I am
the only Eligible faction, second after an Event, so my menu is Op (may add a
Special Activity) or Pass.

**Options considered.**
- *Op + Special Activity now.* Train Binh Dinh (COIN-controlled, Neutral, pop 2)
  and Pacify 2 levels to Active Support, +4; Advise in Quang Tri-Thua Thien to
  remove the 2 VC Underground Guerrillas, restoring Control and leaving 2
  undefended VC Bases there. Worth roughly +4 US and +2 ARVN.
- *Pass.* +3 ARVN Resources, and first eligibility on the on-deck card.

**Plan.** **Pass.**

**Rationale.** The on-deck card is **#26 LRRP, in the order US, VC, ARVN, NVA,
and the VC is marked Critical/Shaded on it.** Its shaded side reads "3
Irregulars map to Casualties. Shift each space they were in 1 level toward
Active Opposition." I have exactly 4 Irregulars on the map — 3 of them the
Quang Tri stack I have been building — so that card would take my Advise engine
and shift Quang Tri and Binh Dinh from Neutral to Passive Opposition and Pleiku
from Active to Passive Support: about +4 VC and -1 US, putting the VC on 33
against a threshold of 35 on the fifth card of the game. If I act here I am
Ineligible on #26 and the VC, first among the eligible, casts it.
If I pass, ARVN is Ineligible next card and the eligible are US, VC, NVA — and
the printed order puts **US first**, so the action is guaranteed by the card,
not by a bot's choice, which is the only kind of pass the last three
post-mortems endorse. I then get to decide on #26 whether to deny by taking
LRRP unshaded outright or by running an Op Only, which closes the Event to the
faction behind me. Either way I act on #26 instead of #116, so the pass costs me
no action at all — the Binh Dinh pacification is still there next card — and
buys the denial plus 3 ARVN Resources. Sixteen idle cards was the charge against
the last game; this is the opposite, a pass that converts a card I would lose
into the card I want.

**Execution.**
**Result.**

## Turn 3 — card #26 LRRP — before save-013
**Situation.** The pass worked exactly as the printed order promised: US first
eligible on #26, with VC and NVA behind me and ARVN Ineligible. But the draw
put **#1 Gulf of Tonkin on deck, also led by the US**, and acting here makes me
Ineligible there. Two US-led cards back to back and one action to spend.

**Options considered.**
- *Pass again*, keeping #1. Rejected outright: passing hands the first-eligible
  slot to the VC, which is Critical/Shaded on LRRP and would cast it. Priced
  below.
- *LRRP unshaded* ("US places 3 Irregulars outside the South then free Air
  Strikes"). Airtight denial, and the free Strike could degrade the Trail from
  3 without any Support shift, since Laos and Cambodia are pop 0. Rejected on
  the placement: I hold **1** Irregular in Available and 5 on the map, and the
  program's Train behaviour with an empty box is `There are not enough US
  Irregulars in the available box / You must remove 1 US Irregular from the
  map`. Placing 3 outside the South would therefore drag two Irregulars out of
  Quang Tri-Thua Thien and strand them in Laos — I would be dismantling my own
  Advise engine to stop the VC dismantling it.
- *Op + Special Activity.* The Advise is worth having (Quang Tri's 2 Guerrillas,
  which would restore Control and leave 2 undefended VC Bases), but it leaves
  the Event open to the faction behind me and the VC takes it.
- *Op Only.* Taken.

**Plan.** **Op Only: Train. No Special Activity.**
- Train space: **Binh Dinh**. Place 1 Irregular (my last in Available).
- Final Train action: **Pacify Binh Dinh 2 levels**, Neutral -> Active Support,
  6 ARVN Resources (33 against Econ 15; headroom is 18, enough for six levels,
  so both levels should be offered).
Expected: Total Support 23 -> 27, US 46 -> 50. Binh Dinh 3 COIN pieces against
the lone VC Base. ARVN Resources 33 -> 27.

**Rationale.** The denial has to happen. LRRP shaded sends 3 Irregulars to
Casualties and shifts each space they came from one level toward Active
Opposition; a bot picking to hurt takes one from each of Quang Tri, Binh Dinh
and Pleiku, which is +4 VC (two Neutrals to Passive Opposition), -1 US (Pleiku
off Active Support), -2 ARVN, and Binh Dinh's Control gone with it — the VC on
33 against a threshold of 35 on card six. That is the shape of the game I lost
in TestGame1 and it is not worth Gulf of Tonkin, whose unshaded side is
position rather than points (Out-of-Play pieces score nothing in the box and
nothing on the map; they only earn later through Support) and whose shaded
side is currently **null**, since the Casualties box is empty — so the bots
gain nothing from the card I am giving up, they simply waste it.
Op Only rather than the Event because it denies *and* pays. The evidence that
it denies is from this game: on #118 the VC took the Event, ARVN then
**passed**, and the NVA still received the full `Op (may add SA)` second-eligible
menu — the slot survives a pass and attaches to whoever acts second, so an Op
Only closes the Event to the VC and to the NVA behind it. And the worst case if
I have that wrong is exactly the outcome I would have had by playing Op + SA
anyway, with +4 points in hand instead of an Advise.
The last Irregular goes to Binh Dinh rather than Quang Tri deliberately. Quang
Tri Control bought with a fifth piece would be 5 against 4 and the VC has two
Bases there to Rally onto, so it would not survive a single Guerrilla; Control
there has to come from removing VC pieces, not adding mine. In Binh Dinh the
Irregular arrives **Underground** beside an **undefended VC Base**, which is
next action's Advise and one more VC point, and it thickens the Control that
protects the Support I am buying. Support persists through changes of Control,
so the +4 is banked whatever happens to Binh Dinh afterwards.

**Execution.** No rejection, no abort, no deviation. Three things learned.
(1) The final Train menu **also** carries a `Perform a Special Activity` entry,
so Op Only has to be declined twice — and after the Pacify the program asked
outright, `Do you wish to perform a special activity? (y/n)`. Answering `n`
printed **`Move the US cylinder to the Op Only box`**, which is the first time
this harness has seen that box used by the US.
(2) **The denial worked.** The VC drew `Trung: VC - W` and was held to
`Move the VC cylinder to the LimOp box` — a single Rally of 4 Guerrillas into
Tay Ninh. Its Critical shaded LRRP was never castable. The inference from
card #118 was right: an Op Only closes the Event to the whole second-eligible
slot.
(3) Operator note to self: do not pipe `ctl.py advance` into `head`, which
truncates the stream and leaves the controller parked at an Enter prompt.

**Result.** As planned. Binh Dinh Neutral -> **Active Support**, Total Support
23 -> 27, **US 46 -> 50**. ARVN Resources 33 -> 27. US Irregulars in Available
0. VC held to a Limited Op; it now has **0 Bases in Available** (all 9 on the
map), so any Base I remove cannot be replaced except by a Rally that first
strips 2 Guerrillas from the space.
**Standing warning for the rest of the campaign: US 50 is score +0, and
victory requires strictly more than the threshold. Fifty is the number that
cost TestGame3 an entire extra campaign. The target is 51.**

## Turn 4 — card #79 Henry Cabot Lodge — before save-021
**Situation.** Card #1 was the NVA's card and it was brutal. It Infiltrated 7
Troops each into Central Laos and North Vietnam, then Marched four times:
9 Troops into **Quang Tri-Thua Thien**, 5 into **Binh Dinh**, and small
detachments into Kien Phong and Kien Giang-An Xuyen, taking NVA Control of all
four. **NVA 6 -> 14 in a single card**, and it is now the nearest rival at -4.
Binh Dinh, which I pacified to Active Support last action, is under NVA Control
— though Support persists through changes of Control, so the 4 points are
intact. On #79 ARVN played Henry Cabot Lodge **shaded** against itself,
removing 3 of its own cubes for Patronage +6 (ARVN 36 -> 42) and going
Ineligible through the next card; the VC passed; I am sole eligible, second
after an Event, so Op (may add SA) or Pass.
Scores: US 50 (+0), NVA 14 (-4), VC 29 (-6), ARVN 42 (-8). The deck says the
on-deck card is card 8 of 13 in pile 1, so **Coup 1 is between one and six
cards away**.

**Options considered.**
- *Pass.* Rejected. On deck is #112 Colonel Chau in the order VC, ARVN, US, NVA
  with ARVN Ineligible, so passing does **not** buy me the first slot — the VC
  is ahead of me in the printed order and casts its Critical shaded side either
  way. Passing would only move my action from this card to the next one, and
  the board needs fixing now.
- *Train + Advise.* Advise in Quang Tri (3 Underground Irregulars) and Binh
  Dinh (1) could take 2 NVA Troops from each, breaking **both** NVA Controls
  for -4 NVA; but the Op would then be a Train whose best Pacify is Da Nang or
  Kontum at pop 1, +2. Net US 52, NVA 10.
- *Train + Air Lift.* Taken. Priced below.

**Plan.** **Op: Train. Special Activity: Air Lift (performed first).**
- Air Lift, 4 spaces: **Da Nang, Hue, Kontum, Binh Dinh**. Lift **2 US Troops
  Da Nang -> Hue** and **2 US Troops Kontum -> Binh Dinh**.
- Train space: **Hue** (now holding US Troops). No forces to place — no US Base
  there and 0 Irregulars in Available — so "Do not place forces".
- Final Train action: **Pacify Hue 2 levels**, Neutral -> Active Support, 6 ARVN
  Resources (30 against Econ 15; 24 left, clear of the floor).
Expected: Total Support 27 -> 31, **US 50 -> 54**. Binh Dinh: NVA 6 pieces
against 6 others once the Troops land, so **NVA Control breaks**, NVA 14 -> 12.
ARVN Resources 30 -> 24.

**Rationale.** Two corrections to how I have been valuing things.
First, **the Victory check is the first phase of the Coup, so pacification done
in the Coup's own Support phase cannot win that Coup** — it counts only for the
next one. With the Coup possibly one card away, every point has to be bought
*before* the card turns. That kills the tempting alternative of saving Hue as a
strict-test space for the Coup Support phase and demotes Da Nang's and Kontum's
US Troops, whose only near-term worth was qualifying them for that same phase.
Second, victory goes to the **highest** score above 0, not merely to anyone
above 0, so a point of my own is worth as much as a point denied to a rival,
and worth it against *all three* rivals at once. Working that through: the
Air Lift line leaves the NVA needing 23 points to beat me and the Advise line
also leaves it needing 23 — identical against the NVA — but the Air Lift line
puts the VC's bar at 40 instead of 38 and ARVN's at 55 instead of 53. Two extra
US points beat two denied NVA points because they count against everybody.
Air Lift breaks Control by *adding* pieces rather than removing them, which is
the trick that makes both effects fit in one action: Binh Dinh is NVA 6 against
4 others, so two US Troops landing there make it 6 against 6 and the marker
comes off. Hue is the only pop-2 space on the board that is COIN-controlled,
below Active Support, and reachable — worth 4 points where Da Nang and Kontum
are worth 2 — and it needs only a US piece present to become a Train space.
Sources: Kontum and Da Nang rather than Saigon. Saigon is adjacent to Tay Ninh,
where the VC now has 6 Guerrillas and 2 Bases, and it carries 12 points of
Active Support; stripping its US Troops would leave 4 COIN pieces against a
stack that can already field 6. Da Nang is not adjacent to the Quang Tri
stack, and Kontum is Neutral at pop 1, so both are cheap to thin.
The Advise is not lost, only deferred: Quang Tri still holds 3 Underground
Irregulars and Binh Dinh 1, and breaking Control is a just-in-time play — the
NVA re-marches, but pacified Support persists.

**Execution.** No rejection, no abort, no deviation. The Air Lift space prompt
was bare (typed names accepted); its inner prompts are all numbered menus.
Selecting all four spaces first and then lifting worked as documented, and Hue
appeared in the Train list immediately after receiving Troops, confirming that
Air Lift and Train may share a space.

**Result.** As planned at the time: 2 Troops Da Nang -> Hue and 2 Kontum ->
Binh Dinh, `Remove NVA Control marker from Binh Dinh` (NVA 14 -> 12), Hue
Neutral -> Active Support, **US 50 -> 54**. ARVN Resources 30 -> 24.
**Both halves were then undone within one card, and the manner matters.**
The VC cast Colonel Chau shaded exactly as forecast, stripping Passive Support
from Ba Xuyen, Khanh Hoa and Kien Hoa-Vinh Binh and dropping a Guerrilla into
each: US 54 -> 50, ARVN 42 -> 38. The NVA then Rallied, took the **Trail to 4**,
and Bombarded Hue and Binh Dinh for 2 US Troops to Casualties — and the Binh
Dinh Troop was the piece holding the 6-against-6 tie, so **NVA Control returned
there and the NVA is back to 14**.
The lesson is about *which kind* of gain survives. The Hue pacification is
still on the board and will be until something Terrors or Governs it; the
Control break lasted one bot action because it was bought with a tie, and a
tie is one Bombard wide. **Breaking Control by adding pieces is only as durable
as the thinnest margin in the stack — prefer removing enemy pieces, or add
enough to hold a real margin.**

## Turn 5 — card #66 Ambassador Taylor — before save-027
**Situation.** ARVN opened #66 with an **Op Only** (Training Rangers into Saigon
and 3 Troops + 3 Police into Hue), which closes both the Event and any Special
Activity to me: my menu is Limited Op or Pass. That is expensive, because
Ambassador Taylor unshaded is the card TestGame3 built its game on — "up to 2
US pieces from out-of-play to South Vietnam" is exactly the Province Base I
need — and I cannot reach it. Meanwhile the VC's Colonel Chau has taken
Ba Xuyen, Khanh Hoa and Kien Hoa-Vinh Binh from Passive Support to Neutral and
dropped a Guerrilla into each, breaking COIN Control in all three, and the NVA's
Bombard has put the Trail at 4 and 2 US Troops in Casualties.
**US is back to exactly 50, score +0.** Pile 1 has three cards left and one of
them is the Coup, so I have perhaps two more actions to find a point.

**Options considered.**
- *Pass.* +3 Resources, but on deck is #51 in the order NVA, VC, US, ARVN with
  both the NVA and the VC marked **Ignored**, which means an Op from each every
  time; two bots act and the card ends before my slot. Passing here buys
  nothing and loses this card too.
- *Limited Op Train + Pacify.* **Not available.** The Train list is every space
  holding a US piece — Hue, Saigon, Pleiku-Darlac, Binh Dinh, Quang Tri — and of
  those the three COIN-controlled ones are all already at Active Support, while
  Binh Dinh and Quang Tri are under NVA Control. Da Nang and Kontum are
  COIN-controlled and Neutral but I emptied them of US Troops last action, so
  they are not Train spaces. There is no pacification on the board this card.
- *Limited Op Assault in Binh Dinh.* Two US cubes in Highland is about 1 hit,
  enough to take NVA from 6 pieces to 5 against 5 others and break Control for
  -2 NVA. Rejected: it is the same tie-width gain the Bombard just undid, and
  it does nothing for a US score sitting exactly on the threshold.
- *Limited Op Train in Saigon -> Transfer patronage.* Tempting as the one
  untested US tool and it would raise the Resources that are now capping my
  pacification, but it scores nothing and builds nothing.

**Plan.** **Limited Op: Sweep in Kien Hoa-Vinh Binh, moving 1 US Troop from
Saigon.**
Expected: Kien Hoa-Vinh Binh becomes COIN-controlled (1 US Troop + 1 ARVN
Police against 1 VC Guerrilla), ARVN +2, and the Guerrilla flips Active. No US
points this card.
Fallback: if a Limited Op Sweep turns out not to offer troop movement, `abort`
at the operation menu — which reverses with no state change — and Patrol 1 US
Troop from Hue to Da Nang instead, which is certain and sets up +1 or +2.

**Rationale.** With no pacification available, the only thing worth doing with
a Limited Op is to manufacture one for the next action, and the question is
which target. Kien Hoa-Vinh Binh is **pop 2** and one COIN piece short of
Control: a single US Troop makes it 2 against 1, turns it into a Train space,
and puts a two-level shift from Neutral worth **+4** within reach, against
Da Nang's or Kontum's +2 at pop 1. It is also the space the VC just took off
me, so it is a repair rather than a new commitment.
One Troop, not two, and from Saigon rather than Hue. Saigon carries 12 of my
27 Support points and sits adjacent to Tay Ninh, where the VC now has 6
Guerrillas; at 8 COIN pieces it is untouchable, at 7 it still is, but at 6 a
six-Guerrilla March would tie it and strip COIN Control. One Troop keeps Saigon
at 7 and safely out of reach, and Kien Hoa only needs one.
The Resource position is the real constraint now and it is worth naming: 18
against Econ 15 leaves headroom for a **single** level, so even next card
Kien Hoa is +2 rather than +4 unless ARVN's Resources recover. That is the
argument for making the target a pop-2 space rather than a pop-1 one — at one
affordable level, pop 2 pays double.

**Execution.** No rejection, no abort, no deviation. **A Limited Op Sweep does
offer troop movement** — the fallback was not needed. Flow: `US Sweep space` ->
bare `Sweep in which space` -> `US Sweep Troops into` -> `US Move troops to
<space> from` (adjacent spaces holding US Troops) -> a count. Saigon was the
only source offered, confirming Sweep movement is one space.

**Result.** `Place COIN Control marker in Kien Hoa-Vinh Binh`, ARVN 38 -> 40,
and the VC Guerrilla there flipped Active. US unchanged at 50, as planned.

## Turn 6 — card #75 Sihanouk — before save-033
**Situation.** The Trail reached 4 and the NVA showed what that means: on #51
it Marched to **ten destinations in a single operation**, taking Control of
Quang Tin-Quang Ngai, Tay Ninh, Quang Nam, Quang Duc-Long Khanh, Phuoc Long and
three Cambodian spaces, and Ambushing the Police out of Da Nang and Quang Nam.
**NVA 14 -> 20**, above its threshold of 18, before ARVN's Assaults on #75
pulled it back to 16. ARVN has also spent itself down: **ARVN Resources are 12
against Econ 15**, which means pacification is not merely limited but
*refused* — the program rejects it outright below Econ. US sits on exactly 50.
The deck now says 12 of pile 1's 13 cards are drawn and all 12 were events, so
**card 13 is the Coup**: #43 Economic Aid is the last event card of the
campaign, and I have at most two decisions left.
I am the only Eligible faction on #75 — ARVN acted, NVA and VC are Ineligible.

**Options considered.**
- *Sihanouk unshaded* ("free Sweep into or in any Cambodia spaces, then free
  Assaults in one"). No denial value at all: both bots marked for the shaded
  side are Ineligible, so nobody can cast it whatever I do. And the effect is
  nearly empty for me — Cambodia is pop 0, so NVA Control there is worth 0
  points, and I have no US Troops adjacent to Cambodia to Sweep with.
- *Limited Op.* **Worthless this card.** Every Train action is gated on ARVN
  Resources exceeding Econ, and 12 against 15 fails the test, so neither Pacify
  nor cube placement is available; an Assault in Binh Dinh would remove one NVA
  piece from a space that is already COIN-controlled, for no points.
- *Pass.* Taken.

**Plan.** **Pass.** +3 ARVN Resources (12 -> 15), and stay Eligible for #43.

**Rationale.** This is the pass that the whole campaign turns on. **#43 Economic
Aid unshaded reads "2 ARVN or 2 US Bases out-of-play to Available. Then ARVN
Resources +6 or Aid +12."** US Bases in Available count for the US score and
Out-of-Play pieces count nothing, so moving my 2 Out-of-Play Bases into the box
is **+2 US, straight to 52**, which is the difference between winning Coup 1 and
repeating TestGame3's exact mistake of sitting on the threshold. Acting here
makes me Ineligible on #43 and the card would go unplayed — both bots are
marked *Ignored* on it, which means an Op every time — leaving me at 50 and
score +0 at the Victory check.
Passing keeps me Eligible, and on #43 the order is NVA, ARVN, US, VC with ARVN
Ineligible, so only the NVA acts ahead of me. The one risk is an NVA **Op Only**,
which would close the Event; but its Special Activity chain is reliable — when
the `3d6 <= Available NVA Troops` check fails it simply Bombards instead, as it
did on #112 — so it has taken an Op *with* a Special Activity on every card of
this game.
If the Event is reached I will take the **2 US Bases** and then **Aid +12**
rather than Resources +6: the Coup's Resources phase adds Econ + Aid to ARVN's
pile, so Aid is worth its face value in Resources at the Coup *and* keeps
paying at the next one, while +6 Resources is a one-off. Neither affects the
Victory check, which is the first phase; the Bases do.

**Execution.** Passed as planned; ARVN Resources 12 -> 15.

**Result.** **The risk I named came in.** The NVA's Special Activity chain broke
for once — `3d6 <= Available NVA Troops (2)` failed and, with no March to Ambush
from, it took an **Op Only** instead of Bombarding — so Economic Aid is closed
to me and the +2 US Bases are gone. Its Attack then removed 2 US Troops from
Binh Dinh and **1 Troop plus all 3 Underground Irregulars from Quang
Tri-Thua Thien**, which is my Advise engine destroyed in one operation: 5 US
Troops and 3 Irregulars now sit in Casualties and I have **no Irregulars
anywhere**. The pass itself was still the right price — a Limited Op at 12
Resources against Econ 15 could do nothing at all — but the plan rested on a
bot habit rather than on a rule, and the habit broke.

## Turn 7 — card #43 Economic Aid [MONSOON] — before save-035
**Situation.** Last event card of the campaign: **#126 Coup! Young Turks is on
deck.** The NVA's Op Only leaves me Limited Op or Pass. ARVN Resources are
**15 against Econ 15**, and the gate is Resources *exceeding* Econ, so
pacification is refused outright — there is no move on this board that raises
Total Support. Available holds 21 Troops and 2 Bases and no Op can add to it.
**So US stands at exactly 50, score +0, and cannot reach 51 before the Victory
check.** Nobody else is above 0 either — NVA 16 (-2), VC 29 (-6), ARVN 40
(-10) — so Coup 1 will pass with no winner and the game goes to campaign 2.
Accepting that, this action is worth exactly what it does for **Coup 2**.

**Options considered.**
- *Train in Kien Hoa-Vinh Binh and Pacify.* The one line that would win the game
  now, and it is closed: 15 is not greater than 15, and even a single level
  would leave 12, below Econ. Not worth spending the action to watch the menu
  refuse it.
- *Train in Saigon -> Transfer patronage to ARVN resources.* Still the one
  untested US tool, and it would cut ARVN's Patronage. Deferred: the Coup's
  Resources phase is about to hand ARVN roughly +41 anyway, so the Resources
  half is worthless this card, and ARVN at -10 is not the faction to attack.
- *Assault.* Not available where it matters — the NVA's Attack left **no US
  Troops in Binh Dinh**, and US Assault needs them.
- *Pass.* Rejected, and this is the point: the NVA has acted, so **my acting
  ends the card at two factions and the VC never gets its turn**. Passing would
  hand the VC a free Limited Op immediately before the Victory check.

**Plan.** **Limited Op: Patrol. Move 1 US Troop from Hue to Kontum.** If the
Limited Op allows a second destination, also move Pleiku-Darlac's Troop to
Qui Nhon.
Expected: no score change now; Kontum becomes a qualifying space for the Coup
Support phase.

**Rationale.** The Coup's phase order decides this. Victory is first, so nothing
I do now can win Coup 1; **Support comes third, before Commitment**, so the
free Troop casualties I get to place on the map arrive *too late* to create
pacification targets for this Coup's Support phase. Anything I want to pacify
at the Coup has to have US Troops and ARVN Police standing in it **before the
card turns**, and that is this action's only real job.
The Resources phase will give ARVN Econ + Aid — roughly +41 on Aid 26 — so at
the Support phase I will have something like 56 against Econ 15 and can afford
a dozen levels; the binding constraint will be **qualifying spaces, not money**.
Today only three qualify (Hue, Saigon, Kien Hoa-Vinh Binh) and the first two
are already at Active Support, so the phase would pacify Kien Hoa for +4 and
then stop with three of its four slots unused. Moving one idle Troop into
Kontum — COIN-controlled, Neutral, ARVN Police already there — adds a second
slot worth +2, and leaves US Troops in a II Corps city for the whole of
campaign 2. Hue's Troop is the right one to spend: Hue is already at Active
Support with 5 ARVN Police holding Control, so the Troop is doing nothing
there, whereas Saigon's last Troop is load-bearing with 6 VC Guerrillas and an
NVA stack next door in Tay Ninh.

**Execution.** Monsoon printed `Sweep is prohibited [Not allowed in Monsoon]`
and the operation menu listed only Train, Patrol, Assault. The Hue -> Kontum
move went as planned. **Then a deviation, and it was mine.** I tried to send
Pleiku-Darlac's Troop on to Qui Nhon for a second qualifying space; the program
never offered `Select destination` and moved it straight to **Kontum**. A
**Limited Op Patrol funnels every move into the one space** — that is what
"a single space" means for Patrol, and I should have seen it before spending
the second Troop. The `seq` guard did its job: the step expecting `Select
destination` found the Move-cubes menu instead and stopped without sending
`Qui Nhon` into it, so the mistake cost a wasted Troop move and nothing worse.
Net effect: Kontum holds 2 US Troops where 1 would have done, Pleiku-Darlac is
down to its Base and an Active Irregular (still COIN-controlled, still a Train
space through the Base), and the Qui Nhon +1 was never available.
One new fact for the record: the Patrol's closing `Assault at one LOC` resolved
as **`US assaults in Kontum`** — the Patrol destination, a City, not a LoC —
and **2 US Troops in a City inflicted 2 hits**, confirming roughly one hit per
cube in a City. Nothing was there to remove, so it was a harmless no-op.

**Result.** No score change, as expected: **US 50, score +0 going into the
Victory check**, with NVA 16 (-2), VC 29 (-6), ARVN 40 (-10) — no faction above
0, so Coup 1 will produce no winner. Kontum now has US Troops beside its ARVN
Police under COIN Control, which makes it the second space qualifying for the
Coup Support phase's strict test alongside Kien Hoa-Vinh Binh. Acting rather
than passing ended the card at two factions and **denied the VC its last turn
before the Coup**.

## Coup 1 — #126 Young Turks — Support phase
**Situation.** Victory phase: `None of the Factions has achieved its victory
condition` — US 50 against a threshold of 50 is score +0, not a win, exactly as
forecast. The VC then sabotaged four LoCs, which **cut Econ from 15 to 12** —
the VC spiting ARVN's income widens my pacification floor, as the last
post-mortem noted. ARVN earned +38 to **53 Resources**, and Aid fell 26 -> 2 on
the 8 pieces in Casualties. Pacification headroom is 53 - 12 = 41, about
thirteen levels, so money is not the constraint; spaces are. The program offers
exactly the two I spent the last two actions manufacturing: **Kontum** and
**Kien Hoa-Vinh Binh**.
**Plan.** Pacify **both, two levels each**: Kien Hoa-Vinh Binh Neutral ->
Active Support (pop 2, +4) and Kontum Neutral -> Active Support (pop 1, +2),
12 Resources in total. Expected Total Support 27 -> 33, **US 50 -> 56**.
**Rationale.** Nothing competes for these Resources — the US pacifies first in
this phase and ARVN would otherwise spend them on its own Ops. Both spaces hold
a single ARVN Police, so both are Govern-reachable afterwards, but Govern takes
one level at a time and +6 banked now against that risk is a trade worth making.
This is the pay-off for reading the Coup's phase order correctly: Support comes
before Commitment, so these targets had to exist *before* the card turned, and
they did.

## Coup 1 — #126 Young Turks — Commitment phase
**Situation.** Rotation sent 1 Troop Out of Play and returned all 3 Irregulars
to Available; **4 Troop casualties are mine to place free** on any
COIN-controlled space, LoC or Saigon. Then up to 10 Troops and 2 Bases may move
between Available and the map, at **1 US point per piece taken out of the box**.
ARVN's Redeploy has meanwhile placed COIN Control in Da Nang and **removed it
from Binh Dinh** (Binh Dinh is absent from the placement list, which confirms
it). US stands at 56 after the two pacifications: 33 Support + 23 in the box.

**Plan.**
- Free casualties: **2 to Kien Hoa-Vinh Binh, 1 to Saigon, 1 to Da Nang.**
- Move out of Available: **1 US Base to Kien Hoa-Vinh Binh** (-1 US, to 55).
  No Troops moved, either direction.

**Rationale.** The free Troops cost nothing and should buy position the box
cannot. Kien Hoa-Vinh Binh takes two: it is the pop-2 space I just lifted to
Active Support and it is held by a bare 2 COIN pieces against a VC Guerrilla,
so it is both the most valuable and the thinnest thing I own — and it is
**adjacent to Kien Phong**, the one large Support project left on the board
(pop 2 at Active Opposition, held by only 3 enemy pieces, an 8-point swing if
it can be taken and pacified). Saigon takes one because 12 of my 33 Support
points sit there next to Tay Ninh's 15 enemy pieces; the Support itself
survives a change of Control, but **losing COIN Control there would leave me
unable to repair Saigon if Terror knocks it down**, and that is the loss worth
insuring against. Da Nang takes one purely to make it a Train space: Neutral at
pop 1 and newly COIN-controlled, it is worth +2 and is otherwise unreachable,
since Train needs a US piece present.
The Base is the one point I will spend. ARVN has 41 Resources against Econ 12
and no use for them that helps me; a US Base converts that dead money into
force, because Train may place up to 6 ARVN cubes in a space holding one, for 3
Resources. In Kien Hoa that means a pop-2 Active Support space held by a real
margin instead of a tie, Police on the ground for the Coup 2 strict test, and a
staging stack next door to Kien Phong. One point for six cubes and the only
route to a pop-2 gain is the right price.
I am **not** moving Troops out of Available, and not moving any to it. Each
Troop out is a point for a piece with no specific job; and pieces moved *to*
Available trigger the withdrawal penalty — the VC shifts a population toward
Active Opposition — which at Saigon's pop 6 could cost far more than the point it
pays. The box stays at 21 Troops and 1 Base.

## Turn 8 — card #105 Rural Pressure — before save-042
**Situation.** Coup 1 passed with no winner. The Reset degraded the Trail to 3,
cleared the sabotage, flipped everything Underground and reshuffled; the Agitate
Total is 2. The VC opened campaign 2 with its Critical shaded Rural Pressure:
Ba Xuyen to Passive Opposition, Phu Bon-Phu Yen's Support removed, Kien Hoa
knocked from Active back to Passive Support, Patronage -6. **US 55 -> 52**,
ARVN 39 -> 33, VC 31 -> 32. The NVA passed, so I am the second actor.
My Advise engine is back: the Reset flipped the returned Irregulars Underground,
so Binh Dinh holds **2 Underground Irregulars** and Pleiku 1, and Saigon still
has 2 Underground ARVN Rangers. Aid is down to 2, which as a side effect has
all but disabled ARVN's Govern — there is nothing left to transfer.
On deck is **#109 Nguyen Huu Tho, VC Critical/Shaded: "Place a VC Base and a VC
Guerrilla in Saigon. Stay Eligible."** The VC leads that card and I am last in
its order, so this cannot be denied — it is TestGame3's Saigon problem arriving
on schedule.

**Options considered.**
- *Pass.* Pointless: passing does not improve my position on #109, where the VC
  acts first whatever I do, and it wastes this card.
- *Train + Advise.* Taken.

**Plan.** **Op: Train. Special Activity: Advise.**
- Train space: **Kien Hoa-Vinh Binh**. Place 2 Irregulars (free).
- Final Train action: **Pacify Kien Hoa 1 level**, Passive -> Active Support,
  pop 2, +2 US for 3 Resources (41 against Econ 12 — no constraint now).
- Advise in **Binh Dinh** (2 Underground Irregulars against 1 NVA Underground
  Guerrilla and a VC Base) and **Quang Nam** (1 Underground ARVN Ranger against
  3 NVA Underground Guerrillas). Take the +6 Aid.
Expected: US 52 -> 54. Binh Dinh becomes COIN-controlled once the Guerrilla
goes (2 Irregulars against a lone Base), securing 4 points of Active Support and
ARVN +2; Quang Nam falls to 1 Ranger against 1 Guerrilla, a tie, so **NVA
Control breaks there**, NVA -1. If the Base in Binh Dinh is also removable the
VC drops a point as well.

**Rationale.** Kien Hoa rather than Da Nang for the pacification, although both
are worth +2. Da Nang's two levels cost 6 Resources and would put the points in
a Neutral pop-1 city with one US Troop, next door to Quang Nam's NVA Guerrillas
and two LoCs the NVA is sitting on. Kien Hoa's single level costs 3 and puts
them in a pop-2 space holding 3 US Troops, a US Base and 2 ARVN Police — the
strongest position I have. Support persists through Control changes but not
through Terror, so the question is which space the enemy can reach, and the
answer is Da Nang. Da Nang keeps for later; it is not going anywhere.
The Advise pair is the real value. Binh Dinh is 4 points of Active Support
currently sitting **Uncontrolled** after ARVN's Redeploy pulled its Troops out,
defended by nothing but my 2 Irregulars; removing the NVA Guerrilla restores
COIN Control on the spot. The Bases-last rule may mean only the Guerrilla is
offered, in which case the VC Base stays and my second Underground Irregular
kills it next action. Quang Nam is the cheapest point on the board: one Ranger
already standing there converts two removals into a broken NVA Control.

## Turn 9 — card #86 Mandate of Heaven — before save-046
**Situation.** Two strokes of luck and one blow. **#109 Nguyen Huu Tho — the VC
Critical shaded card that would have put a VC Base and Guerrilla in Saigon —
went unplayed, because the VC was Ineligible on it.** The blow came from the
NVA instead: it Marched 4 Troops out of Quang Tri into **Hue**, taking NVA
Control of a pop-2 City, and another Troop into Quang Nam. **NVA 15 -> 18,
exactly its threshold.** ARVN then took Mandate of Heaven unshaded (a Govern
capability, of little use to it with Aid at 8) and the VC passed, leaving me
sole eligible, second after an Event.
Scores: **US 54 (+4)**, NVA 18 (+0), VC 31 (-4), ARVN 32 (-18). Worth stating
plainly: victory goes to the highest score above 0, so the NVA at +0 does not
beat me at +4 — it would need **25 points** to do that. My own score is the
thing to protect and grow.

**Options considered.**
- *Pass.* Useless again: on deck is #87 in the order ARVN, VC, NVA, US, and
  ARVN is Critical/Shaded on it. I am last in that order either way.
- *Advise.* Weak targets this card — Binh Dinh and Saigon are now clear of
  enemies, and Kien Hoa holds a single VC Guerrilla. Not worth the slot.
- *Train + Air Lift.* Taken.

**Plan.** **Op: Train. Special Activity: Air Lift.**
- Air Lift, 4 spaces: **Kontum, Hue, Kien Hoa-Vinh Binh, Quang Nam**.
  2 US Troops **Kontum -> Hue**; 1 US Troop **Kien Hoa -> Quang Nam**.
- Train space: **Da Nang**. No forces to place.
- Final Train action: **Pacify Da Nang 2 levels**, Neutral -> Active Support,
  pop 1, +2 US for 6 of ARVN's 41 Resources.
Expected: **US 54 -> 56**. Hue goes to 5 COIN against 4 NVA, so **COIN Control
returns** (NVA -2, ARVN +2); Quang Nam goes to 2 against 2, a tie, so NVA
Control breaks there too (NVA -1). **NVA 18 -> 15.**

**Rationale.** Da Nang is the only Train-Pacify left on the board — every other
COIN-controlled space holding a US piece is already at Active Support, and the
Passive-Support pop-1 cities have no US piece to make them Train spaces. So the
Op is settled and the question is what the Special Activity buys.
Air Lift over Advise because it converts idle Troops into two broken NVA
Controls in one activity. Kontum's 2 Troops are doing nothing — it is Active
Support at pop 1 with no enemy near and an ARVN Police to hold it — whereas in
Hue they are the margin between NVA Control of a pop-2 City and COIN Control of
it. I am buying Hue with **two** Troops rather than one deliberately: one would
only tie at 4-all, and I have already been taught this campaign what a tie is
worth — the Binh Dinh tie I bought on card #79 was undone by a single Bombard
on the same card. Five against four is a real margin. Quang Nam gets the tie
treatment only because it is worth 1 point and I have nothing better for the
fourth slot.

## Turn 10 — card #38 McNamara Line — before save-050
**Situation.** The NVA took Nguyen Chanh Thi **shaded**, replacing 2 ARVN Police
in Hue with a **VC Base and a VC Guerrilla** — so the Saigon problem I dodged on
#109 has arrived in Hue instead. Hue is now Uncontrolled: COIN 3 against NVA 4
and VC 2. ARVN 35 -> 29, VC 31 -> 32. I am first among the eligible on #38, with
only ARVN behind me.
Scores: **US 56 (+6)**, VC 32 (-3), NVA 15 (-3), ARVN 29 (-21).

**Options considered.**
- *McNamara Line* (single event): redeploys COIN forces out of Laos/Cambodia —
  I have none there, so that half is dead — costs ARVN 12 Resources, and bars
  NVA Infiltrate and Trail improvement until the Coup. Real but not points, and
  the Resource hit lands on my own pacification budget.
- *Pass, to take #64 Honolulu Conference next card.* Seriously considered and
  rejected. Honolulu's prize is "Pacifies as if Support Phase" — the **strict**
  test, needing COIN Control **and US Troops and ARVN Police** together — and
  **not one space on the board currently qualifies with anything to gain**.
  Every space that has both is already at Active Support; every space below it
  (Qui Nhon, Cam Ranh, An Loc, Can Tho, Phu Bon-Phu Yen) has ARVN Police but no
  US Troops. The trap is that I cannot both build those spaces and use the card:
  acting here to create them makes me Ineligible on #64, and passing to keep #64
  leaves nothing for it to pacify. Since the event would then pay only Aid +10
  and Patronage -5, the +2 on the table now is worth more.
- *Op + Special Activity.* Taken.

**Plan.** **Op: Train. Special Activity: Air Lift.**
- Train space: **Quang Nam**. Pacify **2 levels**, Neutral -> Active Support,
  pop 1, **+2 US** for 6 Resources.
- Air Lift: 1 **Underground Irregular, Kien Hoa-Vinh Binh -> Hue**.
Expected: **US 56 -> 58.**

**Rationale.** Quang Nam is the only Train-Pacify left anywhere — everything
else COIN-controlled with a US piece is already maxed — so the Op chooses
itself, and the Air Lift I broke NVA Control with last card is what made it
possible.
The Irregular into Hue is the setup that matters. Hue holds 4 points of Active
Support with a **VC Base and an Underground Guerrilla** sitting in it, which is
both a VC point and a standing Terror threat against my Support; Advise is the
only tool that reaches an Underground Guerrilla and a Base, and it needs an
Underground Irregular or Ranger **in the space**, which Hue has not got. One
Irregular delivered now turns next action's Advise into the removal of both
pieces. It comes from Kien Hoa rather than Binh Dinh on purpose: Binh Dinh's
lone Irregular is the only COIN piece holding Control of a pop-2 Active Support
space, and moving it would hand back the Control I bought two cards ago, while
Kien Hoa still has 2 Troops, a Base and 2 Police after giving one up.

## Turn 11 — card #24 Operation Starlite — before save-053
**Situation.** The VC took Honolulu Conference itself, choosing **Aid -10 to 0**
and Patronage -5, which strips ARVN's Coup income to Econ alone and has already
cut its Resources to 17 against Econ 12 — **one level of pacification per action
is now all I can afford**. ARVN played McNamara Line. The NVA has marched 5
Troops into Quang Nam and taken Control there, though my pacification holds at
Active Support. Binh Dinh is down to a single Active Irregular holding COIN
Control of a pop-2 space.
Scores: **US 58 (+8)**, VC 32 (-3), NVA 16 (-2), ARVN 23 (-27). I am first
eligible on #24.

**Options considered.**
- *Op + Advise.* Advise Hue (the Irregular I flew in last card removes the VC
  Base and Guerrilla, VC -1, and ends the Terror threat to 4 points of Active
  Support) and Advise Quang Nam (2 Underground Irregulars take 2 NVA Troops,
  restoring COIN Control, NVA -1). Worth -2 enemy points and real protection —
  but the Op itself would be empty, because **no space on the board is both
  COIN-controlled with a US piece and below Active Support**, so there is again
  no pacification to be had.
- *Operation Starlite unshaded.* Taken.

**Plan.** **Event, unshaded: remove all VC from Quang Tin-Quang Ngai** — 4 VC
Guerrillas and **2 VC Bases**. The space is coastal and adjacent to both Quang
Nam and Da Nang, each holding a US Troop, so it qualifies.
Expected: **VC 32 -> 30**, and the VC's entire I Corps base area gone.

**Rationale.** The deciding thought is that **Advise keeps and an Event does
not.** The Irregular sitting Underground in Hue will still be there next action,
and Quang Nam's two will too; Operation Starlite exists only on this card. And
it is the larger hit: two Bases against the one Advise would take, from a
faction holding **0 Bases in Available**, so these cannot be replaced except by
a Rally that first strips two Guerrillas — and I am removing its four
Guerrillas there in the same stroke. Taking it also denies the VC the shaded
side it is marked for.
Against that I am accepting the Hue Terror risk for a card. That is affordable
precisely because of where the score stands: at +8, with the VC at -3 and the
NVA at -2, no rival can pass me without gaining a dozen points, so the loss I
should fear is my own Support collapsing, and a single Terror in Hue is -2 of a
36-point Support total. A two-Base hit on the faction nearest me is worth more
than insuring against that.
