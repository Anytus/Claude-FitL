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

## Turn 8 — card #38 McNamara Line — before save-051
**Plan.** Limited Op Train in Kien Giang-An Xuyen (no placement), Pacify Neutral → Passive Support (1 level; only 5 Resources above Econ).
**Why.** +2 US; Kien Giang has no Police so the Coup Support phase can't reach it. Acting also ends the card before the VC. Pass-for-Starlite weighed: the Event's best target (QTQN) would hand the NVA Control there; not worth the VC action. Event (ARVN -12) rejected: cuts the Coup pacify budget.
**Execution.** none
**Result.** As planned: Kien Giang Passive Support (US 38→40), ARVN Resources 17.

## Turn 9 — card #69 MACV — before save-056
**Plan.** Op + SA: Train Saigon (no placement, no final action), Advise with a Kien Phong Irregular on its NVA Guerrilla; +6 Aid.
**Why.** Pacify and ARVN placement are blocked (Resources 17, Econ 15) and Assault by Lansdale, so the action is for the Advise and the +6 Aid (Coup pacify budget). Taking Op+SA leaves the NVA only a LimOp or the Event. MACV Event (free US SA, stay Eligible) weighed: hands the NVA a full Op+SA, and US is last on Plei Mei anyway.
**Execution.** Final Train menu offered Transfer patronage (no Pacify); took 3 (Patronage 19→16, Resources 20). seq stopped at "Use Irregular/Ranger in which space": auto-selected Kien Phong (only candidate). Added an ARVN Advise Assault in Phu Bon-Phu Yen (only candidate): 0 hits (1 Police).
**Result.** NVA Guerrilla out of Kien Phong; ARVN 44→41; Aid 28.

## Turn 10 — card #82 Domino Theory — before save-063
**Plan.** Limited Op Sweep into Kien Phong: US Troops 2 from Kien Giang, 1 from Saigon, 1 from Can Tho (6 Troops + 2 Irregulars vs 5 NVA Troops).
**Why.** NVA is at 22 (threshold 18) and the Coup is one of the next 4 draws; ARVN's Op-only leaves me a LimOp, Assault banned (Lansdale). Breaking a pop-2 NVA Control is the most one space gives (-2). Kien Phong over Kien Giang/Binh Dinh: keeps the Kien Hoa Troops for Coup pacification and guards 4 points of Active Support. Pass rejected: US is last on #86.
**Execution.** none
**Result.** As planned: Kien Phong COIN Control, NVA 22→20 (still 2 over).

## Turn 11 — card #102 Cu Chi (Coup #125 on deck, Monsoon) — before save-069
**Plan.** Limited Op Train in Binh Dinh: place 2 Irregulars (none Available, so 2 come off the map elsewhere); no final action.
**Why.** Last action before the Victory check; NVA 20 > 18. Binh Dinh becomes 4 US pieces vs 3 NVA, breaking NVA Control (pop 2): NVA 18 = score 0, not a win. Sweep (Monsoon) and Assault (Lansdale) are unavailable; the Event does nothing. Acting also ends the card before ARVN.
**Execution.** Mechanic: placing Irregulars with none Available prompts "You must remove 2 US Irregulars from the map" and lets the US pick the spaces; removed the Active ones in Kien Giang and QTTT (no Control change). Declined Pacify (no Resources above Econ).
**Result.** As planned: Binh Dinh COIN Control, NVA 20→18 (score 0) going into the Coup.

## Turn 12 — 2nd Coup #125 Nguyen Khanh — Support phase — before save-071
**Plan.** Pacify Hue Passive→Active (3), Kontum Neutral→Active (6), Kien Hoa-Vinh Binh Passive Opposition→Passive Support (6): 15 of 45 above Econ.
**Why.** +6 US, −2 VC; none holds VC Guerrillas, so the Agitate Total (10, 2 Guerrillas per space under Cadres) can't reach them.
**Execution.** Resumed at the start of the Coup (container reclaimed); the round re-ran identically up to this prompt.
**Result.** As planned: US 42→48. VC Agitated Tay Ninh and QTQN (VC 20→24). NVA Redeploy pulled 19 Troops to Laos/Cambodia; NVA 17.

