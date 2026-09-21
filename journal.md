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
