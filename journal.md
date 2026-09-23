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