## Turn 12b — 2nd Coup #125 — Commitment — before save-071
**Plan.** Place the 4 Troop casualties in Da Nang; move 2 Troops Kontum→Da Nang and 1 Hue→Da Nang (7 of 10). Nothing from Available, no Base.
**Why.** Da Nang borders QTQN (6 NVA Troops, NVA Control, 2 VC Bases): with Assault back after Reset, Air Lift ~9 Troops in + Assault (Lowland) breaks NVA Control; Kien Phong's 5 Troops can do the same to Kien Giang in that action. Kontum/Hue stay Active with ARVN holding Control. Keeps 13 points in Available.
**Execution.** Process slip: the journal write failed (script quoting error) and the same command sent the first answer ("Da Nang") before this entry existed; written immediately after, before any further answer.
**Result.** As planned: Da Nang holds 9 US Troops; Available untouched.

## Turn 13a — pivotal offer at draw of #90 (current #100 Rach Ba Rai) — before save-072
**Plan.** Decline Linebacker II.
**Why.** It would cost this turn's US action (Air Lift + Assault on QTQN/Kien Giang, ~−4 NVA) for −2 NVA Bases, and its 3-Casualties-to-Available would be wasted (box empty). Kept for a later NVA surge; its precondition (Support+Available >40) should stay met.
**Execution.** none
**Result.** Declined; #100 Rach Ba Rai proceeds.

## Turn 13 — card #100 Rach Ba Rai — before save-074
**Plan.** Op + SA: Air Lift first (Da Nang 9 Troops → QTQN; Kien Phong 4 Troops → Kien Giang), then Assault QTQN (9 hits vs 6 NVA Troops) and Kien Giang (4 hits vs 3 NVA Troops).
**Why.** Breaks NVA Control in both pop-2 spaces (NVA 17→13) and strips 9 NVA Troops, giving margin under 18 for this campaign; COIN Control in QTQN sets up later Train/Pacify there. Underground Guerrillas shield the VC Bases, so no Base kills expected.
**Execution.** Added: Air Lifted 1 Underground Irregular Kien Phong→Kien Giang (future Advise vs its NVA Guerrilla). Kien Giang Assault auto-selected as the only remaining space.
**Result.** As planned: 9 NVA Troops removed, NVA Control broken in QTQN and Kien Giang; NVA 17→13; COIN Control in both.

## Turn 14a — pivotal offer at draw of #95 (current #46 559th Transport Grp) — before save-078
**Plan.** Decline Linebacker II.
**Why.** NVA at 12 (6 under); Casualties box empty so its recovery half is wasted; keep it for a real NVA surge.
**Execution.** none
**Result.** Declined.

## Turn 14 — card #46 559th Transport Grp — before save-080
**Plan.** Op + SA: Train Binh Dinh (no placement) and Pleiku-Darlac (2 ARVN Police via the US Base, 3 Resources); Pacify Binh Dinh Active Opposition → Neutral (6). Advise with Irregulars in Kien Phong and Kien Giang (remove their NVA Guerrillas); +6 Aid.
**Why.** −4 VC in a space with Police, so on-deck Westmoreland shaded (VC Critical: 3 Provinces without Police, 2 levels toward Opposition) can't reverse it; Police shields Pleiku's Support. Advise cleans the delta. Event (Trail −2) weighed: NVA at 12 is not the pressing threat.
**Execution.** VC passed first, so the pivotal was offered a second time; declined again. Placed 2 ARVN Troops + 2 Police in Pleiku. Deviation: Advise menu offered Quang Nam's Ranger; used it on 2 NVA Troops there instead of the Kien Phong Guerrilla.
**Result.** Binh Dinh Neutral (VC 24→20); Pleiku has Police; 2 NVA Troops out of Quang Nam, NVA Guerrilla out of Kien Giang; Aid 16.

## Turn 15a — pivotal offer at draw of #9 (current #53 Sappers) — before save-087
**Plan.** Decline Linebacker II.
**Why.** It would replace #53, whose unshaded Event (−2 NVA Troops in each of 3 spaces, US stays Eligible) I can take after the VC's Op, and keep me first on #9 Psychedelic Cookie (unshaded: 3 Out-of-Play Troops to Available, +3). Linebacker kept for later.
**Execution.** none
**Result.** Declined.

