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
