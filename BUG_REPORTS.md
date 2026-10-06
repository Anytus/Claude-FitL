# Bug reports for the `fitl` program (github.com/sellmerfud/fitl)

Issues found in Curt Sellmer's Tru'ng bot program while running the harness.
They are collected here and presented upstream in batches rather than one at
a time. Each entry records the rule, the program's behaviour, the evidence,
the cause in the source, and a suggested fix, in the form of a ready-to-post
issue. Status is one of: **pending** (not yet reported), **reported #N**,
**fixed vN** (upstream commit named).

The harness build in `fitl/lib` is v1.53 plus `fitl/fitl-1.53-harness.patch`.
Entries marked "harness: patched" are also fixed in that build; the others
are present in the build the games run on.

---

## 1. Three adjacencies missing from the map table — fixed v1.54 (issue #59)

**Status.** Reported by Kevin as issue #59; fixed upstream by commit
`e34dfe7` "fix(59): Add missing entries to adjacency map" (2026-09-21),
released as v1.54. Harness: patched (the build closes the table under
symmetry, which covers exactly these three).

**Rule.** 1.3.6: "Any 2 spaces meeting one of the following conditions are
adjacent: Spaces that border on (touch) one another. Provinces that would
touch but for separation by a LoC. LoCs or Provinces separated by Towns."
1.3.1: "Towns are not spaces, merely boundaries between adjacent LoCs."

**Behaviour.** Three pairs were listed in one direction only, so movement
that looks up adjacency from the destination (March, for one) did not offer
the other side as an origin:

- LOC Cam Ranh -- Da Lat and Quang Duc-Long Khanh (via Da Lat)
- LOC Da Nang -- Dak To and LOC Kontum -- Dak To (via Dak To)
- LOC Saigon -- An Loc -- Ban Me Thuot and Khanh Hoa (via Ban Me Thuot)

**Fix.** Upstream added the missing entries to `adjacencyMap` in
`FireInTheLake.scala`; the v1.54 diff adds precisely the three pairs above.

---

## 2. Limited Op Patrol allows the follow-up Assault in a City — pending

**Status.** Pending. Present in v1.53 and in master at v1.54 (checked
2026-09-22). Harness: not patched. Affects human US and ARVN players only;
both bot Patrols already check for a LoC.

**Draft issue text:**

> **Title:** Limited Op Patrol allows the follow-up Assault in a City (rule 3.2.2)
>
> Rule 3.2.2 says the Patrol's free Assault is "in 1 LoC" and, for a Limited
> Operation, "the Assault must be in the destination LoC." A human player
> whose Limited Op Patrol ends in a City is currently offered, and given, an
> Assault in that City.
>
> **To reproduce** (Full scenario, US human, v1.53 and current master):
>
> 1. Put an insurgent piece in Can Tho (e.g. `adjust Can Tho`, add 2 VC
>    Active Guerrillas).
> 2. As the second eligible faction, take a Limited Op Patrol and move the
>    2 US Troops from Saigon to Can Tho.
> 3. After "Activating guerrillas on LOCs", the menu offers "Assault at one
>    LOC". Choosing it runs the assault in Can Tho without asking for a
>    space, since it is the only candidate:
>
> ```
> Choose one:
> 1) Assault at one LOC
> 2) Do not Assault at one LOC
> Selection: 1
>
> US assaults in Can Tho
> The assault inflicts 2 hits
> Remove 2 VC Active Guerrillas from Can Tho to AVAILABLE
> ```
>
> **Cause.** In `Human.scala`, `executePatrol` / `assaultOneLOC`, the
> Limited Op branch uses the Patrol destination as the assault candidate
> without checking that it is a LoC; the non-limited branch filters
> `game.locSpaces`:
>
> ```scala
> val locs = if (params.limOpOnly)
>   limOpDest.toList map game.getSpace filter canAssault
> else
>   game.locSpaces filter canAssault
> ```
>
> The bot Patrols (`US_Bot.patrolOp`, `ARVN_Bot.patrolOp`) already test
> `sp.isLoC` on the Limited Op destination, so only human US/ARVN players
> are affected.
>
> **Suggested fix:**
>
> ```scala
> val locs = if (params.limOpOnly)
>   limOpDest.toList map game.getSpace filter (sp => sp.isLoC && canAssault(sp))
> else
>   game.locSpaces filter canAssault
> ```

**Evidence.** Reproduced 2026-09-22 on the harness build in a throwaway
two-human game (ARVN Patrol + Govern first, then US Limited Op Patrol
Saigon -> Can Tho); the program output above is verbatim. The playing model
should treat a City offered as a Patrol assault space as illegal and decline
it.

---

## 3. A Bot loops forever in some games — pending

**Status.** Pending. Found by the headless all-Bot runner on the harness
build (v1.53 plus harness patch); 13 of 1,000 all-Bot Full-scenario games
(1.3%) in the first calibration run.

**Behaviour.** The game never finishes: the US Bot's Air Lift spends minutes
of CPU in Bot.movePiecesToDestinations -> movePiecesFromOneOrigin ->
mustKeepInOrigin -> selectPiecesToKeep -> KP_KeepCoinFirepowerGreaterOrEqualToVulnerable
(seen on seed 9). Seeds 9, 16, 38, 86, 193, 249, 350, 461, 515, 538, 656, 698
and 767 time out; 9, 16 and 38 do so through the program's own interactive
main loop as well (`--via-main`), so it is in the Bot code, not the runner. Not yet reduced to a reportable case.

## 4. Bot placement assertions — pending

**Status.** Pending. Found by the headless all-Bot runner; 18 of 1,000
all-Bot Full-scenario games (1.8%) in the first calibration run. Seed 1
reproduces through the program's own main loop as well. Not yet reduced to
reportable cases; the Bot and card are not yet identified.

- "Cannot place more than 2 bases in Saigon": seeds 1, 145, 242, 343, 359,
  403, 444, 586, 725.
- "Cannot place more than 2 bases in Quang Tin-Quang Ngai": seeds 197, 686,
  746, 757. Two Base placements in one space are probably the same bug.
- "Insufficent pieces in the available box": seeds 229, 261, 789, 947, 969.

## 5. Card #9 shaded with a human US can ask for more Troops than a space holds — pending

**Status.** Pending. Found by `fitl.USPlayer` (`--us-human`).

**Behaviour.** When a Bot executes the shaded side of #9 (Psychedelic
Cookie) and the US is human, the program asks `Remove troops from which
space` and then `Remove how many troops from <space> (0 - n)`, where n is the
number still to remove, not the number of US Troops in that space. An answer
above the space's Troops stops the game with `AssertionError: removeToOutOfPlay()
<space> does not contain all requested pieces` (Card_009.executeShaded,
FireInTheLake.removeToOutOfPlay). A person typing too high a number would hit
it too. Seeds 20, 22, 33, 34, 114, 115, 144, 157 and 198 with `--us-human
--us-policy policies/fit3flat.json` while the default answer was the largest
number; USPlayer now answers 1 there.
