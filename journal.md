# journal.md — full turn plans and rationales

This is the audit artifact. Every US action, Coup-round decision, and
pivotal-event decision gets an entry here **before** the first answer is
sent to the program, in the format given in `CLAUDE.md`. Rejections by the
program, aborts, and deviations from the plan are recorded verbatim in the
entry's Execution section.

## Turn 1 — card #112 Colonel Chau — before save-004
**Situation.** Card #43 ended before the US could act (NVA Op+SA, ARVN Event).
On #112 ARVN and NVA are Ineligible; VC took its Critical/Shaded side, stripping
Passive Support from Khanh Hoa, Phu Bon-Phu Yen and Kien Hoa-Vinh Binh and
placing a Guerrilla in each (US 38 -> 34). I am the only faction left, second
eligible after an Event, so my menu should be Op (may add a Special Activity)
or Pass. On deck is #48 Nam Dong: VC is Critical/Shaded there — "Remove a COIN
Base from a Province with 0-2 COIN cubes (US to Casualties)" — which points
straight at my Pleiku-Darlac Base (1 COIN cube). But VC has just acted, so it
is Ineligible on #48; the actors there will be NVA (Ignored -> Op) and ARVN
(Performed/Unshaded -> "Remove up to 3 Guerrillas from a Province with a COIN
Base, set it to Active Support", whose only legal target is Pleiku-Darlac).
That is a gift I should not disturb. Passing is worthless: US is last in order
on #48 and two bots will act there regardless.

**Options considered.**
- *Event.* Not available to the second eligible after an Event, and the unshaded
  side (1 Police into each of 6 Provinces) buys ARVN control, not US Support.
- *Train + Pacify Saigon.* Saigon is Passive Support, pop 6, COIN Control, with
  2 US Troops and 3 ARVN Police: one level of Pacify at 3 ARVN Resources turns 6
  points of Passive Support into 12 of Active Support. +6 US points for 3
  resources is the best rate on the board by a wide margin.
- *Assault / Sweep.* Every Guerrilla on the map is Underground; Assault can
  remove nothing and Sweep alone scores nothing.
- *Air Strike as the SA.* Only legal target would be the Trail (2 -> 1); NVA
  Resources are untracked for a bot, so the gain is thin.
- *Advise as the SA.* No Active enemies anywhere, so neither Advise sub-option
  has a target, but the +6 Aid at the end is free and converts to ARVN Resources
  in the Coup Resources phase, which is what funds pacification.

**Plan.** Op + Special Activity. Operation: **Train**, three spaces.
1. **Pleiku-Darlac** — place ARVN forces (a US Base is present, so cubes are
   legal): 2 ARVN Troops + 2 ARVN Police. Cost 3. Takes COIN pieces there to 7
   against 3 VC, giving COIN Control and putting Police in place for a later
   Pacify; also thickens the garrison around my only Province Base.
2. **Quang Tri-Thua Thien** — place 2 US Irregulars from Available. Cost 3.
   4 COIN against 3 VC gives COIN Control of a pop-2 Highland I want as the
   second engine later.
3. **Saigon** — do not place forces (free), then **Pacify Saigon one level,
   Passive Support -> Active Support**, cost 3.
Special Activity: **Advise**, taking the +6 Aid (and an ARVN Assault only if
the program offers a space with a removable enemy, which I do not expect).
Expected: Saigon Active Support, US Total Support 11 -> 17 and US points 34 ->
40; Aid 27 -> 33; ARVN Resources 30 -> 21; COIN Control added in Pleiku-Darlac
and Quang Tri-Thua Thien; US Available unchanged in Troops and Bases, Irregulars
3 -> 1.

**Rationale.** The post-mortem's verdict on the last game was that I banked
points in the force pool and never built anything on the map. Saigon is the one
place where Support and a garrison already coexist, and one Pacify there is
worth more than any three cards of piece-shuffling; I take it immediately rather
than saving it. The two placements are the cheap half of the same idea: ARVN
cubes can only go where a US Base or Saigon is, so Pleiku-Darlac is the only
Province where I can build a pacification engine before the first Coup puts a
second Base on the map, and Quang Tri-Thua Thien is the pop-2 space I intend to
work on next. Spending 9 of 30 ARVN Resources is nearly free: the Coup Resources
phase pays ARVN Econ + Aid before the Coup Support phase spends it, and whatever
I leave lying about the ARVN bot will spend on its own priorities anyway. Advise
is chosen over Air Strike because +6 Aid is +6 ARVN Resources at the Coup, which
is two more levels of pacification, while degrading a Trail that only feeds an
untracked bot resource track is close to worthless this early.

**Execution.** No rejections and no aborts. Three surprises, all in my favour:
(1) placing Irregulars costs no ARVN Resources — only the ARVN Troops/Police
placement in Pleiku-Darlac took the -3, so the operation cost 3 for placement
plus 3 for Pacify, not 9. (2) The Advise menu offered "Sweep a space with ARVN
forces" rather than the Assault I saw in TestGame1, and that Sweep only
Activated a Guerrilla in place — no cube movement was offered, so the Kien
Hoa-Vinh Binh Advise achieved almost nothing. (3) Contrary to my TestGame1 note,
"Use Irregular/Ranger to remove enemy pieces" **does** remove Underground
Guerrillas: it auto-selected Binh Dinh (the only legal space) and took 2 VC
Underground Guerrillas off, giving COIN Control of a pop-2 Highland and leaving
the VC Base there naked. I then tried to add Binh Dinh as a fourth Train space
to drop my last Irregular in; the program did not offer it, which confirms that
a space used for Advise cannot also be used for Train in the same action. I
declined Da Nang and Kontum rather than spend on placements I did not need.
Pacify offered Pleiku-Darlac and Quang Tri-Thua Thien as well as Saigon, so the
requirement is looser than "US Troops + ARVN Police + COIN Control" — Quang Tri
has no ARVN Police. I took Saigon as planned.

**Result.** As expected on the headline: Saigon is Active Support and US points
went 34 -> 40 (Total Support 11 -> 17). Aid 27 -> 33, ARVN Resources 30 -> 24
(I had budgeted 21). COIN Control gained in Pleiku-Darlac, Quang Tri-Thua Thien
and — unplanned — Binh Dinh, where the Advise removal is the real prize: 2 VC
Guerrillas to Available and a lone VC Base left with 2 COIN pieces on top of it.
VC 27, NVA 5, ARVN 36. US and VC are Ineligible on #48; ARVN and NVA act there.
