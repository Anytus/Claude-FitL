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
