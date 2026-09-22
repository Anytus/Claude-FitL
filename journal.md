# journal.md — full turn plans and rationales (TestGame5)

This is the audit artifact. Every US action, Coup-round decision, and
pivotal-event decision gets an entry here **before** the first answer is
sent to the program, in the format given in `CLAUDE.md`. Rejections by the
program, aborts, and deviations from the plan are recorded verbatim in the
entry's Execution section. Previous games' journals are under `archive/`.

## Turn 1 — card #26 LRRP — before save-000
**Situation.** First card of the game, order US, VC, ARVN, NVA, everyone
Eligible, and I am first. The VC is marked **Critical/Shaded** on LRRP, whose
shaded side sends 3 US Irregulars from the map to Casualties and shifts each
space they were in 1 level toward Active Opposition. My three Irregulars sit
one each in Quang Tri-Thua Thien (pop 2, Neutral), Binh Dinh (pop 2, Neutral)
and Pleiku-Darlac (pop 1, Neutral): the shaded side would be roughly 5 points
of new VC Opposition and the destruction of the Advise engine on card one.
ARVN Resources 30 against Econ 15, so the pacification gate is wide open.

**Options considered.**
- *Event unshaded* ("US places 3 Irregulars outside the South, then free Air
  Strikes"). It denies the VC the Critical shaded side, but the Irregulars land
  in Laos/Cambodia where Advise cannot use them, and Air Strike removes only
  NVA Troops and *Active* Guerrillas — every NVA Guerrilla outside the South is
  Underground, so the strike hits nothing but a Trail degrade from 1, which is
  already near the bottom. Denial for almost no build.
- *Op + Special Activity.* An Advise would be worth two enemy pieces, but it
  leaves the second-eligible menu holding `Event`, and the VC is Critical for
  the shaded side. That hands the VC exactly the card I must not give it.
- *Op Only* (Op with no Special Activity). RULES_LEARNED §2, confirmed twice:
  it closes the Event to the whole second-eligible slot. The VC is held to a
  Limited Op or a Pass, the Critical shaded LRRP is dead, and I still get a
  full multi-space operation. The price is one Advise.

**Plan.** **Op Only — Train**, three spaces, no Special Activity.
1. **Saigon** — `Do not place forces` (selected only to make it the Pacify
   space).
2. **Binh Dinh** — place 2 Irregulars. COIN goes to 4 pieces against VC 3
   (2 Guerrillas + Base): COIN Control of a pop-2 Highland, the pop-2 Province
   engine all four post-mortems demand, and a second Underground Irregular for
   future Advise.
3. **Pleiku-Darlac** — it holds a US Base and Resources exceed Econ, so place
   ARVN cubes: 2 Troops + 4 Police for 3 Resources. COIN 9 against VC 3 is
   Control of a pop-1 Highland with ARVN **Police** present, which is the
   strict Coup Support-phase test; it also drains ARVN's Available box.
Final Train action: **Pacify Saigon**, 1 level, Passive Support -> Active
Support, 3 Resources. Then `n` to the Special Activity question, which prints
the Op Only box and closes the Event.
Expected: Total Support 15 -> 21, US 38 -> 44. Two new COIN Controls (so ARVN
rises about 3, from 35, which is not yet a threat). ARVN Resources 30 -> 24,
still well above Econ 15. VC held to a Limited Op and denied ~5 points.

**Rationale.** The single largest point on this board is Saigon at pop 6 going
Passive -> Active Support for 3 Resources, and Saigon is the one space ARVN's
Govern can never reach. Doing it inside an Op Only buys the +6 and the denial
of a VC Critical card in the same action, which is the trade TestGame4 found
and recommended. The two Controls cost nothing but free Irregulars and 3
Resources, and they are the precondition for pacifying Binh Dinh later —
TestGame1's post-mortem names the absence of exactly that pop-2 engine as the
reason it lost. I am deliberately not putting Irregulars into Quang
Tri-Thua Thien, next to North Vietnam and Central Laos, which is where
TestGame4 lost its whole Advise engine to one NVA operation.

**Execution.** One stop, no rejections. The `seq` ran steps 1-19 as written
(Saigon `Do not place forces`; Binh Dinh 2 Irregulars; Pleiku-Darlac 2 ARVN
Troops + 4 Police; `Finished selecting spaces`; Pacify Saigon 1 level to
Active Support). Step 20 (`final Train action` => `Finished`) did **not**
match and nothing was sent for it: after the Pacify resolved, the program did
not return to the `Choose final Train action` menu at all but went straight to
`Do you wish to perform a special activity? (y/n)`. So a Train's single Pacify
ends the operation by itself. I continued with a one-step `seq` sending `n`,
which printed `Move the US cylinder to the Op Only box`. Nothing was rejected
and nothing was aborted.

**Result.** Exactly as planned. `Move the 'Support + Avail US' marker from 38
to 44`; Saigon Active Support; Binh Dinh and Pleiku-Darlac both now read COIN
Control; ARVN Resources 30 -> 24; ARVN Available drained to 6 Troops and 6
Police. The denial worked: the VC drew its Tru'ng card and was held to a
**Limited Op** (Rally, 3 Guerrillas into Tay Ninh), and the Critical shaded
LRRP was never played. Scores US 44 (-6), VC 27 (-8), ARVN 38 (-12), NVA 4
(-14). One thing to carry forward: Binh Dinh now holds 3 Irregulars in one
space, which is the concentration TestGame4's post-mortem warns against; it is
adjacent to Southern Laos, and I should spread them at the first cheap chance.


## Turn 2 — card #68 Green Berets — before save-008
**Situation.** ARVN opened #68 with an **Op Only** (Train in Saigon; the Duong
Van Minh leader effect also paid Aid +5 to 20), which closes the Event to
everyone behind it, so my menu is `Limited Op` or `Pass`. The VC is marked
**Critical/Shaded** here, and shaded Green Berets reads "Remove any 3
Irregulars to Available and set 1 of their Provinces to Active Opposition" —
aimed straight at the 3 Irregulars I stacked in Binh Dinh last card, which
would also take a pop-2 Highland from Neutral to Active Opposition: about 4 VC
points, my COIN Control there, and the Advise engine.

