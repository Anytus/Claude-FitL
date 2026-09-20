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
