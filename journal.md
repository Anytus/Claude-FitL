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
