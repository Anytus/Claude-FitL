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
