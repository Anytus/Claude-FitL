# journal.md — turn plans and rationales (TestGame9)

Every US action, Coup-round decision, and pivotal-event decision gets a brief
entry here **before** the first answer is sent to the program, in the format
given in `CLAUDE.md`. Previous games' journals are under `archive/`.


## Turn 1 — card #31 AAA — before save-001
**Plan.** Op + SA: Train Saigon (no placement) + Pleiku-Darlac (2 Irregulars), Pacify Saigon to Active Support; Advise Irregular removal in Quang Tri and Binh Dinh (2 VC Guerrillas each), +6 Aid.
**Why.** Saigon Active is +6 now and blunts Burning Bonze's shift on deck; Advise strips the Guerrillas guarding two VC Bases in pop-2 Highlands.
**Execution.** Program was not running at turn start; resumed from save-001. seq stopped after the first Advise space (second space auto-selected: only one candidate); finished with two single sends. Advise removal takes 2 Guerrillas without asking counts when only Guerrillas are present.
**Result.** As planned: Saigon Active (+6, US 44), COIN Control in Quang Tri and Binh Dinh (VC Bases left bare), Aid 21.

## Turn 2 — card #66 Ambassador Taylor — before save-007
**Plan.** Pass.
**Why.** ARVN's Op Only leaves me a Limited Op and closes the Event to NVA; passing keeps me first Eligible on #29 Tribesmen, where unshaded removes 4 Insurgent pieces (Pleiku Guerrillas + bare VC Bases) and denies VC's Critical shaded (all my Irregulars become VC Guerrillas).
**Execution.** none
**Result.** NVA took a Limited Op Rally (Base in Parrot's Beak, Trail 2); I stay first on #29.

## Turn 3 — card #29 Tribesmen — before save-010
**Plan.** Event unshaded: remove the three VC Bases in Quang Tri, Binh Dinh and Pleiku-Darlac plus 1 VC Guerrilla in Pleiku-Darlac.
**Why.** Denies VC its Critical shaded (5 Irregulars turned into Guerrillas); -3 VC points, and Bases are VC's scarcest piece (2 Available). The last Pleiku Guerrilla is left for Advise.
**Execution.** Rejected (send, no label matching): 'Binh Dinh' is not valid. Must be one of: 1, 2, 3, or abort — resent via seq. Pleiku-Darlac was auto-selected as the last candidate, so my 'Pleiku' landed on the count prompt: 'Pleiku' is not valid. Must be one of: 0, 1, 2, or abort — then sent 2, Bases 1 (Guerrilla count filled itself).
**Result.** As planned: 3 VC Bases and 1 Guerrilla removed, VC 27 -> 24.

## Turn 4 — card #79 Henry Cabot Lodge — before save-020
**Plan.** Op + SA: Train Saigon (no placement) and Quang Tri (1 Irregular), final action Transfer 3 Patronage; Advise Irregular removal of the last VC Guerrilla in Pleiku-Darlac, +6 Aid.
**Why.** ARVN is at 49 (wins at 51) and the pile-1 Coup lies within the next 5 cards; -3 Patronage buys margin against a Govern before it. Saigon's pacification can wait for the Coup Support phase (it qualifies).
**Execution.** seq stopped at 'Place how many Irregulars (0 - 2)' (asked despite 1 Available; answered 1). Advise space auto-selected (one candidate) and +6 Aid asked after one space.
**Result.** As planned: Patronage 24 -> 21 (ARVN 46), ARVN Resources 30, Pleiku clean, Aid +6.

## Turn 5 — card #110 No Contact — before save-029
**Plan.** Limited Op Sweep into Binh Dinh with 2 US Troops from Kontum and 1 from Pleiku-Darlac (5 US vs 3 NVA Troops).
**Why.** NVA is at 16 (wins at 19) and the Coup is card 12 or 13; flipping Binh Dinh to COIN Control takes NVA to 14 so one more March before the Coup cannot win it. ARVN rises to 46 (acceptable). Passing for #93 was weighed: NVA cannot act on #93 anyway, but it can on card 12.
**Execution.** Walked the Sweep chain in single steps (no rejections): 'Sweep in which space' typed; then 'US Sweep Troops into' menu -> 'US Move troops to Binh Dinh from' (several sources offered, Da Nang included) -> 'Move how many US Troops'; Finished twice.
**Result.** As planned: Binh Dinh COIN Control, NVA 16 -> 14, ARVN 44 -> 46.

## Coup 1 — #126 Young Turks, Support phase — before save-034
**Plan.** Pacify Saigon 1 level (Passive -> Active) and Da Nang 2 levels (Neutral -> Active); the only two candidates.
**Why.** 45 ARVN Resources above Econ; +8 US for 9 Resources. Nothing else qualifies (no Police with US Troops elsewhere).
**Execution.** none (cost 3 per level under Young Turks).
**Result.** Saigon Active, Da Nang Active (+8 US); ARVN then pacified An Loc.

## Coup 1 — Commitment — before save-034
**Plan.** Move nothing.
**Why.** Every Troop placed costs a point and a withdrawal costs a population shift the VC would aim at Saigon; the 4 Troops in Binh Dinh (now with 4 ARVN Police) and 2 in Da Nang already serve the next Support phase. Quang Tri's pieces cannot move (NVA Control).
**Execution.** none
**Result.** No moves, no withdrawal shifts.

## Turn 6 — card #109 Nguyen Huu Tho — before save-040
**Plan.** Op + SA: Train Binh Dinh (no placement), Pacify it 2 levels to Active; Advise Ranger removal in Saigon (VC Guerrilla + Base) and Quang Nam (2 NVA Troops), +6 Aid.
**Why.** A VC Guerrilla in Saigon exposes 12 points to Terror and Coup Agitation; clearing it (and the Base, -1 VC) comes first. Binh Dinh +4 US; Quang Nam back to COIN Control (-1 NVA). Passing for ROKs was weighed and rejected: Saigon cannot wait.
**Execution.** Pacify space auto-selected (one candidate), so seq stopped: "no menu entry starts with 'Binh Dinh'" (nothing sent); resumed at the level menu. Changed the second Advise space from Quang Nam to Quang Tri (pop 2, same 2-Troop removal) when both were offered.
**Result.** Binh Dinh Active (+4, US 49); Saigon cleared (VC -1); Quang Tri back to COIN Control (NVA 15 -> 13, ARVN 47); Aid +6.
