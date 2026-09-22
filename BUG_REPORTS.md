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
