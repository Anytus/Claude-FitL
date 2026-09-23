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

## Coup 1 — #126 Young Turks, Support phase — before save-024
**Plan.** Pacify Hue (terror off, 2 levels to Active) and Da Nang (2 levels to Active); 15 of 47 spare ARVN Resources.
**Why.** The only two candidates; +6 US for Resources the bots would otherwise spend.
**Execution.** Stop: Hue menu reads "Remove 1 terror marker and shift 2 levels to Active Support" (not "Shift 2 levels"); resent with that label.
**Result.** As planned: Hue and Da Nang to Active Support.

## Coup 1 — Commitment phase — before save-024
**Plan.** Saigon's 2 US Troops → Can Tho 1, An Loc 1; Quang Tri's lone Troop → Available; Binh Dinh's Troop → Qui Nhon. Bases stay.
**Why.** Can Tho, An Loc and Qui Nhon (COIN, Police, Passive) become next-Coup pacify targets (+1 each); one Troop home is +1 with no withdrawal shift (penalty is per 2). Bigger withdrawals risk a VC shift in Saigon.
**Execution.** Quang Tri and Binh Dinh were not offered as sources (only COIN-controlled spaces are), so the Troop-to-Available and Binh Dinh moves were dropped; Da Nang 1 → Qui Nhon instead. Rejected: `send Can Tho` → "'Can Tho' is not valid. Must be one of: 1, 2, ... 28"; resent via seq label match.
**Result.** Saigon → Can Tho 1, An Loc 1; Da Nang → Qui Nhon 1; nothing withdrawn.

## Turn 6 — card #75 Sihanouk — before save-028
**Plan.** LimOp Train in Pleiku-Darlac: place 6 ARVN cubes (Troops + Police) at the US Base, then Pacify Pleiku Neutral→Active.
**Why.** NVA sits at 17 of 18; this breaks NVA Control of Pleiku (−1 NVA), gives COIN Control and +2 US for 9 ARVN Resources. Acting also ends the card before VC can take the shaded Event (free Rally/March for VC and NVA). Rejected: LimOp Assault in Pleiku (2 Troops killed, no US gain).
**Execution.** Stops at the ARVN Troops/Police counts and the final-action menu (seq written only to placement); answered 3 Troops, 3 Police, Pacify, 2 levels. No rejections.
**Result.** As planned: Pleiku COIN Control and Active Support; US 50, NVA 16.

## Turn 7 — card #48 Nam Dong — before save-034
**Plan.** Pass.
**Why.** Only a LimOp is open and no US Troops remain where it would matter. Passing keeps US Eligible for #93 Senator Fulbright (VC, US, ...): VC is marked Ignored so it takes an Op + SA, leaving US the unshaded Event: 4 US pieces map → Available, +4 US with no withdrawal shift.
**Execution.** none
**Result.** Passed as planned.

## Turn 8 — card #93 Senator Fulbright — before save-037
**Plan.** Event, unshaded: move 4 US Troops to Available: Hue 2, Quang Tri 1, Da Nang 1.
**Why.** +4 US (49 → 53) with no withdrawal shift. These Troops guard nothing: Hue keeps 6 ARVN cubes; Quang Tri keeps its Irregular; Da Nang is already Active Support. The Bases (Training) and the Troops in An Loc, Can Tho and Qui Nhon (next-Coup pacify) stay.
**Execution.** Several stops: the event prompts space by space, then a count, then a piece-type count in mixed stacks; answered each in turn. No rejections.
**Result.** As planned: US 53; Da Nang lost COIN Control.

