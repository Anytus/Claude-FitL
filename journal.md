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

### Audit note (Kevin, after Coup 1): "wasn't your whole plan to place another base?"
Correct, and the Commitment entry above is where I went off it. My stated plan
at session start was a second US Base on the map early to unlock Train placement
of ARVN cubes in a pop-2 Province; at the prompt I dropped it because ARVN's
Redeploy had just put 4 Police in Quang Tri-Thua Thien and 2 in Binh Dinh, which
made both spaces pacifiable without a Base. That premise is not durable: those
are ARVN pieces, killable by the VC and movable by ARVN's own Redeploy at the
next Coup. The Base is what makes the engine mine — it is the only way I can
place ARVN cubes in a Province (Quang Tri offered "Place Irregulars" only;
Pleiku-Darlac, which has a Base, offered ARVN Troops/Police), and with 57 ARVN
Resources that is up to 6 cubes per Train for 3. I gave that up for 1 point on
the strength of a garrison I do not control, which is the pool-hoarding instinct
the post-mortem warned about wearing a local excuse.
Not recoverable: the Coup is saved, rollback is Kevin's tool, and US Bases reach
the map only via Commitment or an event, so the next chance is Coup 2.
Consequences I am adopting now: (1) bank Quang Tri-Thua Thien and Binh Dinh with
**Train Pacify on ordinary cards**, not at the Coup 2 Support phase — Train's
Pacify is the looser test (it offered Quang Tri with no ARVN Police on card
#112 where the Coup phase refused it), so the +8 can be taken before the Police
can be picked off; (2) a US Base into a pop-2 Highland is the first call on the
Coup 2 Commitment phase, not something to re-argue at the prompt.

## Turn 2 — card #79 Henry Cabot Lodge — before save-014
**Situation.** The NVA's 20-Troop March last card wrecked the plan I had for the
two pop-2 Highlands: Binh Dinh is NVA-controlled (7 NVA Troops against my 2
Troops, 1 Irregular and 2 ARVN Police, plus a VC Base) and Quang Tri-Thua Thien
is Uncontrolled (9 NVA Troops and a Guerrilla plus VC 2 Guerrillas and a Base
against 4 Troops, 3 Irregulars and 4 Police). Pacify needs COIN Control, so the
+8 I had banked on is out of reach this card. The VC also took Saigon back down
to Passive Support and 12 off Aid. ARVN has just played #79 shaded, removing 3
of its own Troops for +6 Patronage, and is Ineligible through the next card.
US 36, VC 32, NVA 10, ARVN 38.
**Options considered.**
- *Pass.* Worthless. On deck is #101 Booby Traps with VC and NVA both
  Critical/Shaded and both Eligible; they are 1st and 2nd in that card's order
  and I am 3rd, so staying Eligible buys me nothing at all.
- *Assault + Advise.* 4 US Troops in Quang Tri give 2 Highland hits and 2 in
  Binh Dinh give 1; with 4 more from Advise that is 7 NVA Troops. It still does
  not reach COIN Control in either space (Quang Tri needs 3 removals, Binh Dinh
  needs 4) and it gives up the biggest scoring move on the board.
- *Air Strike.* Rejected on the arithmetic: every populated space struck shifts
  1 level toward Active Opposition, and Quang Tri and Binh Dinh are both Neutral
  pop-2, so striking the two stacks that matter would hand the VC +4 and put it
  at 36 — over its threshold — to kill maybe 4 NVA Troops. The one stack I would
  happily strike, Quang Tin-Quang Ngai, holds no COIN pieces and is unreachable
  without Arc Light.
- *Train + Pacify Saigon.* Saigon is Passive Support at pop 6 with COIN Control,
  US Troops and an ARVN Police: one level for 3 Resources is +6 US points.
**Plan.** Op + Special Activity.
Operation **Train**, two spaces: **Quang Tri-Thua Thien** (place my last
Irregular from Available — free, and it keeps Advise fodder in the space the
NVA is sitting in) and **Saigon** (do not place forces). Final Train action:
**Pacify Saigon 1 level, Passive -> Active Support**, 3 Resources.
Special Activity **Advise**, two spaces, both "use Irregular/Ranger to remove
enemy pieces": **Pleiku-Darlac**, where an Underground Irregular sits with a
lone VC Base, and **Binh Dinh**, where the removal should take 2 NVA Troops.
Then take the +6 Aid. Neither Advise space is a Train space, so there is no
conflict with the rule I hit last turn.
**Rationale.** +6 US points for 3 Resources is the best rate available and I
take it before anything else knocks Saigon down again. For the Special Activity
the question is whose points to attack, and the answer is the VC's: it sits at
32 against a threshold of 35 with ties going its way, while the NVA at 10
against 18 cannot win at the next Coup whatever it does. So the first Advise
goes at the VC Base in Pleiku-Darlac (-1 VC, and it denies the VC a rally point
inside an Active Support space); I am not certain the program will let a
removal take a Base with no Guerrillas guarding it, and if it refuses I will
fall back to Quang Tri-Thua Thien. The second goes into Binh Dinh, where 2 NVA
Troops leave the NVA at 5 against 6 other pieces and break its Control, which is
worth 2 NVA points and is the first step back toward pacifying the space.
Expected: US 36 -> 42, Aid 21 -> 27, ARVN Resources 57 -> 54, VC 32 -> 31,
NVA 10 -> 8.
**Execution.** Two things to record.
(1) The first "Train in which space:" prompt arrived with **no list** — the
program printed the bare prompt, and `screen`, `read` and `transcript.log` all
showed the same thing — so I typed the space name, "Quang Tri-Thua Thien", and
it was accepted. On the very next selection the same prompt came back with a
numbered menu, and my typed answer was rejected verbatim:
    'Saigon' is not valid. Must be one of:
    1, 2, 3, 4, 5, 6, 7, 8, or abort
I printed the menu and answered 4. So this prompt takes either form and the
only safe procedure is to print the screen before every answer, which is what
caught it.
(2) Placing Irregulars in Quang Tri-Thua Thien offered "(0 - 2)" although
Available held 1. I answered 2 on the guess that Available was really 2, and the
program instead said "There are not enough US Irregulars in the available box /
You must remove 1 US Irregular from the map" and listed Binh Dinh, Pleiku-Darlac
and Quang Tri-Thua Thien. Taking the piece from Binh Dinh or Pleiku-Darlac would
have destroyed the Advise plan for this very turn, so I took it from Quang Tri
itself: remove 1 there, place 2 there, net +1, identical to the placement I
had planned. Deviation with no cost, but the lesson is that the upper bound on
a placement prompt is not the Available count — it is Available plus voluntary
removals from the map.
No aborts. Advise offered Binh Dinh and Pleiku-Darlac but not Quang Tri-Thua
Thien, confirming again that a Train space cannot be an Advise space.
**Result.** As planned on every count, and the uncertain part worked: Advise
**does** remove a Base with no Guerrillas guarding it — the lone VC Base came
off Pleiku-Darlac (VC 32 -> 31) — and 2 NVA Troops off Binh Dinh broke NVA
Control there (NVA 10 -> 8). Saigon is Active Support again, US 36 -> 42, Aid
21 -> 27, ARVN Resources 57 -> 54. Standing: US 42 (-8), ARVN 38 (-12), VC 31
(-4), NVA 8 (-10). Note for the next turns: the Advise Irregular/Ranger removal
is the most efficient tool I have — 2 enemy pieces per space, up to 2 spaces,
free, no Support shift, and it reaches Underground Guerrillas and undefended
Bases that Assault and Air Strike cannot touch.

## Turn 3 — card #15 Medevac — before save-020
**Situation.** The NVA's Attack took all 6 US Troops I committed at Coup 1 plus
an Irregular into Casualties; Binh Dinh has no US pieces at all and Quang
Tri-Thua Thien is down to 4 Irregulars and 4 ARVN Police. The VC's Booby Traps
shaded capability is permanent, so Sweep now costs a US Troop per space on a 1-3
and is effectively off the table. US 42, ARVN 38, VC 31, NVA 8. I am first
eligible for the first time this game. On deck is #118 Korean War Arms with VC
Critical/Shaded — "place any 1 VC piece in each of 3 spaces", and a piece may be
a Base — so I should expect the VC to be at 33-34 within two cards.
**Options considered.**
- *Medevac shaded* ("executing faction remains Eligible; no Air Lift until
  Coup"). The eligibility is worthless here: on #118 the order is VC, ARVN, NVA,
  US and the VC and NVA are both Eligible, so two bots act before me whatever I
  do. It would also ban the one tool that can redistribute my Irregulars.
- *Medevac unshaded* ("this Commitment, all Troop Casualties to Available").
  Real but small: it saves the 2 of 6 Troop Casualties that would otherwise go
  Out of Play at the Coup 2 Commitment, so +2 US points.
- *Assault.* No legal space — every space holding US Troops (Hue, Da Nang,
  Quang Nam, Kontum, Pleiku-Darlac) is free of enemies, and the two spaces with
  enemies no longer hold US Troops.
- *Air Strike.* Both reachable stacks sit in Neutral pop-2 Highlands, so each
  space struck would shift a level toward Active Opposition and pay the VC 2
  points per space. Still refused.
- *Train + Advise.* The only Op with anything in it.
**Plan.** Op + Special Activity.
Operation **Train**, two spaces: **Pleiku-Darlac** — place 2 ARVN Rangers (it
has the US Base, so Rangers are legal there; 3 Resources) — and **Hue**, no
placement. Final Train action: **Pacify Hue 1 level, Passive -> Active
Support**, 3 Resources, +2 US.
Special Activity **Advise**: **Quang Tri-Thua Thien**, "use Irregular/Ranger to
remove enemy pieces" (4 Underground Irregulars are there), then a second space
only if the program offers an ARVN Assault that would actually remove something;
then take the +6 Aid.
**Rationale.** Two honest caveats about this turn. First, the Hue pacification
is nearly free but nearly redundant: Hue and Quang Nam both qualify for the Coup
2 Support phase anyway and I have only those two candidates against four slots,
so banking it now only buys insurance against the VC marching a Guerrilla into
Hue and terrorising it. Second, and more important, the reason I am not taking
Medevac unshaded for its +2 is that this action's real value is the Advise
removal and the Rangers. The Advise Irregular/Ranger removal is the only tool I
have that reaches Underground Guerrillas and undefended Bases, and its
limitation is reach, not rate: it needs an Underground Irregular or Ranger in
the target space, and after the Attack I have them in exactly one contested
space. Two Rangers in Pleiku-Darlac are Air Lift cargo for later — the way to
get a removal engine pointed at the VC's six Bases, which is the part of the VC
total I can actually take off the board. Expected: US 42 -> 44, Aid 27 -> 33,
ARVN Resources 54 -> 48, 2 enemy pieces off Quang Tri-Thua Thien.
**Execution.** No rejections, no aborts. Three things learned.
(1) Train offered **Quang Tri-Thua Thien** as a space although it holds no US
Troops, only Irregulars — so the Train space test is US *pieces*, not Troops.
(2) The Advise removal let me **choose** the pieces this time, printing
"Select 2 pieces among the following: 5 NVA Troops, 1 NVA Underground Guerrilla,
2 VC Underground Guerrillas" and prompting for a count of each in turn; after I
answered 0 and 0 it assigned the remaining 2 to the VC Guerrillas automatically.
I chose the VC Guerrillas over the NVA Troops deliberately: either pair flips
Quang Tri to COIN Control (COIN 8 against 9 enemy pieces, so removing any 2
does it), but taking the Guerrillas also leaves the VC Base there unguarded for
a later removal, and the VC is the faction that can actually win at the next
Coup.
(3) I spent the spare second Advise slot on the ARVN Assault it offered in Binh
Dinh, expecting nothing; it "inflicts 0 hits", as 2 Police in Highland should.
Harmless, and it confirms the Police-in-Highland rate.
**Result.** Hue is Active Support and Quang Tri-Thua Thien is **COIN-controlled**
— better than planned, since I had written that space off for this card. US
42 -> 44, Aid 27 -> 33, ARVN Resources 54 -> 48, 2 VC Guerrillas to Available,
2 Rangers into Pleiku-Darlac. The Medevac question answered itself: ARVN played
the unshaded side after me, so the momentum is in play and all 6 Troop
Casualties will reach Available at the Coup 2 Commitment regardless — the +2 I
declined to spend my action on arrived for free, which vindicates taking the Op.
Standing: US 44 (-6), ARVN 40 (-10), VC 31 (-4), NVA 8 (-10).
**Next card's aim:** Quang Tri-Thua Thien is pop-2, Neutral and COIN-controlled.
Train-Pacify there is +4 if the program will pacify a space whose only US pieces
are Irregulars; if it refuses, that tells me US Troops are required and the
Coup 2 Support phase will refuse it too.

## Turn 4 — card #29 Tribesmen — before save-026
**Situation.** VC 33 against a threshold of 35, and 8 of those 33 are Bases it
placed for free last card. US 44, NVA 9, ARVN 40. I am first eligible on #29
(US, VC, ARVN, NVA); VC and NVA are Ineligible, so the shaded side that would
replace all my Irregulars with VC Guerrillas cannot be played by anyone this
card. Unshaded removes any 4 Insurgent pieces from spaces with Irregulars — and
my only Irregulars are the 4 in Quang Tri-Thua Thien (the Pleiku-Darlac one has
no insurgents beside it), so all 4 removals would come out of that one stack of
5 NVA Troops, 1 NVA Guerrilla and the VC Base.
On deck is **#63 Fact Finding** (ARVN, US, NVA, VC). Its shaded side — ARVN
Critical, NVA and VC both Performed — is "Remove Support from a COIN-Controlled
City outside Saigon, Patronage +4", which against Hue is -4 US. Its unshaded
side is "2 US pieces from out-of-play to South Vietnam, or transfer a die roll
from Patronage to ARVN Resources. Aid +6."
**Options considered.**
- *Take Tribesmen unshaded now (Line A).* I pick the 4 removals myself — the VC
  Base (-1 VC) and 3 NVA Troops. But it makes me Ineligible on #63, where the
  shaded side then lands from ARVN, NVA or VC whichever is eligible: -4 US.
  Net roughly VC -1, US -4.
- *Train + Pacify Quang Tri-Thua Thien (Line C).* It is pop-2, Neutral and
  COIN-controlled, so 2 levels is +4 US — if the program will pacify a space
  whose only US pieces are Irregulars. Same flaw: Ineligible on #63, -4 back.
- *Pass (Line B).* Passing keeps me Eligible and makes ARVN first eligible on
  this card. ARVN is marked Performed/Unshaded here, and it has taken the Event
  on all four cards where it was marked Performed or Critical this game, so it
  should play Tribesmen unshaded itself — the 4 removals still come off my Quang
  Tri stack, just with the bot choosing which. More importantly, **any** ARVN
  action on #29, Event or Op, makes ARVN Ineligible on #63, which leaves me
  first among the eligible there.
**Plan.** **Pass.** Then on #63 take the unshaded Event: 2 US pieces from Out of
Play into South Vietnam, plus Aid +6.
**Rationale.** The Out-of-Play box holds 10 US Troops and 2 US Bases that no
Commitment phase can ever reach — they are worth 0 points where they sit, so
moving them onto the map is the one deployment in this game that costs nothing.
Fact Finding unshaded is therefore the free version of the thing I talked myself
out of at Coup 1: a US Base and a Troop into Quang Tri-Thua Thien, which is
already COIN-controlled with 4 ARVN Police, would make it pacifiable for +4 in
the Coup 2 Support phase (that phase demands US Troops, which Quang Tri no
longer has) and give me the durable Province Base Kevin was right to ask about.
Taking the unshaded side also denies the shaded -4 to all three bots at once,
which an Op on #63 would not: if I took an Op there, NVA is second in line and
is marked Performed/Shaded.
The risk is precise and bounded: if ARVN *also* passes, #29 is wasted and ARVN
plays the shaded side on #63 for -4 anyway. I am pricing that at low
probability on four-for-four evidence, against a swing of about 4 US points plus
two free pieces.
**Execution.** Passed at the first menu (3). No rejections.
**Result.** **The branch I priced as unlikely is the one that happened: ARVN
passed as well.** Nobody acted on #29, so the 4 insurgent removals were never
made, all four factions are Eligible again, and ARVN — still Eligible — will
take its Critical/Shaded side of #63 first in that card's order and strip
Support from a City outside Saigon for -4 US. The pass earned +3 ARVN Resources
each for me and ARVN and nothing else; VC and NVA were Ineligible so the card
was a null for everyone.
My prediction was based on ARVN having taken the Event on all four cards where
it was marked Performed or Critical. That is now four-for-five, and the
counter-example came with a "Performed" marking rather than "Critical" — worth
remembering: **Performed is a preference, not a commitment, and a bot that is
sole eligible may simply bank the +3.** The deeper error is that I let a
one-sided read of the bot carry a plan whose downside was the same -4 I was
trying to dodge plus a dead card; the sequencing play only pays if the denial is
certain, and denial by proxy — relying on a bot to spend its own eligibility —
never is. Where I can deny a card by acting on it myself, that is the version
worth taking.
Position unchanged: US 44, VC 33, NVA 9, ARVN 40 (Resources 54).

## Turn 5 — card #63 Fact Finding — before save-027
**Situation.** ARVN played the shaded side but chose **Qui Nhon** (Passive
Support, pop 1) rather than Hue, so the damage was -1, not the -4 I had priced;
Patronage to 25, ARVN 44. US 43, VC 33, NVA 9. I am second eligible after an
Event, so the menu is Op (may add a Special Activity) or Pass; the Event is
gone, and with it the worry about who else could use it.
**The clock, recalculated.** The Coup round resolves Victory *first*, before
Resources, Support, Redeploy and Commitment. So the 6 Troop Casualties that
Medevac will send to Available, and everything the Coup Support phase pacifies,
count for Coup **3**, not Coup 2. To win at Coup 2 I need US above 50 on
ordinary card play alone, from 43 — and the VC, on 33, needs only 36 to take it
first on a tie. That reframes what my remaining two or three actions are for.
**Options considered.**
- *Pass again.* No. On deck #17 Claymores has no legal target for its shaded
  side (it needs a space holding both a COIN Base and an Underground Insurgent;
  Saigon and Pleiku-Darlac, my only COIN Bases, have no insurgents at all), so
  there is nothing to deny and nothing to gain by staying Eligible.
- *Advise as the Special Activity.* Quang Tri-Thua Thien is the only space with
  Underground Irregulars beside enemies, and it is the space I want to Train in
  — the two cannot share. That leaves Advise worth a 0-hit ARVN Assault and
  +6 Aid, and Aid is nearly worthless with ARVN already holding 54 Resources.
- *Air Strike.* Still refused: every reachable stack sits in a populated space
  that would shift a level toward Active Opposition, paying the VC 2 a space.
**Plan.** Op + Special Activity.
Operation **Train** in **Quang Tri-Thua Thien** (no placement — 0 Irregulars in
Available), then **Pacify it 2 levels, Neutral -> Passive -> Active Support**,
6 Resources, **+4 US**. If the program refuses the space because its only US
pieces are Irregulars rather than Troops, I fall back to Quang Nam for +2 and
record the refusal.
Special Activity **Air Lift**: move 2 US Troops, one from Da Nang and one from
Kontum, into **Kien Hoa-Vinh Binh**.
**Rationale.** Quang Tri first because the +4 is already set up and its COIN
Control is the fragile part — 5 NVA Troops and a Guerrilla are still standing in
it — and because Support persists through a change of Control, so once the
marker is on Active Support only Terror can take it back, and the VC has nothing
but a Base left in the space to do that with.
The Air Lift is the more important half. Kien Hoa-Vinh Binh is Active Opposition
at pop 2 — 4 of the VC's 33 points — held by one Underground VC Guerrilla
against a lone ARVN Police, which is why it is Uncontrolled. Two US Troops make
it COIN-controlled 3 pieces to 1 and supply the US Troops that pacification
demands; a Train next card then shifts it 2 levels to Neutral and takes **4
points straight off the VC**, with a further 2 available later if I push it to
Passive Support. That is the same size of swing as a pacification of my own
spaces but aimed at the faction that is 3 points from winning, and there is no
other VC-held space I can reach this cheaply — every VC Base on the map is
buried behind Guerrillas or NVA Troops, and Underground Guerrillas are immune to
both Assault and Air Strike. The cost is that Da Nang and Kontum fall to one US
Troop plus one ARVN Police each; both are pop-1 Cities at Active Support, so the
exposure is 2 points apiece and only to Terror.
**Execution.** No rejections, no aborts. Two notes.
(1) **Train Pacify does not require US Troops.** Quang Tri-Thua Thien was
offered and pacified with nothing but 4 Irregulars and 4 ARVN Police in it, so
the fallback to Quang Nam was never needed. The Coup Support phase is the strict
one (COIN Control + US Troops + ARVN Police); Train's is looser.
(2) The "Air Lift in which space:" prompt arrived in the **bare, listless form**
again, so I typed the space names. Air Lift selects up to 4 spaces first and
then moves pieces among them in any direction, and it is not
adjacency-limited — Da Nang and Kontum in I and II Corps lifted straight into
Kien Hoa-Vinh Binh in IV Corps.
**Result.** Everything as planned. Quang Tri-Thua Thien is **Active Support**
(US 43 -> 47, Total Support 30) for 6 Resources; Kien Hoa-Vinh Binh is
**COIN-controlled** with 2 US Troops beside the ARVN Police against 1 VC
Guerrilla, and ARVN's marker moved 44 -> 46 on the control gain. Da Nang and
Kontum are each down to 1 US Troop and 1 ARVN Police.
Standing: US 47 (-3), ARVN 46 (-4), VC 33 (-2), NVA 9 (-9). Three factions are
now within 4 points of their thresholds, and ARVN's climb is entirely Patronage
— 25 of its 46 — which is the part of its score I cannot touch.
**Next card's aim:** Train-Pacify **Kien Hoa-Vinh Binh** 2 levels, Active
Opposition -> Neutral, for **-4 VC**. That is the single largest swing available
to me and it is aimed at the only faction that can win at the Coup 2 Victory
check.

### Kevin note (administrative, after card #63)
"You can reduce patronage by training in Saigon." Correct and I had missed it:
the Train final-action menu offers "Transfer patronage to ARVN resources"
alongside Pacify, and I have skipped past it every single Train. ARVN is at 46
of 50 with **25 of those points in Patronage**, so that transfer is a direct
reduction of the second-closest faction to victory — and I wrote in the last
report that Patronage was the part of ARVN's score I could not touch, which was
simply wrong. It costs the one final Train action, so it competes head-on with
Pacify; from here I price both every turn instead of assuming Pacify.

## Turn 6 — card #66 Ambassador Taylor — before save-037
**Situation.** ARVN took **Op Only** (Train, stacking 3 Troops + 3 Police into
each of Saigon and Hue), which confirms the TestGame1 note: as second eligible
after an Op Only my menu is "1) Limited Op  2) Pass" and the Event is closed to
me. So Ambassador Taylor's unshaded side — 2 US pieces out of the Out-of-Play
box, or Patronage -3 — is not available. US 47, VC 33, ARVN 43, NVA 11.
Last card's Subvert stripped the ARVN Police out of Kien Hoa-Vinh Binh and put a
Guerrilla in, so my 2 US Troops there face 2 VC Guerrillas and nobody controls
it; the -4 pacification needs one more COIN piece in the space first, which
means an Air Lift, which a Limited Op cannot carry.
**What actually decides this.** The VC is 3 points from winning outright at the
Coup 2 Victory check, and that check happens before anything else in the Coup.
Denying the VC points is existential in a way that adding 2 to my own total is
not.
**Options considered.**
- *Limited Op now.* The only real content is Train in Quang Nam and pacify it 2
  levels, Neutral -> Active Support, +2 US for 6 Resources. Kien Hoa-Vinh Binh
  is not pacifiable (Uncontrolled), Qui Nhon, Cam Ranh, An Loc, Can Tho and Ba
  Xuyen hold no US pieces so they cannot even be Train spaces, and the transfer
  of Patronage to ARVN Resources that Kevin pointed out costs the same single
  action while ARVN, at 43 with 8 to go, is not the faction about to win.
- *Pass.* On deck is #72 Body Count (ARVN, NVA, US, VC). ARVN is Ineligible
  there, having just acted. If I stay Eligible the order is NVA, then me, then
  VC — and a card ends after two factions act.
**Plan.** **Pass.**
**Rationale.** Two things follow from that turn order, and the first is the one
I got wrong on card #29. **My action on #72 is guaranteed by the order itself,
not by a bot's choice**: only NVA stands ahead of me among the eligible, so the
only way I could be squeezed out is if NVA and VC both acted first, and VC is
behind me. On #29 I passed and left the denial resting on ARVN choosing to
spend its eligibility; here nothing rests on anyone.
Second, passing takes the VC's turn away from it. If I act now, #72 is NVA and
VC; if I pass, it is NVA and me, and the VC — 3 points from victory, with Terror
available in Khanh Hoa and Phu Bon-Phu Yen and one Base still in Available —
gets nothing.
And the action I am buying is bigger. As second eligible after an NVA Event I
get a full Op + Special Activity: Air Lift 2 US Troops out of Saigon (which ARVN
has just garrisoned with 5 Troops and 4 Police, so it can spare them) into Kien
Hoa-Vinh Binh for COIN Control, then Train-Pacify it 2 levels from Active
Opposition to Neutral — **-4 VC**, taking them to 29 and out of reach of the
Coup 2 check. Even the worst case is not a loss: if NVA takes an Op with a
Special Activity I fall back to a Limited Op and pacify Quang Nam for the same
+2 I would have had here, one card later.
The real cost is tempo — acting on #66 would leave me eligible again two cards
out, and passing spends that. I am paying it because a VC at 29 cannot win at
Coup 2 and a US at 49 cannot either.
**Execution.** Passed (2). No rejections. The program confirmed eligibility:
US, VC and NVA to the Eligible box, ARVN to Ineligible — exactly the
configuration the plan depends on.
**Result.** +3 ARVN Resources (45). No board change. #72 Body Count is current
with US, VC and NVA eligible and ARVN out; NVA acts first, I act second, and the
card ends before the VC.

## Turn 7 — card #72 Body Count — before save-039
**Situation.** NVA took Op + Special Activity (Infiltrate 6 Troops into North
Vietnam; March a Guerrilla out of Quang Tri onto the Saigon-An Loc LoC and 3
Troops from the Parrot's Beak into Kien Giang-An Xuyen for NVA Control, NVA 11
-> 13). As second eligible after an Op + SA my menu is Event, Limited Op or
Pass — no Special Activity, so the Air Lift that the Kien Hoa-Vinh Binh plan
needs is not available this card. US 47, VC 33, ARVN 43, NVA 13.
**The redundancy that decides this.** A Limited Op's only scoring content is
Train in Quang Nam, pacifying it 2 levels from Neutral to Active Support for
+2. But Quang Nam holds COIN Control, a US Troop and an ARVN Police, which is
exactly the Coup Support phase's test — **the Coup will pacify it for me
anyway**, and it is my only candidate against four slots there. The +2 would
only be worth something if it carried me over 50 at the Coup 2 Victory check,
and 47 + 2 = 49. So the Limited Op is worth close to nothing.
**Options considered.**
- *Event.* Body Count unshaded is a momentum making Assault and Patrol cost 0
  with +3 Aid per Guerrilla removed. I have almost no Assault targets that are
  not Underground. Worthless. The shaded side is obviously not mine to play, and
  the VC cannot reach it either: NVA has acted, so my acting ends the card.
- *Limited Op -> Quang Nam.* +2, redundant as above.
- *Limited Op -> Train Saigon, transfer Patronage to ARVN Resources.* Not
  redundant — the Coup cannot do it — but it is aimed at ARVN on 43 needing 51,
  not at the VC on 33 needing 36.
- *Pass.*
**Plan.** **Pass.**
**Rationale.** The VC is the only faction that can end the game at the Coup 2
Victory check, and it needs 3 points it can plausibly find: Terror in Khanh Hoa
(Neutral, pop 1, VC Guerrilla present) is +1, Terror in Phu Bon-Phu Yen
(Passive -> Active Opposition) is +1, and it still holds a Base in Available
worth +1 if it Rallies one out. Taking 4 points off it at Kien Hoa-Vinh Binh —
Air Lift 2 US Troops from Saigon, which ARVN has just garrisoned with 5 Troops
and 4 Police, then Train-Pacify 2 levels from Active Opposition to Neutral —
puts the VC on 29 and out of reach. That needs a full Op + Special Activity,
which #59 can give me: NVA has acted and so is Ineligible there, ARVN acts
first, I act second, and ARVN is marked Performed/Unshaded, so the likeliest
branch hands me the Op + SA.
**The dependency, stated plainly.** This is *not* the guaranteed-by-turn-order
case I had on #66. It needs **the VC to act on #72**, so that it is Ineligible
on #59 and does not take the slot ahead of me. If the VC passes, #59 is VC then
ARVN and I am shut out — the #29 failure exactly. The VC has acted on all four
cards it was eligible for this game, but ARVN was four-for-four before it passed
on me. What makes the bet defensible this time is not a better read of the bot,
it is that the thing I am risking is worth almost nothing: the Limited Op I am
declining duplicates a Coup pacification I will get for free. I am wagering ~0
for a ~4-point cut in the only score that can beat me.
**Execution.** Passed (3). No rejections.
**Result.** The dependency held: **the VC acted**, taking Body Count shaded, so
it is Ineligible on #59 and my slot there is now secured by turn order — #59 is
ARVN then US, and nobody else is eligible. The event itself placed 6 Guerrillas
into Active Opposition spaces and 2 NVA Troops into the Parrot's Beak, which
cost the **NVA** two Control markers (Kien Giang-An Xuyen and Kien Phong, NVA
13 -> 9) and left the VC score untouched at 33, since Guerrillas do not score.
The one thing that matters for my plan: Kien Hoa-Vinh Binh now holds 3 VC
Guerrillas against my 2 US Troops, so COIN Control there needs 4 US pieces, not
3 — the Air Lift has to bring 2 Troops, not 1.

## Turn 8 — card #59 Plei Mei — before save-041
**Situation.** ARVN took Op + Special Activity and the Special Activity was
**Govern**: it flipped Quang Tri-Thua Thien and Pleiku-Darlac from Active to
Passive Support and moved their population value from Aid to Patronage. US 47
-> 44, ARVN 43 -> 46, Aid 33 -> 30, Patronage 27. That is the post-mortem's
warning happening on the board, and it changes the standings: **ARVN is now the
faction closest to winning**, 46 against 50, and its engine is a double swing —
every point it takes comes off me. The VC is 33 against 35. Because ARVN took
an Op + SA, my menu is Event, Limited Op or Pass; the Air Lift the Kien Hoa plan
needed is out of reach for a third card, so that plan is shelved.
**Options considered.**
- *Event, Plei Mei unshaded* ("remove any 3 NVA pieces from a space with or
  adjacent to a COIN Base"). It would take the 3 NVA Troops off Binh Dinh,
  leaving a naked NVA Base against 2 ARVN Police — which flips Binh Dinh to
  **COIN Control**, and COIN Control is ARVN's score, not mine. It would cost
  the NVA 2 points (9 -> 7, a faction 9 short of winning) and hand ARVN +2 (46
  -> 48, a faction 4 short). I am not playing an event that promotes the leader.
- *Limited Op, pacify Quang Tri-Thua Thien 1 level* (Passive -> Active Support,
  pop 2, 3 Resources). +2 US, and **not** redundant with the Coup: Quang Tri has
  4 Irregulars and 4 ARVN Police but no US Troops, and the Coup Support phase
  requires US Troops, so Train is the only way to pacify it. The catch is that
  it is exactly a Govern target — COIN-controlled, ARVN cubes, outside Saigon —
  so I would be restocking the shelf ARVN just robbed.
- *Limited Op, Train Saigon, transfer Patronage to ARVN Resources.* The lever
  Kevin pointed out. Patronage is 27 of ARVN's 46, and Saigon is the one space
  Govern cannot touch, so this is the only move on the board that takes points
  off the leader without feeding it back.
**Plan.** **Limited Op -> Train in Saigon -> Transfer Patronage to ARVN
Resources.** I do not know the size of the transfer; I will read the prompt, and
if it turns out to be trivial I will **abort** and re-run the Limited Op as the
Quang Tri-Thua Thien pacification instead, recording the abort.
**Rationale.** Support outside Saigon is a revolving door while ARVN Governs:
anything I pacify in a space holding ARVN cubes can be taken straight back for
ARVN's gain, so +2 there is worth appreciably less than +2 on the scoreboard
suggests. Patronage is the opposite — it is a third of ARVN's total, it sits
where Govern cannot restock it from, and cutting it is the only way I have to
push the nearest faction away from its threshold. It is also a mechanic I have
never used in two games, and knowing what it is worth changes how I price every
remaining Train.
On deck is #22 Da Nang with VC Critical/Shaded, "remove all Support within 1
space of Da Nang; no Air Strike until Coup". I read the affected spaces as Da
Nang itself plus Quang Nam, Quang Tin-Quang Ngai and three LoCs — Hue and Quang
Tri-Thua Thien are two spaces away, reached through the Hue-Da Nang LoC — so the
cost should be the 2 points of Da Nang's Active Support and a ban on an
operation I have refused to use all game. Not worth a third consecutive pass to
deny, especially as passing would leave me eligible but with nothing built.
**Execution — I threw the action away.** The final Train action menu appeared as
I hoped, but **with only two entries**, because Saigon is already at Active
Support and so had no Pacify available:

    Choose final Train action:
    ====================================================
    1) Transfer patronage to ARVN resources
    2) Finished with Train operation
    ----------------------------------------------------
    Selection: 2

I sent **2**, intending "Transfer patronage", from the three-entry shape I had
seen on every previous Train — `1) Pacify  2) Transfer patronage  3) Finished`.
Pacify was absent, the menu renumbered, and 2 was "Finished with Train
operation". No rejection, no abort, no warning: the turn simply ended with a
Train in Saigon that placed nothing and transferred nothing.

The cause is not the interface, it is me. I chained the two sends with output
discarded and only printed the screen afterwards, so I answered a menu I had
never read — the exact failure the post-mortem lists as the decisive mistake of
the last game, committed on the same turn I wrote "I will read the prompt". The
program's menus renumber whenever an option is unavailable, and the final Train
menu drops Pacify when no selected space can be pacified.

**Rule adopted, without exception: one send per command, and print the screen
immediately before every answer. Never chain sends.**

**Result.** Nothing. US 44, ARVN 46, VC 33, NVA 9; ARVN Resources 48 unchanged,
Patronage still 27. A wasted action with ARVN 4 points from victory, and I still
do not know what the transfer is worth. The one consolation is small and does
not excuse it: a Limited Op Train could not have pacified Quang Tri-Thua Thien
either, since only the single selected space is eligible for the final action,
so the alternative plan I was weighing was worth less than I thought.

## Turn 9 — card #24 Operation Starlite — before save-049
**Situation.** US 42, ARVN 46, VC 33, NVA 13. I am first eligible with the full
menu for the first time since card #15. On deck is **#70 ROKs**, VC
Critical/Shaded: "shift Qui Nhon, Phu Bon-Phu Yen and Khanh Hoa each 1 level
toward Active Opposition". Those are Neutral, Passive Opposition and Neutral at
pop 1 each, so that event is **+3 VC — exactly 36, over the threshold, and the
VC wins at the Coup 2 Victory check.** Whatever I do here has to leave the VC
unable to reach 36.
**Can I deny ROKs?** Not reliably. If I act here I am Ineligible on #70 and the
VC, second in that card's order behind an ARVN marked Ignored, gets it. Passing
to take ROKs unshaded myself would work — but it costs this action, and I can
instead simply put the VC out of range.
**Options considered.**
- *Starlite unshaded on Quang Tin-Quang Ngai* ("remove all VC from a coastal
  Province with or adjacent to US Troops"; Quang Nam and Da Nang both hold a US
  Troop and both are adjacent). It kills 7 VC Guerrillas and 2 VC Bases — but
  Guerrillas do not score and Opposition markers persist, so it is only -2 VC,
  and it leaves 4 NVA Troops alone in the space, handing the **NVA** Control of
  a pop-2 Province: +2 NVA, taking them from 13 to 15 against a threshold of 18.
  Trading 2 VC points for 2 NVA points is not a bargain.
- *Starlite unshaded on Kien Hoa-Vinh Binh.* Removes the 3 Guerrillas and gives
  me COIN Control, but scores nothing this card and spends the action that could
  have converted it.
- *Op + Special Activity: Air Lift then Train-Pacify Kien Hoa-Vinh Binh.*
**Plan.** Op + Special Activity.
Operation **Train**, space **Kien Hoa-Vinh Binh** (2 US Troops there make it a
legal Train space), no placement — every Available pool is empty, ARVN has 0
Troops, 0 Police, 0 Rangers and I have 0 Irregulars.
Special Activity **Air Lift**: 2 US Troops from **Saigon** to Kien Hoa-Vinh
Binh, taking it to 4 US pieces against 3 VC Guerrillas and therefore **COIN
Control**.
Final Train action: **Pacify Kien Hoa-Vinh Binh 2 levels, Active Opposition ->
Passive Opposition -> Neutral**, 6 ARVN Resources of 42. **-4 VC, 33 -> 29.**
**Rationale.** This is the largest swing available and it is aimed at the only
faction that can win at the next Victory check. At 29 the VC cannot reach 36
even after ROKs gives it +3 on the next card — 32 — which is the whole point:
rather than spend my action denying one event, I move the target out of range of
that event and everything else it might find. Saigon can spare the Troops: ARVN
has just trained 8 Troops and 7 Police into it and my Base stays.
Two further reasons this space and not Quang Tri-Thua Thien's +2. First,
pacifying Opposition is a double-ended lever — this is -4 now and, once the
marker is on Neutral, a further +4 US later if I can push it to Active Support,
where pacifying my own Passive Support spaces only ever pays once. Second and
more important after last card: Kien Hoa-Vinh Binh will hold **no ARVN cubes**,
and Govern needs ARVN cubes in a COIN-controlled space outside Saigon. It is the
one piece of Support I can build that ARVN cannot take back.
**Execution.** One send per command, screen printed before every answer, as the
rule now requires. No rejections, no aborts. Three findings.
(1) The Special Activity menu now reads "1) Advise  2) Air Lift  3) Do not
perform", with a note "Momentum: #22 Da Nang prohibits Air Strike" — the program
removes the banned activity from the list rather than refusing it later, which
is another way menus renumber.
(2) **Air Lift can move ARVN Troops as well as US Troops and Irregulars/Rangers.**
I declined and moved US Troops, deliberately: a garrison with no ARVN cubes is
immune both to Govern, which needs ARVN cubes, and to VC Subvert, which removes
ARVN cubes. Kien Hoa-Vinh Binh is now an all-US space.
(3) The final Train menu offered only "1) Pacify  2) Finished" — no Patronage
transfer — which confirms Kevin's note precisely: **the transfer requires Saigon
to be one of the selected Train spaces.**
**The cost I had underweighted.** Taking COIN Control of Kien Hoa-Vinh Binh moved
the 'COIN Control + Patronage' marker from 46 to **48**. Control is ARVN's
score, so every space I bring under control feeds the faction now 3 points from
winning. Pacifying afterwards added nothing further to ARVN, but the lesson
generalises: from here, control gains are a real cost to be priced, not a free
by-product, and the Patronage transfer in Saigon is the counterweight.
**Result.** Kien Hoa-Vinh Binh: COIN Control, pacified 2 levels from Active
Opposition to **Neutral**, 6 Resources. **VC 33 -> 29.** ARVN then played
Operation Starlite unshaded on Quang Tri-Thua Thien and removed the VC Base
there: **VC 29 -> 28**, and ARVN is Ineligible on #70. So the ROKs +3 lands on a
VC at 28, taking it to 31 — 5 short of the 36 it needed. The existential threat
on this card is closed.
Standing: ARVN 48 (-2), NVA 13 (-5), VC 28 (-7), US 42 (-8). **ARVN is now the
faction to beat**, and 27 of its 48 is Patronage.

## Turn 10 — card #64 Honolulu Conference — before save-056
**Situation.** ARVN took Op + SA (Transport, shifting 2 Troops and 2 Rangers
from Pleiku-Darlac into Binh Dinh; its Assault found no space), so the Event is
open to me as second eligible. US 42, ARVN 46, VC 31, NVA 13. NVA's Bombard has
stripped Kien Hoa-Vinh Binh back to 3 US Troops against 3 VC Guerrillas and
taken the COIN Control marker off — but the Neutral marker stays, so the 4
points I took off the VC there are not refunded.
**The card.** Single text: "Aid +10 or -10. Patronage +3 or -5. If US or ARVN
executing, that Faction Pacifies as if Support Phase."
**Plan.** Take the **Event**.
- **Patronage -5**: ARVN 46 -> 41. Obvious; ARVN is the closest to victory and
  27 of its 46 is Patronage.
- **Aid -10**: 30 -> 20.
- **Pacify as if Support Phase.** That phase's test is COIN Control + US Troops
  + ARVN Police, which on the current board is satisfied by **Da Nang** (Neutral,
  pop 1) and **Quang Nam** (Neutral, pop 1), each 2 levels to Active Support for
  6 Resources: **+4 US, 42 -> 46**. Kontum qualifies but is already Active.
  Quang Tri-Thua Thien (Passive Support, pop 2) and Pleiku-Darlac (Passive
  Support, pop 1) would be worth +3 between them but hold no US Troops —
  Bombard took the last one out of Pleiku — so I expect them to be refused; if
  the program offers them I will take them.
**Rationale on Aid, which is the one genuinely close call.** The instinct is
+10, because Aid becomes ARVN Resources in the Coup Resources phase and
Resources buy pacification. But I checked what I will actually have to spend
them on: after this event puts Da Nang and Quang Nam at Active Support, the
Coup 2 Support phase has **no eligible US pacification space left** — Kontum,
Saigon and Hue are already Active, and Quang Tri-Thua Thien and Pleiku-Darlac
both fail the US Troops test. I hold 36 Resources and will not get near the
bottom of them. Aid I do not need is Aid that ARVN's **Govern** converts into
Patronage at 1 point of its score per population, which is the engine that took
3 points off me two cards ago. So I take -10 and starve it rather than +10 and
feed it.
**Expected after the card:** US 46, ARVN 41, VC 31, NVA 13. That is the first
time this game I would be the leader.
**Execution.** One send per command, screen printed before every answer. No
rejections, no aborts. The pacification offered exactly the two spaces I
predicted — Da Nang and Quang Nam — and refused Quang Tri-Thua Thien and
Pleiku-Darlac, confirming that the Support-phase test really is COIN Control +
US Troops + ARVN Police and that Irregulars do not substitute for Troops there,
even though they do for Train.
**Result.** Exactly as planned. Aid 30 -> 20, Patronage 27 -> 22 (ARVN 46 ->
41), Da Nang and Quang Nam both to Active Support for 12 Resources (US 42 ->
46). Standing: **US 46 (-4), VC 31 (-4), NVA 13 (-5), ARVN 41 (-9).** For the
first time this game the US is level at the top, and the faction that was 2
points from winning three cards ago is now 9 away.
**Where the remaining points are.** At the Coup 2 Victory check I need 51. The
Commitment phase returns all 9 Troop Casualties to Available under Medevac —
+9 US — but Commitment comes *after* Victory, so that lands for Coup 3, not
Coup 2. Before then my only pacification targets are Quang Tri-Thua Thien
(Passive Support, pop 2, +2) and Pleiku-Darlac (Passive Support, pop 1, +1),
both of which Train can reach because Train accepts Irregulars, and both of
which are Govern targets. The other lever is Kien Hoa-Vinh Binh: Neutral, pop 2,
3 US Troops against 3 VC Guerrillas, needing one more US piece for COIN Control
and then 2 levels of Train Pacify for **+4 US**.

## Turn 11 — card #83 Election — before save-060
**Situation.** NVA 19 (+1), VC 31, US 46, ARVN 39. The NVA wins at the next Coup
Victory check unless I take a point off it, and out-scoring it is not a
substitute: at exactly 50 my score is 0, not above 0, and at 51 we would both be
+1 with the tie going to the NVA. ARVN has just taken **Op Only** (Patrol along
the Saigon-Can Tho LoC, one NVA Guerrilla killed), so my menu is Limited Op or
Pass — no Event, and crucially **no Special Activity**.
**Options considered.**
- *Limited Op.* Everything useful is out of reach. Train can only select spaces
  holding US pieces, and Binh Dinh — the space I need — holds nothing but ARVN.
  Assault needs US Troops beside removable enemies, and the only US Troops
  co-located with anything are the 2 in Kien Hoa-Vinh Binh facing 3 *Underground*
  Guerrillas. Sweep is taxed by Booby Traps. What is left is Train-Pacify
  Pleiku-Darlac, Passive -> Active Support at pop 1: **+1 US**, and the NVA still
  at 19.
- *Pass.*
**Plan.** **Pass.**
**Rationale.** On deck is #67 Amphib Landing, order ARVN, US, VC, NVA. ARVN has
just acted and is Ineligible there; the VC and NVA are behind me in the order.
So if I stay Eligible I am **first eligible on #67 with the full menu, guaranteed
by turn order** — nobody precedes me, and this does not depend on a bot's choice
the way card #29 did.
The alternative is far worse than its +1 suggests. If I spend a Limited Op here I
am Ineligible on #67, where the eligible factions would be exactly VC and NVA —
so the NVA gets a free action to build on 19 and I would have no way to touch it
before the Coup, which could be the very next card. Passing keeps the NVA's score
at 19 for one more card but guarantees me the action that can cut it.
What that action can be: **Advise in Binh Dinh**. It is NVA 8 pieces against 6
COIN, and ARVN's Transport left **2 Underground Rangers** sitting there, so the
Irregular/Ranger removal takes 2 NVA pieces, leaves 6 against 6, and breaks NVA
Control for **-2, taking the NVA to 17 and below its threshold.** #67's own
unshaded side is a second route to the same end — relocate US Troops among
coastal spaces, then a free Sweep and Assault in one coastal space, with Binh
Dinh, Quang Tri-Thua Thien and Quang Tin-Quang Ngai all coastal — so I will have
two ways to do it and can pick on the board I see.
**Execution.** Passed (2). No rejections. Eligibility confirmed as the plan
requires: US, VC and NVA Eligible, ARVN Ineligible — so on #67 the order is
ARVN (out), **US**, VC, NVA and I act first.
**Result.** +3 ARVN Resources (24). No board change. NVA stays at 19 (+1) for
one more card, which is the price of the guaranteed action.
