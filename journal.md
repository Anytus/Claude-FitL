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

## Turn 4 — card #107 Burning Bonze — before save-027
**Plan.** Op + SA: Train Saigon (no placement), Pacify Saigon Passive → Active (3); Advise Irregular in Kien Giang (remove 2 NVA Troops) and in QTTT (remove 2 VC Guerrillas); +6 Aid.
**Why.** +6 US back in Govern-proof Saigon; Kien Giang Advise breaks NVA Control (NVA -2) and blunts the stack beside my 2 Troops; QTTT strips VC Terror carriers. NVA is Ineligible on #116. Alternative (Assault KG/KH/BX + Advise) weighed: more kills, no Support.
**Execution.** none
**Result.** As planned: Saigon Active (US 30→36), NVA Control lost in Kien Giang (NVA 11→9), 2 VC Guerrillas out of QTTT, Aid 15.

## Turn 5 — card #43 Economic Aid — before save-033
**Plan.** Limited Op Train in Kien Phong (no placement, none Available), Pacify Neutral → Active Support (6).
**Why.** +4 US in a space with no ARVN cubes (Govern-proof) and no VC; Kien Phong lacks Police so the Coup Support phase can't reach it, while Kien Hoa/Ba Xuyen can be done there. Alternative (Assault KG to take COIN Control) weighed: no score for US.
**Execution.** none
**Result.** As planned: Kien Phong Active Support, ARVN Resources 24.

## Turn 6 — card #97 Brinks Hotel — before save-039
**Plan.** Limited Op Assault in Saigon: 3 US Troops with the US Base = 6 hits on the 3 Active VC Guerrillas.
**Why.** 3 VC Guerrillas in Saigon threaten Terror and the Coup Agitate (total 4) against 12 points of Active Support; a Coup can come any draw now. Event (Aid +10 or 4 Patronage to Resources) weighed: nothing to do with Saigon.
**Execution.** none
**Result.** As planned: 6 hits, 3 VC Guerrillas removed from Saigon.

## Turn 7 — card #105 Rural Pressure — before save-045
**Plan.** Op + SA: Assault Kien Hoa-Vinh Binh (1 Active VC) and Kien Giang-An Xuyen (1 NVA Troop); Advise with a Kien Phong Irregular on its NVA Guerrilla; +6 Aid.
**Why.** ARVN is Critical on Lansdale shaded next card (no US Assault until the Coup), so Assault now. Takes COIN Control in Kien Giang and keeps Kien Hoa clean for the Coup Support phase. Pacifying now is capped at 1 level (ARVN Resources 20, Econ 15); the +6 Aid feeds the Coup pacification budget.
**Execution.** seq stopped at "Choose special activity=>Advise": "no menu entry starts with 'Advise'" (menu offered Air Lift, Air Strike only). Mechanic: Advise is not offered with Assault (only Train/Patrol, inferred). Deviation: Air Lifted the QTTT Troop to Hue instead, so Hue qualifies for Coup pacification (COIN, Police, US Troop); no Aid.
**Result.** VC Guerrilla out of Kien Hoa; 1 NVA Troop out of Kien Giang (COIN Control); 1 US Troop now in Hue.