## Turn 15 — card #53 Sappers — before save-088
**Plan.** Event unshaded: remove 2 NVA Troops each from Quang Tin-Quang Ngai, Quang Nam and Quang Duc-Long Khanh; US stays Eligible.
**Why.** Thins the stacks beside my 5 exposed Troops in QTQN, breaks NVA Control in QDLK (−1), and keeps me first Eligible on #9 (unshaded: +3 US Troops to Available). LimOp weighed: one space, loses the #9 Event.
**Execution.** Rejected: at "1st Selection:" seq typed the name; program: "'Quang Tin-Quang Ngai' is not valid. Must be one of: 1, 2, 3, 4, or abort". Mechanic: "Nth Selection:" prompts need the on-screen number; sent 3, 2, 1 via send, checking each renumbered menu.
**Result.** As planned: 6 NVA Troops removed, QDLK NVA Control broken (NVA 11→10); US stays Eligible.

## Turn 16 — card #9 Psychedelic Cookie (Coup #127 on deck, Monsoon) — before save-090
**Plan.** Event unshaded: move 3 US Troops from Out of Play to Available.
**Why.** +3 US; all bots are far below their lines (NVA 10, VC 20, ARVN 40), so no push-back is needed before the Victory check. Taking it also denies the NVA (second, Performed/Shaded) the shaded side (3 US Troops to Out of Play). Train+Pacify Binh Dinh weighed: its 2 VC Guerrillas let the Coup Agitate undo it, and the NVA would then get the shaded Event.
**Execution.** none
**Result.** As planned: 3 Troops Out of Play → Available (+3 US).

## Turn 17 — 3rd Coup #127 Nguyen Cao Ky — Support phase — before save-092
**Plan.** Pacify Kien Hoa-Vinh Binh Passive → Active Support (1 level, 4 under Ky).
**Why.** +2 US; only candidate; no VC Guerrillas there for Agitate.
**Execution.** none
**Result.** As planned: Kien Hoa Active (US 49→50). VC Agitated QTTT and Phu Bon (VC 20→25). NVA Redeploy emptied QTQN and Tay Ninh of NVA Troops.

## Turn 17b — 3rd Coup #127 — Commitment — before save-092
**Plan.** Place the 3 Troop casualties in Da Nang; move 2 Troops Kien Giang→Da Nang. Nothing from Available.
**Why.** Stages 5 in Da Nang beside QTQN (my 5 Troops vs 11 Guerrillas, 2 VC Bases, already Active Opposition): Sweep 11 in to activate all, then Air Strike at no Support cost. Delta has no enemy pieces; Air Lift can return Troops there. Keeps Available points.
**Execution.** none
**Result.** As planned: Da Nang 5 US Troops, Kien Giang 2.

## Turn 18 — card #25 TF-116 Riverines (pivotal offer, then first Eligible) — before save-099
**Plan.** Decline Linebacker II; Pass on #25.
**Why.** On-deck #28 Search and Destroy shaded (VC Critical) is a lasting capability shifting every US/ARVN Assault Province toward Opposition — it would tax my main anti-NVA tool for the rest of the game. Passing keeps me first on #28 (printed order US first); by the Tru'ng rules the VC (Op+SA) and NVA (LimOp) act on #25 and are then Ineligible on #28, so I can take a full Air Lift + Assault there (fallback: take the unshaded Event myself). Cost: one tempo with NVA at 20; next Coup is 5+ cards away. Linebacker would make me Ineligible on #28.
**Execution.** Reasoning error: the briefing listed VC and NVA as Ineligible on #25 (they acted on Tet); I missed it. They cannot act on #25, so both are Eligible on #28 with the VC second behind me. The pass still guarantees me first on #28, but only the fallback remains: take S&D unshaded myself, no Op.
**Result.** Passed (+3 ARVN Resources); ARVN acts alone on #25.

