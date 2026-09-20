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

## Coup 1 (card #125 Nguyen Khanh) — Support phase, US Pacification — before save-008
**Situation.** Victory phase passed with nobody above threshold (VC -8, US -8,
NVA -12, ARVN -14). ARVN earned Econ 15 + Aid 33 = +48, so ARVN Resources are 72
against an Econ of 15 — pacification is effectively unlimited this phase. The
program offers 4 spaces but only two are legal: Da Nang and Kontum. Neither
Quang Tri-Thua Thien nor Binh Dinh is offered although both are COIN-controlled
with US Troops, and the difference is that neither has an ARVN Police: the Coup
Support phase enforces COIN Control + US Troops + ARVN Police, which is stricter
than the Train Pacify I did on card #112.
**Plan.** Pacify **Da Nang** two levels (Neutral -> Passive -> Active Support)
and **Kontum** two levels (Neutral -> Passive -> Active Support). 6 ARVN
Resources each, 12 of 72 spent, leaving 60 against Econ 15.
**Rationale.** Both are pop-1 Cities that already hold the full pacification
requirement, so each buys 2 US points for 6 Resources and there is nothing else
to spend on — the Resources are gone at the next Coup anyway and the ARVN bot
will burn whatever I leave. Expected US Total Support 19 -> 23 and US points
42 -> 46. The known cost is exposure: Active Support in a City with ARVN cubes
is what ARVN's Govern strips for Patronage, and #107 Burning Bonze is the next
card with VC marked Critical/Shaded, which will shift Saigon one level toward
Opposition (-6) and take 12 off Aid. I cannot stop either, and declining points
now to avoid points being taken later is how I lost the last game.
**Execution.** No rejections. The Pacify menu offers the whole shift at once
("Shift 2 levels to Active Support"), so each City took one answer. Only Da Nang
and Kontum were ever offered.
**Result.** Da Nang and Kontum both Active Support, -12 ARVN Resources. ARVN then
pacified Hue 1 level to Passive Support for 3 of its own. The VC spent its entire
Agitate Total straight afterwards: Kien Hoa-Vinh Binh to Active Opposition (2
levels) and Phu Bon-Phu Yen to Passive Opposition. Net on the markers: US 42 ->
48, VC 27 -> 32.

## Coup 1 (card #125 Nguyen Khanh) — Commitment phase — mid-Coup, no save yet
**Situation.** Pacification went as planned (Da Nang and Kontum to Active
Support, ARVN added Passive Support in Hue); the VC then spent its whole
Agitate Total, taking Kien Hoa-Vinh Binh to Active Opposition and Phu Bon-Phu
Yen to Passive Opposition. Markers: US 48, VC 32 — I am 2 under my threshold and
the VC is 3 under its, and ties go to the VC. The Redeploy phase was a gift:
ARVN moved 2 Police into Binh Dinh and 4 into Quang Tri-Thua Thien, so both
pop-2 Highlands now hold COIN Control + US Troops + ARVN Police and are
pacifiable without my spending a piece. Note for the record: `render.py` is
showing save-009, the pre-Coup state, because the Coup round writes one save at
its end; everything above is read from the program's narration.
**Options considered.** Withdrawal (map -> Available) is out: it pays 1 VC
population shift per 2 pieces and I need the board. Every piece I move the other
way costs exactly 1 US point now, so the test for each move is what it buys.
Hue (+1 US Troop -> pacify Passive -> Active Support, pop 2) and Quang Nam
(+1 Troop -> pacify Neutral -> Active Support, pop 1) each cost 1 point and
unlock 2, so they are net gains. Binh Dinh and Quang Tri-Thua Thien do not need
troops to be pacified — they need troops to kill the two VC Bases sitting in
them, and Highland Assault is 1 hit per 2 US Troops.
**Plan.** Move 6 US Troops from Available, no Bases:
- **Quang Tri-Thua Thien +3** (1 -> 4 US Troops): 2 Assault hits, enough to take
  the VC Base after an Advise strips the 2 Underground Guerrillas, with a spare
  hit if the VC re-garrisons.
- **Binh Dinh +1** (1 -> 2): exactly the 1 hit needed for the lone, naked VC Base.
- **Hue +1** and **Quang Nam +1**: pacification unlocks.
Keep both US Bases in Available: ARVN's redeploy already put Police where I
needed them, so a Base on the map would buy only Train placement I do not yet
need, at the cost of a point.
**Rationale.** This is my only chance to put pieces on the map for the whole of
campaign 2 — Available-to-map moves happen in Commitment and nowhere else — so
under-deploying now is a thirteen-card mistake, which is close to what I did
last game. The cost is real: US 48 -> 42. I accept it because the two pacifications
I already own (+8 from the Highlands) do not by themselves beat a VC that only
needs 3 points, and VC Bases are the one part of the VC total I can remove
outright. Expected by Coup 2: Support 25 -> 37 (Quang Tri +4, Binh Dinh +4, Hue
+2, Quang Nam +2), Available 17, two VC Bases gone (VC 32 -> 30 before its own
gains).
**Execution.** No rejections. The move prompt asks for the source space first
(only Available and spaces already holding US Troops are listed) and then the
destination, where every COIN-controlled space and every LoC is legal —
including Hue and Quang Nam, which hold no US Troops. I re-printed the
destination menu before each of the four answers rather than trusting it to be
stable. Withdrawal reported "0 pieces were removed to Available", so no
population shifted.
**Result.** 6 US Troops placed: Quang Tri-Thua Thien +3, Binh Dinh +1, Hue +1,
Quang Nam +1. US 48 -> 42 exactly as costed. Reset then flipped my Active
Irregular in Binh Dinh back to Underground (US Irregulars do flip in Reset, not
just enemy Guerrillas) and rolled the new Agitate Total at 1, the lowest
possible — the VC starts campaign 2 with almost nothing banked. Going into
card #107 the standings are US 42 (-8), VC 32 (-3), NVA 6, ARVN 36.