**Options considered.**
- *Pass.* +3 ARVN Resources and keeps me Eligible for #43 Economic Aid. But I
  am third in that card's order (NVA, ARVN, US, VC) behind an NVA marked
  Ignored and an ARVN marked Performed/Unshaded, so both are likely to act and
  squeeze me out anyway. Worse, a pass leaves the VC the second-eligible slot
  on this card. I believe ARVN's Op Only has closed the Event to the VC as
  well, but that is an inference about how long the closure lasts, and
  TestGame4's post-mortem is explicit that a plan resting on an inference
  about a bot's slot is a bet, not a plan.
- *Limited Op.* Two factions will then have acted and the card ends with the
  VC never getting a turn at all. Certain denial instead of probable denial,
  and it buys points rather than 3 of ARVN's Resources.

**Plan.** **Limited Op — Train in Binh Dinh.** `Do not place forces` (I hold
only 1 Irregular in Available and Binh Dinh already has 3; adding a fourth is
the concentration I want to break up, not deepen). Final Train action:
**Pacify Binh Dinh, 2 levels, Neutral -> Active Support**, 6 Resources.
Expected: Total Support 21 -> 25, US 44 -> 48. ARVN Resources 24 -> 18, which
still clears Econ 15, so the gate stays open next card. ARVN gains 0 (Binh
Dinh is already COIN-controlled, so no new Control).

