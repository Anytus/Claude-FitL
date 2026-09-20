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
