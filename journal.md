# journal.md — full turn plans and rationales (TestGame3)

This is the audit artifact. Every US action, Coup-round decision, and
pivotal-event decision gets an entry here **before** the first answer is
sent to the program, in the format given in `CLAUDE.md`. Rejections by the
program, aborts, and deviations from the plan are recorded verbatim in the
entry's Execution section. Previous games' journals are under `archive/`.


## Turn 1 — card #29 Tribesmen — before save-000
**Situation.** Opening position, nothing has happened. US is first eligible; order US, VC, ARVN, NVA. VC is marked Critical/Shaded: replace all four of my Irregulars (Quang Tri, Binh Dinh, Pleiku... actually three on map) with VC Guerrillas, a Neutral Highland to Active Opposition, Patronage -3. ARVN is Performed/Unshaded. On deck #93 Senator Fulbright (VC, US, NVA, ARVN): VC Ignored, so the VC takes an Op there; I am second whatever I do here, and Ineligible if I act.
**Options considered.**
- Event unshaded: "Remove any 4 Insurgent pieces total from spaces with Irregulars." Pieces include untunneled Bases. Spaces with Irregulars: Quang Tri-Thua Thien, Binh Dinh, Pleiku-Darlac, each holding 2 VC Guerrillas and 1 VC Base. Denies the VC its Critical shaded side, which would cost me all three map Irregulars (my Advise tools) and put a Highland at Active Opposition.
- Op + SA (Train Saigon to Active Support + Advise removals): +6 US now, but the VC then plays shaded Tribesmen: I lose the Irregulars, VC gains 3 Guerrillas and +4 Opposition.
- Op Only (Kevin's note): would leave the VC a LimOp and deny it the event. Worth remembering, but the unshaded event here removes three Bases, which an Op cannot.
**Plan.** Event, unshaded. Remove: the VC Base in Quang Tri-Thua Thien, the VC Base in Binh Dinh, the VC Base and 1 Guerrilla in Pleiku-Darlac. If the program removes Bases only after Guerrillas, fall back to clearing Quang Tri-Thua Thien entirely (2 Guerrillas + Base) plus 1 Guerrilla in Pleiku-Darlac.
**Expected effect.** VC 27 -> 24 (three Bases off the map). Pleiku-Darlac becomes COIN Control (3 US pieces v 1 Guerrilla): ARVN +1. Quang Tri and Binh Dinh keep 2 Guerrillas each against my Troop + Irregular, so still Uncontrolled, but each is one Advise removal from Control, and no Base means no Base-fed Rally there. Support unchanged. US 38 unchanged. US Ineligible on #93.
**Rationale.** Bases are the VC's score and its Rally engine; three of its seven are in the spaces where I have Irregulars and this event takes them for nothing while denying a Critical shaded event that would gut my Advise tool for the campaign. TestGame1 made this same play and it was among its good calls. The Pleiku choice over a full Quang Tri clear: Control in Pleiku comes with my Base already there, which is what makes Train place ARVN cubes outside Saigon; Quang Tri and Binh Dinh can be controlled next by Advise.
**Execution.** (below)
Sent: perform, 1 (Event), 1 (Unshaded), 2 (Pleiku-Darlac), 2 pieces, 1 Base (program filled 1 Guerrilla automatically), 1 (Binh Dinh), 1 piece, 1 Base, 3 (Quang Tri-Thua Thien), 1 piece, 1 Base. No rejections, no deviations. The program let me choose Bases directly; they are not removed last under this event.
**Result.** Exactly as planned: three VC Bases and one Guerrilla removed, COIN Control in Pleiku-Darlac, VC 27 -> 24, ARVN 35 -> 36. VC then passed; ARVN Trained Saigon/Hue, pacified Hue (+2 US) and Governed Kien Hoa and An Loc (-3 US, +3 Patronage). US Ineligible on #93 and squeezed out of #107 (fourth in order behind VC Event and ARVN Op). Burning Bonze shaded then hit Saigon (-6, Aid -12) and ARVN bought it back (+6). Net US 38 -> 37 after three cards.

## Turn 2 — card #97 Brinks Hotel — before save-010
**Situation.** US 37, VC 24, ARVN 39, NVA 8. VC and ARVN Ineligible; order VC, US, ARVN, NVA, so I act first and only the NVA (Performed/Unshaded) follows. ARVN Resources 12 < Econ 15: nobody can pacify. On deck #15 Medevac (US, ARVN, NVA, VC): ARVN Performed/Unshaded (all Troop casualties to Available at Commitment, which ARVN played for me in TestGame2); NVA and VC Performed/Shaded (no Air Lift until Coup, executing faction stays Eligible).
**Options considered.**
- Event unshaded: Aid +10 or 4 Patronage -> ARVN Resources, and flip Duong Van Minh. Pro-COIN either way, but the NVA is marked Performed/Unshaded for it, so if I take an Op + SA the NVA will most likely play it for me. Taking it myself wastes my action on something the bot gives me.
- Pass to be first on Medevac: I would then only take an Op there anyway, and it lets the NVA act here instead of after me. No.
- Op + SA: Advise removals in Quang Tri-Thua Thien and Binh Dinh (each 2 Underground VC Guerrillas vs my Troop + Irregular) give COIN Control in two pop-2 Highlands with no ARVN cubes (Govern-proof, Subvert-proof), removing 4 Guerrillas, and set up Train-Pacify and a Base at Commitment. Train places Irregulars for free elsewhere.
**Plan.** Op Train + Special Activity Advise. Advise (up to 2 spaces): "Use Irregular/Ranger to remove enemy pieces" in Quang Tri-Thua Thien (2 VC Underground Guerrillas) and Binh Dinh (2 VC Underground Guerrillas); accept +6 Aid. Train: Pleiku-Darlac, place Irregulars (2 if allowed, else 1) and a second Train space (Da Nang) for the third Irregular if Pleiku caps at 1; no Pacify (Resources below Econ), Finished.
**Expected effect.** COIN Control in Quang Tri and Binh Dinh: ARVN 39 -> 43 (+4 Control pop). VC unchanged at 24 (Guerrillas do not score). Aid 10 -> 16. US 37 unchanged; two Irregulars flipped Active. US Ineligible on Medevac; ARVN first there.
**Rationale.** Control in the two pop-2 Highlands is the position both post-mortems said the US never built: it is what makes Train pacify there and what Commitment can drop a Base into. It costs nothing but two Irregulars flipping Active. The ARVN +4 is the price; ARVN at 43 with Resources at 12 is not a Coup-1 threat. The Brinks event is left to the NVA, which is marked to play the side that helps me.
**Execution.** (below)
Sent: perform, 2 (Op), 1 (Train), 2 (Special Activity first), 1 (Advise), 2 (Irregular/Ranger removal), 3 (Quang Tri-Thua Thien), 2 (removal again), 1 (Binh Dinh), y (+6 Aid), 1, 4 (Pleiku-Darlac), 1 (Irregulars), 2, 1, 1 (Da Nang), 1 (Irregulars), 1, 2 (Finished selecting), 1 (Pacify, to test it), 1 (Da Nang) -> refused: "It is not possible to pacify in Da Nang / Only 12 ARVN resources available and Econ is 15", then 2 (Finished). Observations: Pleiku-Darlac with a US Base offered only "Place Irregulars / Do not place forces", presumably because ARVN Available was empty; the Irregular prompt allowed 0-2 in a space already holding 1, so the cap is on placement not on total. Pacify is listed in the final menu even when Resources are below Econ, and refused only after the space is chosen. Deviation: none.
**Result.** As planned: 4 VC Guerrillas removed, COIN Control in Quang Tri-Thua Thien and Binh Dinh (ARVN 39 -> 43), Aid 10 -> 16, 3 Irregulars placed (2 Pleiku, 1 Da Nang), 2 Irregulars Active. The NVA then played Brinks Hotel unshaded exactly as hoped, choosing 4 Patronage -> ARVN Resources (ARVN 43 -> 39, Resources 16) and did not flip the leader (Minh's text has no effect from it). On #15 ARVN did not play Medevac unshaded: it Swept four spaces (Resources 16 -> 4) and Raided; the VC took Medevac shaded (no Air Lift until the Coup, VC stays Eligible).
**Correction (Kevin, after card #97).** My inference that Pleiku-Darlac offered no ARVN cubes because ARVN Available was empty is wrong on both counts. Kevin: (1) the ARVN option was withheld because ARVN Resources did not exceed Econ (12 v 15), the same gate as Pacify; (2) US Train may place up to 6 ARVN cubes regardless of what is Available: cubes wanted beyond Available are removed from anywhere on the map to Available and then placed. Not yet observed at a prompt; to be confirmed the first time Resources exceed Econ.

## Turn 3 — card #66 Ambassador Taylor — before save-016
**Situation.** US 37, ARVN 43, VC 24, NVA 7. ARVN Ineligible; order ARVN, US, VC, NVA, so I act first. VC and NVA are both Performed/Shaded: remove Support from 3 spaces outside Saigon and Patronage -3, which would take Hue (2) and two pop-1 Cities off me (-4 US). ARVN Resources 4, Econ 15; Air Lift banned until the Coup. On deck #118 Korean War Arms (VC, ARVN, NVA, US): I am last in order and the VC is Critical/Shaded, so I will almost certainly not act on it whatever I do here.
**Options considered.**
- Event unshaded: Aid +9 (16 -> 25), ARVN Resources +9 (4 -> 13, still under Econ), and up to 2 US pieces from Out of Play into South Vietnam. Denies the shaded side (-4 US, -3 Patronage). Out-of-Play pieces cost no US points to place (they score nothing in the box).
- Op + SA (Sweep or Patrol to redistribute cubes): nothing it moves can pacify before the Coup, and the VC would then fire the shaded side.
- Pass: only worth it if eligibility next card mattered; it does not.
**Plan.** Event, unshaded. Take the pieces, not the Patronage: 1 US Base from Out of Play into Quang Tri-Thua Thien, 1 US Base from Out of Play into Binh Dinh. Both are COIN-controlled pop-2 Highlands held by US pieces only.
**Expected effect.** US 37 unchanged (map Bases do not score). Aid 25, ARVN Resources 13. Four US Bases on the map. Quang Tri and Binh Dinh each become spaces where Train can place ARVN cubes once Resources exceed Econ, and each Base is an extra piece for Control. US Ineligible on #118 (irrelevant). Risk: a Base in Quang Tri with one Troop beside it, next to North Vietnam and Central Laos; the NVA has 8 Troops out of the South and needs 6 in a space to Attack.
**Rationale.** This is the Base-on-the-map plan from the post-mortems, delivered by an event for free and denying a shaded side that would cost 4 points. The Aid raises the Coup payout to ARVN, which is the money my pacification spends. Placing Bases rather than Troops: Troops can come out of Available at Commitment; Bases from Out of Play come only this way, and a Base is what unlocks ARVN cube placement by US Train.
**Execution.** (below)
Sent: perform, 1 (Event), 1 (Unshaded), 1 (US pieces from Out of Play), 2 (count), "Quang Tri-Thua Thien" (bare prompt, typed name accepted), y (Base), "Binh Dinh", y (Base). No rejections, no deviations. The Out-of-Play prompt asks per space "Do you wish to place a base?" and a Troop would presumably follow on n.
**Result.** As planned: Aid 16 -> 25, ARVN Resources 4 -> 13, US Bases from Out of Play into Quang Tri-Thua Thien and Binh Dinh. VC passed; NVA Rallied Central Laos and Infiltrated (Trail 3). On #118 the VC's Critical shaded Korean War Arms placed three VC Bases (Quang Tin, Tay Ninh, Kien Giang: VC 24 -> 27); ARVN Swept III Corps (Resources 13 -> 1) and Raided a VC Base out of Quang Duc (VC 26). On #55 the NVA Rallied and Infiltrated again: Trail 4, 20 NVA Troops now in Laos (15 in Southern Laos, 5 in Central Laos... see render).

## Turn 4 — card #55 Trucks — before save-024
**Situation.** NVA has acted (Op + SA), VC and ARVN Ineligible; I am the only faction left on this card, so my menu is Event / Limited Op / Pass. 33 NVA Troops in Laos and Cambodia, 10 in Central Laos beside my new Quang Tri Base; the NVA's "20+ Troops on the map" check will be Yes from now on. ARVN Resources 1. On deck #17 Claymores (US, ARVN, VC, NVA): US first in order; ARVN Performed/Unshaded; VC and NVA Performed/Shaded. Shaded Claymores removes a COIN Base and an Underground Insurgent from a space with both: Pleiku-Darlac (my Base, 1 Underground VC Guerrilla) is the only such space, so it is aimed at me. Unshaded: executing faction stays Eligible, no Ambush until the Coup, each Marching group that Activates loses a Guerrilla.
**Options considered.**
- Event unshaded Trucks: Trail 4 -> 2 and the NVA removes 4 pieces each from Laos and Cambodia. Real but transient: the NVA re-Infiltrates about 10 Troops a card and re-improves the Trail each Rally. Costs my eligibility on Claymores, where ARVN's Performed marking is a coin flip (this game: NVA Performed took Brinks, ARVN Performed skipped Medevac, VC Performed passed on Taylor) and the VC behind it would take the shaded side and my Pleiku Base.
- Limited Op: nothing pacifiable; nothing worth one space.
- Pass: +3 ARVN Resources (1 -> 4), the card ends with nothing played (no shaded Trucks either, since the bots are marked Ignored and none is eligible), and turn order makes me first on Claymores with certainty, where unshaded keeps me Eligible for the card after as well.
**Plan.** Pass. Then on #17 Claymores: Event unshaded (stay Eligible, deny the shaded Base removal, tax NVA Marches).
**Expected effect.** No board change this card; ARVN Resources 4. Next card: my Pleiku Base safe, Momentum in my favour until the Coup, US still Eligible afterwards.
**Rationale.** This is the turn-order pass the post-mortems endorse: the action bought is guaranteed by the printed order, not by a bot's choice, and it protects a Base (permanent loss if it goes to Casualties) while giving back the eligibility it spends. Trucks is a good event but its effect decays within two NVA turns; Claymores' effect lasts to the Coup.
**Execution.** (below)
Sent: perform, 3 (Pass). No rejections.
**Result.** As planned: ARVN Resources 1 -> 4, card ended, #75 Sihanouk drawn; US first on #17 Claymores with ARVN and VC behind.

## Turn 5 — card #17 Claymores — before save-025
**Situation.** US first; ARVN (Performed/Unshaded) and VC (Performed/Shaded) behind; NVA Ineligible. ARVN Resources 4, so no pacification. On deck #75 Sihanouk (ARVN, NVA, US, VC): NVA and VC Performed/Shaded (free VC then NVA Rally in Cambodia and March out); I am third there, so I will likely be squeezed out whatever happens.
**Options considered.** Event unshaded (stay Eligible, no Ambush until Coup, each Marching group that Activates loses a Guerrilla; denies the shaded removal of my Pleiku Base). Op + SA: nothing to pacify, nothing to remove that Advise can reach except the single Underground Guerrilla in Pleiku (a Train + Advise there would clear it, but the Base stays exposed to shaded Claymores from the VC). Pass: pointless, I am already first.
**Plan.** Event, unshaded.
**Expected effect.** No score change. Momentum Claymores (unshaded) until the Coup. US remains Eligible for #75.
**Rationale.** As in the turn-4 entry: protects a Base from permanent loss, taxes the NVA/VC Marches that Sihanouk shaded will produce, and costs no eligibility.
**Execution.** (below)
Sent: perform, 1 (Event), 1 (Unshaded). No rejections.
**Result.** As planned: Momentum Claymores in play, US stays Eligible (shown as US(+)). ARVN then passed (Resources 7), VC Rallied 4 Guerrillas into Quang Tin and Taxed it (Agitate 4, Quang Tin to Passive Opposition). On #75 Sihanouk I was squeezed out as expected: ARVN Transport + Assault (Kien Giang Control, 4 Guerrillas killed, Resources 1), then NVA shaded Sihanouk: VC and NVA free Rally in Cambodia and March: NVA took Kien Phong (4 Troops) and Quang Tin-Quang Ngai (5 Troops + 4 Guerrillas) for NVA Control, NVA 7 -> 11; a VC Guerrilla marched into Pleiku, an NVA Guerrilla into Binh Dinh. Claymores' March penalty did not fire (no Marching group Activated). On #51 the VC Terrored and Taxed Quang Tin (Agitate 6).
**Note (Kevin, after #75).** At Trail 4 the NVA Marches for free outside South Vietnam; that is how the Parrot's Beak stack reached Quang Tin-Quang Ngai in one March. My turn-4 pricing of Trucks unshaded (Trail 4 -> 2) as "transient" undervalued it.

## Turn 6 — card #51 301st Supply Bn — before save-034
**Situation.** VC has acted (Op + SA); NVA and ARVN Ineligible; I am last on the card, menu Event / Limited Op / Pass. The Coup card is the one card left in pile 1 after #110, so the Coup follows #110. On #110 No Contact I am last in order behind VC, NVA (Performed/Shaded) and ARVN, so I will almost certainly not act on it whatever I do here. ARVN Resources 1; the Coup pays Econ 15 + Aid 25. 10 NVA Troops in Central Laos beside my Quang Tri Base (1 Troop, 1 Active Irregular); 14 in Southern Laos; Trail 4 so they move for free.
**Options considered.**
- Event unshaded: remove 6 non-Base Insurgent pieces from outside South Vietnam. Six NVA Troops out of Central Laos leaves 4 there, under the NVA's "8+ Troops outside the South" March trigger, and under the 6 it needs to Attack my Base if it does march.
- Limited Op: nothing pacifiable, no Assault target with Active enemies, one space only. Worthless.
- Pass: +3 ARVN Resources, eligibility on a card where I am last. Worth almost nothing.
**Plan.** Event, unshaded. Remove 6 NVA Troops from Central Laos. If the program restricts choice, prefer Troops over Guerrillas and Central Laos over Southern Laos.
**Expected effect.** No score change (NVA Control in Central Laos is pop 0 and survives anyway). Central Laos 10 -> 4 Troops. US Ineligible on #110.
**Rationale.** The NVA offensive is the threat to my Bases and Troops, and Aid falls 3 per Casualty at the Coup. This is the only action available that changes that, and it costs me nothing I could use.
**Execution.** (below)
Sent: perform, 1 (Event), 1 (Unshaded), 1 (Central Laos), 6, 6 (Troops; the prompt's minimum was 4 Troops since only 2 Guerrillas were there). No rejections.
**Result.** As planned: 6 NVA Troops from Central Laos to Available. On #110 (Monsoon) the NVA did not take the shaded event: Infiltrate replaced the VC Base in Quang Tin with an NVA Base and removed Passive Opposition there (NVA 12, VC 21), and put 6 Troops back into Southern Laos. ARVN found every operation ineffective and passed. Coup #126 Young Turks drawn; #73 on deck for after the Coup.

## Coup 1 (#126 Young Turks) — Support phase — before the Coup save
**Situation.** Victory phase: nobody above 0. Resources: Econ set to 13, ARVN +38 to 42, no Casualties. US Pacification offered in Da Nang (Neutral, pop 1), Kontum (Neutral, pop 1), Saigon (Passive Support, pop 6); 42 Resources, Econ 13, cost 3 per level.
**Plan.** Saigon 1 level (Passive -> Active Support, +6 for 3), Da Nang 2 levels (Neutral -> Active, +2 for 6), Kontum 2 levels (+2 for 6). Total 15 Resources, leaving 27, still above Econ for ARVN's own pacification.
**Expected effect.** US Support 14 -> 24, US 37 -> 47 before Commitment. The VC's Agitate Total of 6 will then spend against spaces with its Guerrillas.
**Rationale.** The cheapest points in the game, paid with a bot's money that it would otherwise spend on four-space Sweeps. Saigon Active Support is Govern-proof.
**Execution.** (below)
Sent: 3 (Saigon), 1 (1 level to Active), 1 (Da Nang), 1 (2 levels), 1 (Kontum), 1 (2 levels). No rejections. Result as planned: +12 Support, Resources 42 -> 27. ARVN pacified Kien Hoa to Passive; VC Agitated Quang Tin back to Active Opposition (Agitate 6 -> 3). US 37 -> 49, VC 25.

## Coup 1 — Commitment phase
**Situation.** US 49 (Support 26 + 23 in the box). ARVN Redeploy pulled 17 Troops into Saigon and dropped a Troop and a Police into each of Quang Tri-Thua Thien and Binh Dinh, which makes both pass the strict Coup pacification test next time. NVA Redeploy moved 8 Troops from Southern Laos into Quang Tin-Quang Ngai: 13 NVA Troops with an NVA Base, adjacent to Binh Dinh and Kontum. ARVN lost four Controls (44 -> 38). No Casualties.
**Options considered.**
- Deploy Troops to Quang Tri/Binh Dinh: each costs 1 point now, and 13 NVA Troops next door make a 2-3 Troop garrison casualties, not a defence. Air Lift is free again after the Reset and can move the 6 Troops already on the map if a space needs holding.
- Troop to Hue for a +2 Coup pacification: Hue is Govern-exposed (ARVN cubes exceed US cubes there); net +1 at best.
- Nothing: stay at 49.
- Saigon's Base to Available: +1 US (49 -> 50), no withdrawal shift (the penalty is 1 shift per 2 pieces), and Saigon can Train ARVN cubes with or without a US Base. Saigon Control is 26 ARVN cubes deep. The Base's only remaining job there was Assault doubling against enemies Saigon does not have.
**Plan.** Move the US Base from Saigon to Available. Move no Troops. Finished.
**Expected effect.** US 50 (score 0). Bases on the map 3 (Pleiku, Quang Tri, Binh Dinh), Available 3. Next Coup: Quang Tri and Binh Dinh pacifiable under the strict test (+4 each), which is the path above 50.
**Rationale.** A certain point now, at no cost to any plan; the deployment question is better answered with free Air Lifts during the campaign once the NVA stack shows where it is going.
**Execution.** (below)
Sent: 2 (Move a base), 2 (Saigon), 1 (Available box), 3 (Finished). No rejections. Withdrawal: "1 piece was removed to Available / No shifts in support possible". US 49 -> 50. Reset: Trail 4 -> 3, both Momentum removed, Irregulars flipped Underground, all Eligible.

## Card #73 Great Society — NVA shaded event, US choice — after the Coup
**Situation.** ARVN Swept Tay Ninh and Quang Tin and Raided (VC 24); the NVA played Great Society shaded: US moves 3 pieces from Available to Out of Play, my choice among 21 Troops and 3 Bases. Every piece is worth 1 point either way.
**Plan.** 3 Troops. Bases are the scarce piece (3 Available, none in Out of Play now), the only kind that unlocks ARVN cube placement in a Province, and the only kind an event can take from the box permanently. Troops in Out of Play can come back via events like Psychedelic Cookie unshaded, which is on deck.
**Expected effect.** US 50 -> 47. Out of Play 13 Troops.
**Result.** 3 Troops to Out of Play, US 47. Card ended (ARVN Op, NVA Event); I was squeezed out of #73.