**Rationale.** Binh Dinh is the best pacification on the board: pop 2 against
pop 1 everywhere else I could reach, so 2 levels are worth +4 rather than +2,
at the same 6 Resources. It is also the durable choice — Support and
Opposition persist through changes of Control, so even if the VC rallies a
Guerrilla back and flips Binh Dinh out of COIN Control, the 4 points stay on
the board. And the space holds no ARVN cubes, so ARVN's Govern, the largest
single leak in the last three games' US scores, cannot reach it. Ending the
card myself, on a card where a rival is Critical for an event aimed at my own
pieces, is the TestGame4 lesson applied.

**Execution.** One stop, no rejections, no aborts. Steps 1-7 ran as written
(`Limited Op`, `Train`, `Select a space`, `Binh Dinh`, `Do not place forces`,
`Pacify`). Step 8 (`Pacify in which space` => `Binh Dinh`) stopped the
sequence: `no menu entry starts with 'Binh Dinh'`. Nothing was sent. The
reason is the single-candidate rule — with Binh Dinh the only Train space the
program printed `Pacify in which space:  Binh Dinh` and resolved it itself,
so by the time my step was tested the screen already held the *level* menu.
I continued with a one-step `seq` sending `Shift 2 levels to Active Support`.
Two lessons for `PROMPTS.md`: a Limited Op Train has exactly one candidate at
`Pacify in which space`, so that step should be omitted; and my Turn 1 note
that Pacify ends the Train was confirmed again here.

**Result.** As planned. `US Pacifies 2 levels in Binh Dinh`, `Decrease ARVN
resources by -6 to 18`, `Place Active Support marker in Binh Dinh`, `Move the
'Support + Avail US' marker from 44 to 48`. The card then ended immediately
(`Move the US cylinder to the LimOp box`, eligibility adjusted, next card
drawn) with the VC never acting, so the Critical shaded Green Berets aimed at
my 3 Binh Dinh Irregulars was denied outright — the second Critical VC event
killed by turn order in two cards.

## Turn 3 — Coup round 1, card #127 Nguyen Cao Ky — Support phase
**Situation.** Victory phase read `None of the Factions has achieved its
victory condition` (US 48 against 50). Resources phase: no sabotage, Econ
re-set to 15, ARVN earned +35 to **53**, and the Casualties box was empty so
Aid took no deduction. Nguyen Cao Ky is the new leader, so pacification costs
**4 per level**, not 3. The program offers exactly the three spaces I expected
from the strict test (COIN Control + US Troops + ARVN Police): Da Nang,
Kontum, Pleiku-Darlac. Hue and Kien Hoa-Vinh Binh fail it for want of US
Troops; Saigon and Binh Dinh are already at Active Support.

**Options considered.** All three are Neutral pop-1 spaces, so each is worth
+2 (Neutral -> Passive -> Active Support) for 2 levels at 4 Resources a level.
Six levels cost 24, leaving 29 against Econ 15 — comfortably inside the
headroom, and the headroom is checked level by level, so nothing should be cut
short. There is no reason to take fewer: these are free points in a phase that
happens after the Victory check, ARVN's Resources reset every Coup anyway, and
leaving them unspent only funds the bot's own four-space Sweeps.

**Plan.** Pacify all three, 2 levels each, to Active Support: Da Nang, Kontum,
Pleiku-Darlac. Then `Finished pacifying spaces`. Expected: Total Support
25 -> 31, US 48 -> 54, ARVN Resources 53 -> 29.

**Rationale.** +6 for Resources I do not own and cannot carry forward. The one
caveat is that Pleiku-Darlac holds the 6 ARVN cubes I placed on turn 1, so it
is a Govern target worth 1 level; Da Nang and Kontum hold a single ARVN Police
each, so they are cheap for ARVN to reach too. That is an argument for
pacifying them now and re-buying later, not for leaving the levels on the
table.

**Execution.** Steps 1-6 ran as written. Step 7 (`Choose space to pacify` =>
`Finished pacifying`) stopped the sequence, nothing sent: the third
pacification used the last candidate and the program ended the phase itself
rather than re-offering the menu. Same family as my two earlier stops — when
the list empties or holds one entry, the program resolves it without asking.

