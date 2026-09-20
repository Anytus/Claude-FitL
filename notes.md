# notes.md — one line per US turn (cross-session memory)

Format: `card #<n> <title>: <action in a few words> — <why, ten words or fewer>`

Also log here: session resumes (with the save number resumed from), vetoes,
and anything Kevin asked administratively.

session 1: new-game TestGame1 created (Full 1964-1972, US human, human win in any Coup allowed). Agitate Total rolled = 1. No save yet; program awaits first two card numbers.
card #63 Fact Finding: Train Saigon (2 Police) + Quang Tri (2 Irregulars, meant Pleiku), Pacify Saigon to Active Support, Air Strike degrade Trail to 0 — Coup next; +6 Support cheapest big gain
Coup 1 (#125): Pacified Da Nang, Kontum to Active; Commitment pulled 1 Troop each from Da Nang, Kontum to Available — withdrawal rule cost 1 Support (Kontum to Passive); net +1. LESSON: 2 pieces withdrawn = VC shifts 1 pop 1 level.
ADMIN (Kevin, after Coup 1): stop pasting diff.py output in reports; paste the program's own narration for each segment instead — it has everything needed for the board.
RESUME: container/tmux lost after Coup 1 narration but before the Coup save was written. Resumed from save-002 (start of 1st Coup round, current #125, on deck #75). Whole Coup round replayed; bot choices and dice may differ from the first report.
Coup 1 replay (#125): same pacification; Commitment withdrew only 1 Troop (Da Nang) — no withdrawal penalty at 1 piece. US 51.
card #75 Sihanouk: US did not act (ARVN Op+Govern, NVA shaded event exhausted card) — ARVN Govern took 4 Support and 4 Aid; NVA Trail 2, guerrillas into Tay Ninh, Pleiku.
card #112 Colonel Chau: PASS — stay eligible to take #93 Fulbright unshaded (+4) and deny NVA the shaded (base OOP, Aid -9)
RESUME 2: container lost again while waiting for the card after #93. Resumed from save-006 (US turn on #112, on deck #93); replayed the Pass identically (no dice). Board unchanged.
ADMIN: no manual save exists in the program (checked `?` at the perform prompt and at the card prompt). Set up a 5-minute in-session heartbeat cron (job 500f0e68) as an experiment to keep the container alive while Kevin updates the board.
RESUME 3: container lost again (heartbeat cron never fired; it dies with the container). Resumed from save-006, replayed Pass on #112 identically. Heartbeat idea abandoned.
card #93 Senator Fulbright: EVENT unshaded — Binh Dinh Troop, Pleiku Troop+Base, Kontum Troop to Available (+4, US 50) — denies NVA shaded (base OOP, Aid -9). NVA passed; ARVN Train+Govern (Quang Tri to Passive Support, Khanh Hoa/Can Tho Support removed).
RESUME 4: container lost after #93 report. Resumed from save-009 (NVA had passed; ARVN turn unsaved). ARVN replay DIFFERED: activation roll 3 [Failure] after Saigon (was 5,5,4), so only Saigon trained (+3 Troops +3 Police), no Quang Tri/Hue/An Loc training, no Quang Tri pacification; Govern hit Khanh Hoa and Phu Bon-Phu Yen (was Khanh Hoa and Can Tho). Entered card #1 immediately to lock the replayed state into save-010 (NVA turn on #51). US 48, ARVN 44, VC 33, Aid 9, Patronage 25, ARVN Resources 30. Did NOT advance; awaiting Kevin's decision (accept replay vs. he runs `adjust`).
FIX ATTEMPT: edited tools/ctl.py so `advance` enters the top line of reserve_cards.txt at the On Deck card prompt (after git pull) and keeps going; the playing session must never read that file. Untested: the permission classifier blocked running it.
ADMIN: Kevin rebuilt the program (1.53+sbd) to save before the card prompt; cherry-picked commit 97d8b84 onto this branch. Reverted the reserve-card edit to ctl.py (unneeded). Kevin's earlier instruction stands: report program narration, not diff.py.
card #51 301st Supply Bn: US ineligible (no action). NVA Rally (bases Southern+Central Laos, Trail 3) + Infiltrate (5 Troops N.Vietnam, 5 Parrot's Beak); VC March 1 guerrilla to LOC Ban Me Thuot--Da Lat. Patched build confirmed: save-012 written at the card prompt.
ADMIN (Kevin-directed): rollback to save point 10 and adjust to restore the ORIGINAL ARVN turn on #93 (Quang Tri/Hue/An Loc trained, Quang Tri pacified to Passive Support, Govern Khanh Hoa + Can Tho, ARVN Res 15). Verified via show summary. #51 bot actions discarded and replayed from here.
card #51 (replayed after restore): US ineligible. NVA Rally (base Southern Laos, roll 1 fail, Trail 3) + Infiltrate (5 Troops Central Laos, 5 North Vietnam); VC March 1 guerrilla to LOC Ban Me Thuot--Da Lat. save-021 at card prompt.
RESUME 5: program down between turns; resumed from save-021 (card prompt after #51). Nothing lost.
card #1 Gulf of Tonkin: PASS — stay eligible to take #29 Tribesmen unshaded (3 VC bases under my Irregulars) and deny VC shaded. ARVN Sweep Binh Dinh + Raid (NVA base S.Laos, VC base Quang Duc removed).
card #29 Tribesmen: EVENT unshaded — removed VC Bases in Quang Tri, Binh Dinh, Pleiku + 1 Quang Tri guerrilla (VC 27) — best exchange available; denied VC shaded. VC rallied 9 guerrillas + Subvert.
RESUME 6: resumed from save-027 (card prompt after #29). Nothing lost.
card #66 Ambassador Taylor: US ineligible. ARVN Train Saigon + Govern (Quang Tri, Cam Ranh support removed, Aid 6); NVA shaded event removed Support in Da Nang, Kontum, Phu Bon, Patronage -3. US 42.
RESUME 7: resumed from save-030 (card prompt after #66). Nothing lost.
card #17 Claymores: EVENT unshaded (Stay Eligible + momentum) — free action, keeps me eligible for #68 Green Berets unshaded; VC March into Saigon lost 4 guerrillas to the momentum.
RESUME 8: resumed from save-033 (card prompt after #17). Nothing lost.
card #68 Green Berets: PASS — LESSON: after 1st-eligible Op Only, 2nd gets only LimOp (no Event); planned unshaded event impossible. Pass keeps me 1st on #15 with full Op+SA. NVA LimOp Rally S.Laos, Trail 4.
RESUME 9: resumed from save-037 (card prompt after #68). Nothing lost.
card #15 Medevac: Assault Saigon (2 VC removed) + Air Strike (Trail 4->3, 4 LoC guerrillas) — Train/Pacify REJECTED (ARVN res 12 < Econ 15), aborted and redid. LESSONS: pacify needs ARVN Res > Econ; trail degrade costs 2 hits, do first.
card #43 Economic Aid: US ineligible. NVA Rally (base S.Laos, guerrillas) + Infiltrate 10 Troops Parrot's Beak, 9 Central Laos, Trail 4; ARVN unshaded event: 2 ARVN Bases OOP->Available, Aid +12 (18).
card #6 Aces: EVENT unshaded — free Air Strike Parrot's Beak (6 NVA Troops), Trail 4->2 — denies NVA shaded (2 Troops to Casualties). VC Rally 2 Bases + Tax (Agitate 5). Slip: sent perform before entering card 34 (rejected, no effect).
RESUME 10: resumed from save-046 (card prompt after #6). Nothing lost.
card #34 SA-2s: US ineligible. NVA shaded capability (Rally improves Trail 2); ARVN passed (Res 15).
card #78 General Lansdale: US no action (ARVN shaded event: Patronage +3, no US Assault until Coup; VC Rally 11 guerrillas + base Tay Ninh, Subvert Binh Dinh/Hue; Binh Dinh COIN control lost).
card #5 Wild Weasels: EVENT unshaded — removed SA-2s capability — Ops were useless (no Assault, no pacify). NVA March: 11 Troops into Quang Tri (NVA Control), 3 Tay Ninh, 5 Kien Giang; NVA 14.
RESUME 11: resumed from save-055 (card prompt after #5). Nothing lost.
card #14 M-48 Patton (Monsoon): US ineligible. ARVN Patrol (Hue--Khe Sanh, NVA guerrilla killed; Quang Tri stripped of its last ARVN Troop+Police); VC Terror Binh Dinh (Active Opposition). Nobody took the event. Coup #127 next.
Coup 2 (#127 Ky): pacified Da Nang, Kontum to Active (US +4); VC Agitate put Quang Tri/Kien Hoa at Active Opp, VC 38 (+3, would win). Commitment: US Base + 1 Troop to Quang Tri to enable Train Police + Pacify there (-4 VC/+2 US lever). US 47.
RESUME 12: resumed from save-060 (card prompt after Coup 2). Nothing lost.
card #102 replaced by NVA PIVOTAL #122 Easter Offensive (roll 1): free March 5T+1G Binh Dinh, 8T Quang Tin, 2T+1G Quang Nam, 2T NE Cambodia; free Attacks (Irregular in Binh Dinh to Casualties, Police in Quang Nam). NVA 17 (-1). VC Terror Hue/Qui Nhon/Ba Xuyen/Pleiku/Quang Tin + Subvert Hue (control lost), Quang Tri (last Police gone). VC 40, US 44. US did not act (3rd).
ADMIN/RULES NOTE from Kevin (unsolicited): NVA Troops MAY redeploy to NVA Bases at the Coup Redeploy phase but need not; NVA Control from Troop stacks in SVN does not expire on its own. My earlier assumption that they must go home was wrong.
OBSERVER COMMENT (Kevin, unsolicited, not acted on): as NVA he would not have challenged Quang Tri with a US Base present (counter-attack efficient) but would have without it; trading with US forces feeds Casualties (Aid loss, 1/3 Out of Play at Coup).
RESUME 13: resumed from save-064 (card prompt after #122). Nothing lost.
card #8 Arc Light: declined Linebacker II (keep for later; condition Support+Avail>40 at 44). Started Train Quang Tri (3 Police, trail degrade) then ABORTED and PASSED after Kevin's mid-turn warning made me re-check sequencing: passing let ARVN take Arc Light (capability mine) and made ARVN ineligible on #70, so US is first on #70 to take ROKs unshaded and deny VC +3.
card #70 ROKs: EVENT unshaded — Sweep Kontum Police + Da Nang Troop into Binh Dinh, killed 1 NVA Troop + Qui Nhon VC guerrilla, broke NVA control (15). VC PASSED; NVA March+Ambush: US Troop in Binh Dinh to Casualties, Da Nang Police killed, Da Nang + Pleiku NVA Control (NVA 17 again). Declined Linebacker again.
RESUME 14: resumed from save-071 (card prompt after #70). Nothing lost.
card #99 Masher/White Wing: US ineligible. VC Terror Hue (Passive Opp, VC 42) + Kien Giang, Subvert Binh Dinh/Quang Tri (2 ARVN Troops); ARVN unshaded event: Sweep 2 Troops Quang Tri->Hue, Assault killed 2 VC guerrillas, Hue COIN control.
RESUME 15: resumed from save-074 (card prompt after #99). Nothing lost.
card #7 ADSID: Train Quang Tri (2 Police, pacify to Passive Opp, VC 40) + Arc Light Air Strike Quang Tin (6 NVA Troops, control broken, NVA 15). Declined Linebacker again. NVA shaded ADSID: Trail 3, ARVN Res 8 (pacify blocked).
RULES NOTE from Kevin (unsolicited): the Advise Special Activity offers an option to add +6 to Aid. I had not opened Advise's prompts before. Aid only converts to ARVN Resources at the Coup, so it does not unblock pacification now.
RULES NOTE from Kevin (unsolicited, continued): Advise also allows 2 free ARVN Sweeps-in-place or Assaults, or activating an Underground Ranger/Irregular to remove 2 pieces (raid-like). To be verified against the program's own prompts next time I have an SA.
