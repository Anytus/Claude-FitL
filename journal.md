# journal.md — full turn plans and rationales (TestGame6)

Every US action, Coup-round decision, and pivotal-event decision gets a brief
entry here **before** the first answer is sent to the program, in the format
given in `CLAUDE.md`. Previous games' journals are under `archive/`.


## Turn 1 — card #1 Gulf of Tonkin — before save-000
**Plan.** Op + SA: Train Saigon (no placement) and Pleiku-Darlac (2 Irregulars); Pacify Saigon Passive→Active; Advise Irregular removal in Quang Tri-Thua Thien and Binh Dinh (2 VC Guerrillas each), +6 Aid.
**Why.** Saigon to Active is +6 US at once for 3 ARVN Resources; Advise strips 4 Guerrillas from pop-2 spaces for free and sets up COIN Control. Event rejected: 6 OOP Troops to Cities scores nothing now, Op+SA scores 6.
**Execution.** seq stopped at step 15: after Pacify the program asks "Do you wish to perform a special activity? (y/n)" instead of returning to the final-action menu; answered y and continued. Pacify menu offered Pleiku-Darlac too (COIN Control after the 2 Irregulars).
**Result.** As planned: Saigon Active (US 38→44), 4 VC Guerrillas removed, COIN Control in Quang Tri and Binh Dinh, Aid +6.

## Turn 2 — card #43 Economic Aid — before save-007
**Plan.** Pass.
**Why.** Only a LimOp is open (worth +2 via Kontum pacify). Passing keeps US Eligible for #31 AAA (NVA, US, ...), where NVA is Critical/Shaded and should take the Event, leaving US a full Op + SA; worst case a LimOp there anyway.
**Execution.** Program was found not running before the first answer; resumed from latest save (save-007) with ctl.py resume, then passed.
**Result.** Passed as planned.

## Turn 3 — card #31 AAA — before save-009
**Plan.** Op + SA: Train Kontum (no placement) and Binh Dinh (last Irregular); Pacify Kontum Neutral→Active; Advise Irregular removal in Pleiku-Darlac (2 VC Guerrillas), +6 Aid.
**Why.** +2 US for 6 ARVN Resources while they sit above Econ; a fresh Underground Irregular in Binh Dinh for later Advise; Pleiku keeps COIN Control. Rejected: Advise + Assault on the Pleiku VC Base (VC −1, US +0).
**Execution.** Stop 1: Irregular placement asked "Place how many Irregulars (0 - 2)" though 1 Available; sent 1. Stop 2: pacify step "*=>" did not match the "Pacify:" menu; resent with "Pacify:". Stop 3: Pleiku-Darlac was the only Advise candidate and was auto-selected, so my explicit space step found no menu; finished Advise with send, then y to +6 Aid.
**Result.** As planned: Kontum Active Support (+2), 2 VC Guerrillas out of Pleiku, Aid 27.

## Turn 4 — card #118 Korean War Arms — before save-016
**Plan.** Event, unshaded: VC removes 1 Guerrilla from each space with 2+ and no NVA Base (8 spaces).
**Why.** ARVN Resources sit at Econ (15), so no Pacify is possible; a LimOp has no target. The Event strips 8 Guerrillas, including from Quang Tri and Binh Dinh. Passing gains nothing: on #50 NVA and VC act before US.
**Execution.** none
**Result.** As planned: 8 VC Guerrillas removed.

## Turn 5 — card #68 Green Berets (Coup on deck) — before save-022
**Plan.** LimOp Patrol: 2 US Troops Kontum → Hue (via Qui Nhon and Da Nang); decline any Assault.
**Why.** Sets up the Coup Support phase: ARVN income (Econ 15 + Aid 35) will leave ~47 above Econ, and Hue (pop 2, COIN, Police, terror) plus Da Nang then qualify for US pacification, worth about +6. ARVN Resources are at 12, so no Pacify now; the Op-only ARVN action closed the Event.
**Execution.** none (program offered "Assault at one LOC" after the LimOp Patrol into Hue, the known bug; declined).
**Result.** As planned: 2 US Troops now in Hue.