**Result.** All three as planned, and better: `US Pacifies 2 levels in Da
Nang` / `Kontum` / `Pleiku-Darlac`, 8 Resources each, Active Support markers
on all three, ARVN Resources 53 -> 29. Then **ARVN pacified Hue** 1 level to
Passive Support for 4 of its own Resources, which is +2 US I did not pay for.
`Move the 'Support + Avail US' marker from 48 to 56`. Note for the rest of the
campaign: ARVN finished the phase on 25 against Econ 15, so only 10 of
headroom — about two levels at Nguyen Cao Ky's 4 per level — is left to fund
pacification until the next Coup.

## Turn 4 — Coup round 1, card #127 Nguyen Cao Ky — Commitment phase
**Situation.** No casualties, so no rotation and no free placement. The prompt
is `Move up to 10 US Troops and up to 2 bases among Available box, COIN
controlled spaces, LoCs and Saigon`. US stands at 56 with 21 Troops and 2
Bases (23 points) in Available. Every piece moved out of the box is -1 US
point, immediately and directly.

**Options considered.**
- *Move nothing.* Keeps 56, six clear of the threshold. But it leaves me with
  **no pacification target at all**: every space holding a US piece is now at
  Active Support except Quang Tri-Thua Thien, which is Uncontrolled and cannot
  be pacified. A US score made entirely of box points is precisely what lost
  TestGame1.
- *Move a large force plus a Base.* Four Troops and a Base would unlock Hue,
  Kien Hoa-Vinh Binh and ARVN cube placement in a Province, but costs 5 points
  for benefits that mostly mature at Coup 3. The arithmetic is unkind: a pop-2
  Passive -> Active pacification pays exactly +2, so two Troops spent to unlock
  it is a wash for the Coup 2 check.
- *The real reason not to overspend here:* **Air Lift moves Troops map-to-map
  for free.** The 8 US Troops already on the map (Da Nang 2, Kontum 2, Saigon
  2, Binh Dinh 1, Pleiku-Darlac 1) can be lifted into any space I want to
  Train and pacify, at no point cost, as a Special Activity. Commitment is not
  the only way to put a Troop where I need one; it is only the way to take one
  out of the scoring box.

**Plan.** Move **2 US Troops from Available into Kien Hoa-Vinh Binh**, and no
Bases. US 56 -> 54. Then `Finished moving pieces`.

**Rationale.** One modest commitment with a job the box cannot do, which is
TestGame2's rule. Kien Hoa-Vinh Binh is a pop-2 Lowland at Passive Support
held by a single ARVN Police — the most valuable and least defended Support
space I own, and the space TestGame4 was won on. Two Troops there defend 2
points, make it a Train space so a single level of pacification takes it to
Active Support for +2, and leave it a strict-test target for the Coup 2
Support phase. Everything else I keep in the box, because pacification for the
whole of campaign 2 is capped at roughly two levels by ARVN's remaining
headroom, so extra Train spaces would have nothing to spend on them, and Air
Lift can deliver Troops to whatever target the Resources do stretch to.

**Execution.** Two `seq` calls, no rejections, no aborts. The first ran
`Move troops` -> `Available box` -> `Kien Hoa-Vinh Binh` -> `2` and printed
`Place 2 US Troops from AVAILABLE into Kien Hoa-Vinh Binh`; the destination
prompt is a 32-entry menu of every COIN-controlled space, LoC and Saigon, as
recorded. The second sent `Finished moving pieces`. The withdrawal prompt
printed for 0 pieces as expected: `No shifts in support possible`.

**Result.** `Move the 'Support + Avail US' marker from 56 to 54`, exactly the
-2 planned. The rest of the Coup round: the VC spent its whole Agitate Total
of 2 on **Quang Tri-Thua Thien**, taking it straight to Active Opposition
(VC 28 -> 32) — the one pop-2 space I hold pieces in but do not control, and I
had nothing that could answer it. ARVN's Redeploy moved 4 Police from
Pleiku-Darlac to Binh Dinh, which is a mixed gift: it hardens my best Province
but puts ARVN cubes into an Active Support pop-2 space, so Binh Dinh is now a
Govern target. NVA Redeploy pulled 4 Troops back to Southern Laos. Reset put
the Trail at 2, flipped everything Underground, and set the new Agitate Total
to 1.