## Turn 19 — pivotal Linebacker II at draw of #72 (replacing #28 Search and Destroy) — before save-101
**Plan.** Play Linebacker II.
**Why.** Replaces #28, so its shaded capability (VC Critical, second in order) never plays; NVA removes 2 Bases (20→18) and is Ineligible through #72; my 2 Casualties go to Available (+2). S&D unshaded weighed: weak capability (helps only when an Assault would remove nothing) and leaves NVA at 20 with a free hand.
**Execution.** seq stopped at "Choose one=>Event": the pivotal executes directly on perform (no menu).
**Result.** As planned: NVA removed Bases in Southern and Central Laos (NVA 20→18), NVA Ineligible through #72, 2 Troops Casualties→Available (US 47→49).

## Turn 20 — card #114 Tri Quang — before save-109
**Plan.** Op + SA: Train Saigon (no placement), Pacify Saigon Passive → Active (4); Advise with the Irregulars in Kien Phong and Kien Giang, removing 2 NVA Troops each; +6 Aid.
**Why.** +6 US back in Saigon (Govern-proof; its lone VC Guerrilla can't Terror under Cadres). The Advise breaks NVA Control in both delta spaces (NVA 14→10). Air Lift + Assault on Hue's VC Base (−1 VC) weighed: less value; VC at 30 grows slowly (1 Base left Available).
**Execution.** seq stopped at "Pacify in which space": Saigon auto-selected (only candidate); continued with a second seq.
**Result.** As planned: Saigon Active (US 40→46); NVA Control broken in Kien Phong and Kien Giang (NVA 14→10); Aid 13.

## Turn 21 — card #104 Main Force Bns — before save-116
**Plan.** Op + SA: Air Lift first (Da Nang 4 Troops → Kien Phong, 1 → QTQN), then Assault Kien Phong (5 hits vs 5 NVA Troops), QTQN (4 hits vs 4 NVA Troops) and Kien Giang (2 hits vs 3 NVA Troops).
**Why.** ~11 NVA Troops killed; breaks NVA Control of Kien Phong (Active Support, pop 2; NVA 13→11) and strips the stacks sitting on my Support. No bot near its line, so the tempo goes to attrition. Train+Pacify weighed: only +1 available now (Da Nang); the Coup Support phase will pacify.
**Execution.** seq stopped once: after Da Nang emptied, the Air Lift returned straight to the space menu (no 'Finished moving' step); continued with a second seq.
**Result.** As planned: 11 NVA Troops removed (Kien Phong 5, QTQN 4, Kien Giang 2); Kien Phong back to COIN Control (NVA 13→11).

## Turn 22 — card #42 Chou En Lai — before save-122
**Plan.** Pass.
**Why.** Eligibility checked this time: US and VC Eligible, NVA not. On-deck #27 Phoenix Program prints US first; VC is Critical on its shaded side (Hue → Active Opposition + Terror). Passing keeps me first there to take the unshaded side (3 VC pieces from COIN Control spaces: Hue's 2 Guerrillas + Base). If the VC takes a LimOp now it is Ineligible on #27 anyway. Cost: a LimOp or Chou En Lai (−d6 NVA Troops) now.
**Execution.** none
**Result.** Passed (+3 ARVN Resources); VC to act.

## Turn 23 — card #27 Phoenix Program — before save-124
**Plan.** Op + SA: Train Saigon (no placement), Pacify Saigon: remove Terror + Passive → Active (8); Advise with ARVN Rangers in Hue (remove 2 VC Guerrillas) and QTTT (NVA Guerrilla, then an NVA Base); +6 Aid.
**Why.** +6 US in Saigon; VC −2 Guerrillas in Hue; NVA −1 Base. VC is Ineligible on #27, so the shaded threat is gone and the Event (3 VC pieces) is worth less than this.
**Execution.** Mechanic learned on #42: under Cadres a lone VC Guerrilla can still Terror (it is removed afterward) — my Turn 20 note was wrong. Stray answer: QTTT was auto-selected (only candidate) and my seq's next step typed "Quang Tri-Thua Thien" into the "+6 Aid? (y/n)" prompt, which re-prompted; then answered y.
**Result.** As planned: Saigon Active (US 42→48), Hue's 2 VC Guerrillas and a QTTT NVA Base removed (NVA 11→10), Aid +6.