## Turn 9 — card #59 Plei Mei — before save-046
**Plan.** Event, unshaded: remove 3 NVA pieces from Southern Laos (next to the US Base in Pleiku): both NVA Bases + 1 Troop. Fallback if Bases are refused: 3 Troops from Pleiku.
**Why.** NVA sits at 17 of 18 with a Coup possible any card; −2 Bases puts it at 15 and NVA has no Bases in Available. Pleiku Troops instead would give only −1 (lost Control).
**Execution.** Stops at the space and per-type counts (answered Troops 1, Guerrillas 0; Bases took the remaining 2). No rejections. Mechanic: the event offers NVA Bases in a space adjacent to the COIN Base.
**Result.** As planned: NVA 17 → 15.

## Turn 10 — card #95 Westmoreland — before save-052
**Plan.** Op + SA: Train An Loc (no placement), Pacify An Loc Neutral→Active; Advise: ARVN Assault in Saigon (3 Active VC) and Irregular removal in Quang Tri (2 VC Guerrillas); +6 Aid.
**Why.** VC is at 34 (wins at 36) and US at 48 with a Coup possible any card. +2 US now; clearing Saigon denies VC the pop-6 Terror/Agitate target after the Reset; thinning Quang Tri (Passive Opp, pop 2) cuts a +2 VC Terror. Qui Nhon pacify rejected as more exposed (Phu Bon, Binh Dinh next door).
**Execution.** Deviation: second Advise went to Quang Nam (Ranger: 1 NVA Troop + its only Underground VC Guerrilla), not Quang Tri, because Quang Tri would keep 1 Underground VC and could still be Terrorized; Quang Nam removal kills a +1 VC Terror outright. No rejections.
**Result.** An Loc Active (US 50), 3 VC out of Saigon (4 hits), Quang Nam VC gone, Aid 38.

## Turn 11 — card #67 Amphib Landing — before save-060
**Plan.** Op + SA: Train Saigon (place 6 ARVN Troops) and Qui Nhon (none); Pacify Qui Nhon Neutral→Active; Air Lift 3 ARVN Troops each from Saigon to Tay Ninh, Binh Dinh and Kien Phong.
**Why.** NVA is at 20 (+2) and would win a Coup now. Breaking NVA Control in three pop-2 spaces is −6 NVA (to 14), and the Pacify puts US at 52. The Event (coastal relocation) is weak with 2 US Troops on the map.
**Execution.** Deviation: Air Lift caps ARVN at 4 Troops ("Move how many ARVN Troops (0 - 4)"), so Kien Phong got none: 2 to Tay Ninh, 2 to Binh Dinh. Mechanic: Air Lift moves at most 4 ARVN Troops in total. Other stops were menus skipped when there was one choice (Qui Nhon placement, Pacify space); no rejections.
**Result.** US 52, NVA 20 → 16 (Tay Ninh and Binh Dinh Control broken).

## Turn 12 — card #10 Rolling Thunder (Coup on deck) — before save-066
**Plan.** Op only, no SA: Train Pleiku-Darlac (6 ARVN cubes at the US Base), no Pacify (no target), decline the Special Activity.
**Why.** US is at 52 (+2) going into the Victory check. An Op without SA holds VC, the only other Eligible faction, to a one-space LimOp: at worst VC +2 (36, +1) or US −1 (51, +1), so US stays highest either way. Passing or taking the Event would give VC a full Op + SA with multi-space Terror.
**Execution.** No final-action menu (no Pacify target); SA declined with n. No rejections.
**Result.** Pleiku COIN Control; Op Only recorded, so VC gets a LimOp at most.

## Coup 2 — #128 Nguyen Van Thieu, Victory phase — before save-068
**Plan.** None needed; the program declared the result.
**Why.** —
**Execution.** none
**Result.** "US wins with a victory margin of 2!" (US 52 → +2; VC's LimOp Terror took VC to 36, +1). The program asks "Do you want to continue playing this game? (y/n)"; left unanswered for Kevin.

## Game end
Kevin instructed closing the game. Program was not running (container reclaimed); resumed from the latest save at the start of Coup 2, the Victory phase re-ran with the same result ("US wins with a victory margin of 2!"), answered n.