Two lessons recorded for later: an Agitate Total left standing is spent after
the Victory check where nothing can answer it, so Quang Tri needed dealing
with before the Coup and did not get it; and my Commitment reasoning above was
sound but the position it left is thin — I have exactly one pacification
target in campaign 2 (Kien Hoa-Vinh Binh) and roughly two levels of ARVN
headroom to pay for it.

## Turn 5 — card #75 Sihanouk — before save-019
**Situation.** ARVN opened with an Op + Special Activity, and the VC and NVA
both spent themselves on #107, so I am the only Eligible faction left: my menu
is `Event`, `Limited Op`, `Pass`. The board has changed badly since the Coup —
the NVA marched 5 Troops into Pleiku-Darlac (breaking COIN Control there), 4
into Quang Tin-Quang Ngai and 2 into Kien Giang-An Xuyen, taking NVA Control of
both, and 1 into Quang Nam. NVA is 12 of 18. But the biggest single number on
the board is mine: the VC's Burning Bonze knocked **Saigon** back to Passive
Support, and Saigon is pop 6.

**Options considered.**
- *Event unshaded* ("US or ARVN free Sweep into or in any Cambodia spaces,
  then free Assaults in one"). Cambodia is pop 0, so a strike there costs no
  Support, and the Parrot's Beak holds 2 NVA Bases. But my only space adjacent
  to Cambodia is Pleiku-Darlac (Northeast Cambodia and The Fishhook), which
  are both empty; the Parrot's Beak is out of reach, and the NVA at 12 is not
  the faction closest to its line.
- *Pass.* Keeps me Eligible for #116 Cadres, but I am **fourth** in that
  card's order behind an ARVN marked Critical and a VC marked Critical, so I
  would almost certainly be squeezed out. A pass buying nothing is the mistake
  TestGame2 named.
- *Limited Op — Train Saigon, Pacify 1 level.* Passive -> Active Support at
  pop 6 is **+6 for 4 Resources**, the best rate anywhere on the map, and in
  the one space ARVN's Govern cannot reach.

**Plan.** **Limited Op — Train in Saigon.** `Do not place forces` (placing
ARVN cubes would cost 3 Resources and drop me to 19, and the pacification then
would leave 15, which is not *above* Econ 15 and would be refused — the
headroom is too tight to spend on anything else). Final Train action:
**Pacify Saigon, 1 level, Passive -> Active Support**, 4 Resources.
Expected: Total Support 27 -> 33, US 48 -> 54. ARVN Resources 22 -> 18.

**Rationale.** Six points for one level is twice the rate of anything else
available and it re-takes the anchor the VC just knocked over. Becoming
Ineligible on #116 costs nothing, because I would have been squeezed out of
that card anyway. The NVA build-up is the real problem on this board, but a
Limited Op cannot carry a Special Activity, so Advise is not available to
answer it this card; the answer has to come next time I get a full Op.

**Execution.** The container was reclaimed before the first answer went in.
`ctl.py resume TestGame5` reloaded the latest save and returned to the same
`(perform or ?)` prompt on #75 with nothing lost, exactly as the earlier games
recorded. The `seq` then ran all 8 steps with no stop and no rejection — the
first clean full-action sequence of the game. Note that the auto-resolve I
predicted did happen: `Pacify in which space` was never shown, the program
went straight to the level menu, and the `*` guard absorbed it.

**Result.** As planned: `US Pacifies 1 level in Saigon`, `Decrease ARVN
resources by -4 to 18`, `Flip Passive Support marker in Saigon to Active
Support`, `Move the 'Support + Avail US' marker from 48 to 54`.
