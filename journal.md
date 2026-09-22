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
