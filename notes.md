# notes.md — one line per US turn (cross-session memory)

Format: `card #<n> <title>: <action in a few words> — <why, ten words or fewer>`

Also log here: session resumes (with the save number resumed from), vetoes,
and anything Kevin asked administratively.

## TestGame2 (Full 1964-1972, US human, human win allowed in any Coup)
game start: new-game TestGame2 created — Agitate Total set to 3 by d3; awaiting first two card numbers.
card #43 Economic Aid: US did not act (3rd in order; NVA Op+SA, ARVN Event ended the card) — US+VC eligible on #112.
card #112 Colonel Chau: Train (Pleiku/Quang Tri/Saigon) + Advise; Pacified Saigon to Active Support — +6 US points for 3 resources.
  learned: Irregular placement in Train is free; Advise "use Irregular/Ranger" removes UNDERGROUND guerrillas (2 VC G off Binh Dinh); Advise and Train cannot share a space.
card #48 Nam Dong: US ineligible. ARVN played it unshaded on Pleiku-Darlac exactly as predicted (2 VC G removed, Active Support) — US 40 -> 42.
Coup 1 (#125 Nguyen Khanh): pacified Da Nang + Kontum to Active Support (12 res); Commitment moved 6 US Troops out of Available (QT+3, Binh Dinh+1, Hue+1, Quang Nam+1), no Bases — US 48 -> 42.
  ARVN Redeploy gifted 2 Police to Binh Dinh and 4 to Quang Tri: both pop-2 Highlands now pacifiable. Agitate Total reset to 1. Reset flips US Irregulars Underground too.
audit note (Kevin, after Coup 1): I abandoned the "second US Base on the map" plan at Commitment on a weak premise (borrowed ARVN Police). Not recoverable until Coup 2. Adopted: Train-Pacify Quang Tri + Binh Dinh early; Base first at Coup 2 Commitment.
resumed: container/program loss at the card prompt after Coup 1; `ctl.py resume TestGame2` reloaded save-010 and returned to the same prompt. Nothing replayed, no narration missed.
card #107 Burning Bonze: US ineligible (4th in order). VC shaded hit Saigon (Active->Passive Support) and Aid -12; NVA marched 20 Troops out of Laos into Quang Tin, Binh Dinh (NVA Control) and Quang Tri. US 42 -> 36, NVA 6 -> 10.
card #79 Henry Cabot Lodge: ARVN took shaded (3 own Troops off, +6 Patronage, ARVN ineligible next card). US Train+Advise: Pacified Saigon back to Active Support (+6), Advise took the VC Base off Pleiku-Darlac and 2 NVA Troops off Binh Dinh (NVA control broken), +6 Aid.
  learned: Advise removal CAN take an undefended Base; the Train space prompt sometimes has no list (type the name) and sometimes is numbered (typing is rejected) — print the screen every time; placement prompts allow more than Available by pulling pieces off the map.
card #101 Booby Traps: US ineligible. VC played shaded (capability: Sweep costs a US Troop on 1-3). NVA Attacked: 6 US Troops + 1 Irregular to Casualties from Quang Tri and Binh Dinh; NVA lost 6 to attrition. US now has no Troops in either Highland.
resumed: second container/program loss at the card prompt; ctl.py resume TestGame2 reloaded save-019 (post-NVA-attack state confirmed by render). Nothing replayed.
card #15 Medevac: US first eligible, took Op+SA. Train: 2 Rangers into Pleiku, Pacified Hue to Active Support (+2). Advise: chose 2 VC Guerrillas off Quang Tri -> COIN Control there (pop 2, Neutral, now a +4 pacify target); +6 Aid. ARVN then played Medevac unshaded, so all Troop Casualties reach Available at Coup 2 anyway.
  learned: Train space test is US pieces not Troops; Advise removal lets you pick the pieces; ARVN Police assault in Highland = 0 hits.
resumed: third program loss at the card prompt; resume reloaded save-022 (Medevac momentum intact).
card #118 Korean War Arms: US ineligible. VC shaded placed 3 VC Bases (Tay Ninh, Quang Tin, Quang Duc) -> VC 31 -> 34. NVA Rally/Infiltrate: swapped the VC Base in Binh Dinh for an NVA Base (NVA Control), built 10 Troops in the Parrot's Beak, Trail to 4. VC 33, US 44.
resumed: fourth program loss at the card prompt; reloaded save-025.
card #29 Tribesmen: US PASSED to deny ARVN eligibility on #63 and set up Fact Finding unshaded — ARVN passed too, so the card was a null and ARVN is still eligible to play the -4 shaded event. Prediction failed; Performed != certain.
card #63 Fact Finding: ARVN shaded took Support off Qui Nhon (-1, not the -4 I feared). US Op+SA: Train-Pacified Quang Tri to Active Support (+4, US 47); Air Lifted 1 US Troop each from Da Nang and Kontum into Kien Hoa-Vinh Binh to make it COIN-controlled for a -4 VC pacify next turn.
  learned: Train Pacify needs no US Troops (Irregulars suffice); Air Lift picks up to 4 spaces, moves both ways, no adjacency limit; Coup Victory phase precedes Support/Commitment, so casualties returning and Coup pacification count only for the NEXT Coup.
KEVIN NOTE (administrative, after card #63): "You can reduce patronage by training in Saigon." The Train final action "Transfer patronage to ARVN resources" lowers Patronage, which is 25 of ARVN's 46 points. I had seen the menu item every Train and never priced it, and had wrongly written that ARVN's Patronage was untouchable. It competes with Pacify for the one final Train action.
resumed: fifth program loss at the card prompt; reloaded save-027.
card #17 Claymores: US ineligible. VC Rally (4 G into Tay Ninh, 4 into Quang Tin, 1 into Kien Giang) + Subvert, which stripped the ARVN Police out of Kien Hoa-Vinh Binh and Phu Bon and dropped Patronage to 24 — my Kien Hoa COIN Control is gone (2 US Troops vs 2 VC Guerrillas). NVA marched into Kien Phong for NVA Control (NVA 11).
card #66 Ambassador Taylor: ARVN took Op Only (Train Saigon + Hue), which closed the Event to me — menu was Limited Op or Pass. PASSED: on #72 ARVN is out and the order is NVA, US, VC, so my action is guaranteed by turn order (not by a bot's choice, unlike card #29) and the VC gets no turn. Aim: Air Lift into Kien Hoa-Vinh Binh, then pacify it 2 levels for -4 VC.
card #72 Body Count: US PASSED again (the Limited Op on offer was Quang Nam +2, which the Coup Support phase will give me anyway). VC then acted (shaded event: 6 Guerrillas into Active Opposition spaces, 2 NVA Troops to Parrot's Beak) — which cost NVA two Control markers (13 -> 9) and secured my slot on #59. Kien Hoa now 3 VC Guerrillas vs 2 US Troops.
card #59 Plei Mei: ARVN Op+SA with GOVERN (Quang Tri and Pleiku Active->Passive Support; Aid 33->30, Patronage 27; US 47->44, ARVN 43->46 and now the closest to winning). US took Limited Op Train in Saigon intending the Patronage transfer and MISPLAYED IT: the final Train menu had only 2 entries (Pacify absent because Saigon is already Active Support), I sent 2 from the remembered 3-entry shape, and 2 was "Finished". Action wasted.
  RULE: one send per command, print the screen before every answer, never chain sends.
card #22 Da Nang: US ineligible. VC shaded removed Da Nang's Active Support (US 44->42) and banned Air Strike until the Coup; my adjacency read was right, Hue and Quang Tri were untouched. NVA Bombarded Hue and Pleiku (2 more US Troops to Casualties, now 8) and marched into Kien Phong and Kien Giang for NVA Control (NVA 13).
card #24 Operation Starlite: US Op+SA — Air Lifted 2 US Troops Saigon -> Kien Hoa-Vinh Binh for COIN Control, then Train-Pacified it 2 levels Active Opposition -> Neutral: VC 33 -> 29. ARVN then played Starlite unshaded, removing the VC Base in Quang Tri: VC 28. ROKs (+3 VC) on the next card now lands on 28, not 33 — no VC win at Coup 2.
  learned: Air Lift can carry ARVN Troops; the Patronage transfer needs Saigon as a selected Train space; COIN Control gains feed ARVN's score (46 -> 48 just from controlling Kien Hoa). ARVN is now the closest to victory at 48/50.
card #70 ROKs: US ineligible. VC shaded shifted Qui Nhon, Khanh Hoa and Phu Bon toward Opposition (VC 28 -> 31 — the +3 landed on 28, not 33, exactly as the Kien Hoa pacify intended). NVA Rallied 5 Guerrillas into Binh Dinh and Bombarded Saigon and Kien Hoa, taking a US Troop there to Casualties and knocking my new COIN Control off Kien Hoa (ARVN 48 -> 46).
