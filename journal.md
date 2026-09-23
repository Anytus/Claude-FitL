# journal.md — turn plans and rationales (TestGame7)

Every US action, Coup-round decision, and pivotal-event decision gets a brief
entry here **before** the first answer is sent to the program, in the format
given in `CLAUDE.md`. Previous games' journals are under `archive/`.


## Turn 0 — card #130 Coup! Failed Attempt (1st Coup, drawn first) — Support phase — before save-001
**Plan.** Pacify Saigon Passive→Active (1 level, 3), Da Nang and Kontum Neutral→Active (2 levels each, 6+6); 15 of the 45 above Econ.
**Why.** +10 Total Support (Saigon 6→12 is +6, pop-1 cities +2 each); no VC Guerrillas in any of the three, so the VC Agitate can't reach them. Govern may later trim Da Nang/Kontum (ARVN Police), but Saigon is immune.
**Execution.** seq stopped at its last step: pacification ended by itself when no candidates remained (not a rejection). ARVN then pacified Hue; VC Agitated Binh Dinh to Active Opposition.
**Result.** As planned: +10 Support (US points 38→50); VC points 27→31.

## Turn 0b — card #130 Coup! Failed Attempt — Commitment phase — before save-001
**Plan.** Move 10 Troops from Available: 5 to Can Tho, 5 to Saigon; no Bases.
**Why.** VC at 31/35 is the danger; Can Tho borders Kien Phong and Kien Giang (pop 2 each, Active Opposition, 1 lone Guerrilla each), Saigon borders Tay Ninh/QDLK/BTBT/Kien Phong. Troops in Available score only at the end; 12+ event cards remain before the next Coup to use them.
**Execution.** `send "Finished moving pieces"` rejected: "'Finished moving pieces' is not valid. Must be one of: 1 or 2". Mechanic: `send` does not label-match; re-sent through `seq "*=>Finished moving pieces"`, accepted.
**Result.** As planned; US points 50→40, no withdrawal shift. Then #110 No Contact: VC passed, NVA Rally+Infiltrate, ARVN Train; card closed before the US.

## Turn 1 — card #112 Colonel Chau — before save-008
**Plan.** Op + SA: Sweep Kien Phong (3 Troops from Saigon), Kien Giang-An Xuyen (2 from Can Tho), Ba Xuyen (1 from Can Tho), Kien Hoa-Vinh Binh (1 Saigon + 1 Can Tho); then Air Strike the now-Active Guerrillas in Kien Phong and Kien Giang (already Active Opposition, so no shift); spare hits on the Trail.
**Why.** Lowland sweep activates 1 per Troop; gives COIN Control in four pop-2/1 delta spaces and clears the two pop-2 Active Opposition spaces for Train+Pacify next. Not striking Kien Hoa/Ba Xuyen (Neutral: strike would shift them to Opposition). VC 31/35 is the threat.
**Execution.** Program was not running at start (container reclaimed); resumed from save-007. Air Strike rolled 6 hits; 1 Kien Phong, 1 Kien Giang, 2 Trail (2→1), 2 unused. Mechanic: Sweep selects all spaces first, then asks per destination which adjacent source.
**Result.** As planned: 4 delta spaces COIN-controlled, 2 VC Guerrillas removed, Trail 1, no Support shift.

## Turn 2 — card #93 Senator Fulbright — before save-014
**Plan.** Limited Op Train in Kien Phong: 2 Irregulars, then Pacify Kien Phong Active Opposition → Neutral (2 levels, 6 ARVN Resources).
**Why.** -4 VC points (VC is nearest its line); Irregulars give a future Advise piece in the delta. Event (4 US pieces to Available, +4 US) rejected: pulls Troops that are holding the delta.
**Execution.** seq stopped at "Pacify in which space": program auto-selected the only candidate (Kien Phong); pacify label was "Shift 2 levels to Neutral"; continued with a second seq.
**Result.** As planned: Kien Phong Neutral, VC points 29→25, ARVN Resources 33.

## Turn 3 — card #63 Fact Finding — before save-020
**Plan.** Op + SA: Train Kien Giang-An Xuyen (1 Irregular, last Available), Pacify it Active Opposition → Neutral (6); Advise with Irregulars in Binh Dinh and Quang Tri-Thua Thien, removing 2 VC Guerrillas each; +6 Aid.
**Why.** -4 VC from the pacify; the Advise strips 4 VC Guerrillas (Terror/Agitate carriers) and gives COIN Control in Binh Dinh (pop 2, Active Opp) and QTTT, exposing their Bases. Alternative (Assault Active VC in Kien Hoa/Ba Xuyen) weighed: fewer pieces, no Support gain.
**Execution.** seq stopped at "Place how many Irregulars (0 - 2)" (expected a skip; 1 Available); sent 1. Deviation: Advise menu offered Pleiku-Darlac, whose VC Base stood alone; removed that Base instead of the QTTT Guerrillas.
**Result.** Kien Giang Neutral (VC 25→21), Binh Dinh COIN Control, Pleiku VC Base removed (VC 21→20), Aid 21. Card closed before VC acted.
