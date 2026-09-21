# Post-mortem: TestGame2, US faction, won at the 3rd Coup (margin 4)

Companion to `RULES_LEARNED.md` (mechanics, now covering both games) and
`journal.md` (every turn in full). This is the strategic account: what I
intended, what happened, what I would do differently. Scores are the
program's, from `render.py`. The TestGame1 post-mortem is kept as
`POSTMORTEM_TestGame1.md`; this one is written against its lessons.

## The result in one line

The US won at the third Coup with 54 — 31 points of Support and 23 in the
force pool — because the VC and the NVA were each knocked back under their
thresholds on the card before they could cross, and the Coup card then arrived
one card after I had crossed mine.

## The plan, and what it turned into

I started from the last game's verdict: build Support on the map, get a second
US Base into a pop-2 Province early, and watch the VC's number rather than my
own. The first half of that went as intended. Saigon was Active Support on my
first action (+6 for 3 Resources), Da Nang and Kontum followed at Coup 1, and
ARVN's Redeploy then dropped Police into both pop-2 Highlands I wanted.

The Base never happened, and Kevin was right to ask why. At Coup 1 I committed
six Troops and no Base, on the reasoning that ARVN's Police already made the
Highlands pacifiable; the NVA's twenty-Troop March and Attack over the next two
cards took every one of those Troops into Casualties and the VC's Subvert
stripped the Police out from under the plan. At Coup 2 I skipped the Base
again, this time because Sappers was on deck. Two games, four US Bases in the
box or Out of Play for the whole of both. It did not cost this game, but the
pattern is the same one the last post-mortem named.

What actually won was a different plan that formed around card #63, once the
deployment was gone:

- **Saigon as the anchor.** Twelve of my points sat in the one space Govern
  cannot touch; the VC knocked it to Passive once and I bought it straight back.
- **Advise as the weapon.** The Irregular/Ranger removal turned out to reach
  Underground Guerrillas and undefended Bases, cost nothing, and — because
  Control needs strictly more pieces than everyone else combined — could break
  an NVA Control for two points with a single Special Activity. Every enemy
  piece I removed all game, I removed this way.
- **Air Lift as the engine.** Moving Troops map-to-map costs no points, so two
  Troops out of Saigon into an Opposition Province followed by a Train-Pacify
  was a free four-point swing. Kien Hoa-Vinh Binh went from Active Opposition
  to Passive Support in two such actions: −6 VC, +2 US.
- **Counting only what scores at the next Victory check.** Victory is the
  first phase of a Coup, so returning casualties and Coup pacification arrive
  too late for that check. Once I saw that, every action was priced by what
  the next check would read, and two of my passes were made to guarantee — by
  turn order, not by a bot's whim — the one action that put a rival back under
  its line.

## Why the win came early

Kevin had not seen a US win this early. Four structural things did most of it,
and only the last is skill.

1. The US threshold counts the force pool, and the pool starts near 23 points.
   With ARVN garrisoning the Cities for free, I never had to buy a position
   to hold Support; I only had to buy Support, and I bought it with ARVN's own
   Resources — 60 of them across the game, from a bot that finished with 57
   unspent.
2. Medevac. I declined that event on card #15 and the ARVN bot played it
   itself, so all twelve Troop Casualties came back to Available at Coup 2
   instead of eight. That is the difference between 50 and 54 at the check.
3. The bots fight each other. The NVA converted a VC Base to its own; the VC's
   Body Count cost the NVA two Controls; ARVN's Critical events cleared
   Pleiku-Darlac, killed a VC Base and denied the NVA a −8. And because NVA
   and VC stacks shared the same Provinces, four of the NVA's six Controls sat
   one or two pieces from collapse for the whole of campaign 3.
4. Control breaks are the cheapest points in the game, and I found that in
   time to use it twice.

Note also that a human win in any Coup is the easier setting; on the standard
rule this game was still going.

## What went right

- **Kien Hoa-Vinh Binh, card #24.** With the VC at 33 and ROKs (+3, to 36 and
  a VC win) on deck, I could not deny the event, so I moved the target out of
  its range: Air Lift for Control, Pacify two levels, VC to 29. ROKs then
  landed on 28 and read 31.
- **Binh Dinh, card #67.** The NVA reached 19 (+1) on card #104. ARVN's Op
  Only on #83 blocked the Special Activity I needed; I passed, took first
  eligibility on #67 by turn order, and one Advise removal put the NVA on 17.
- **Honolulu Conference, card #64.** Patronage −5 and a full Support-phase
  pacification in one card: ARVN 46 → 41, US 42 → 46, and for the first time I
  led.
- **The two turn-order passes** (#66, #83). Each converted a Limited Op worth
  +1 or +2 into a guaranteed full action on the next card, with the guarantee
  resting on the card's printed order rather than on a bot choosing to act.
- **Reading the cards.** Da Nang's "within 1 space" cost exactly the 2 I
  predicted; ARVN's Critical marking on Annam did deny the NVA the −8 as
  expected; the Coup-phase order was read from the rules text before it
  mattered rather than after.
- **Menu discipline after the one lapse.** One send per command, screen
  printed first, for the last six turns. No further errors.

## What went wrong, in order of cost

1. **The Coup 1 deployment.** Six Troops out of the box (−6 points), three of
   them into a Province next to eight NVA Troops, with no Base and no ARVN
   cubes of my own placing to hold it. All six were Casualties within two
   cards, and with them went 21 points of Aid at the next Coup. The honest
   alternative was not "no deployment" but a Base plus placed ARVN cubes in
   one space, or a smaller deployment kept where a Base could double its
   Assault.
2. **Card #59.** I meant to transfer Patronage from Saigon and sent "2" to a
   menu I had not printed; Pacify was absent because Saigon was already
   Active, the menu had renumbered, and 2 was "Finished". A whole action, with
   ARVN four points from winning. This is the exact mistake the last
   post-mortem called decisive, repeated on the same turn I wrote "I will read
   the prompt."
3. **Card #29.** I passed so that ARVN would spend its eligibility on
   Tribesmen and leave me first on Fact Finding. ARVN passed too. A dead card,
   and the −1 I was dodging landed anyway. Denial that rests on a bot's choice
   is not denial.
4. **Aid.** I took −10 at Honolulu to "starve Govern", then established two
   cards later that Govern is nowhere near Aid-constrained at those levels;
   what Aid changes is the Resources my own pacification spends. Roughly
   neutral, but reasoned wrongly and written up as a win.
5. **Eleven of twenty-four cards without a US action.** Nine Ineligible, two
   eligible but third or fourth in order behind two acting bots. Some of that
   is the sequence of play; some is four passes. The right passes (#66, #83)
   bought actions that decided the game; the wrong one (#29) and the marginal
   one (#72) bought nothing.
6. **A narrow toolkit.** No Assault, no Air Strike, no Sweep, no Patrol in
   thirteen turns. Air Strike's shift toward Opposition made it a liability
   with the VC that close; Sweep was taxed by Booby Traps; but Assault was
   never even tested, and the Patronage transfer that Kevin pointed out was
   never executed.

## The decisive stretch

The game turned twice, both times on a rival sitting at +1 or one point short.

From card #118 the VC was at 33 with a threshold of 35. Fact Finding gave me
Quang Tri (+4) and an Air Lift into Kien Hoa; Subvert took the Control back;
two passes and a wasted Limited Op followed while ARVN's Govern took three
points off me. Then Operation Starlite: first eligible, Air Lift, Pacify, VC to
29 — and ARVN, taking the event I had declined, removed a VC Base for 28. ROKs
came and went at +3. That stretch was won on one action.

From card #104 the NVA was at 19 (+1). ARVN's Op Only on Election closed my
Special Activity; I passed; on Amphib Landing the Advise on Binh Dinh read
"Remove NVA Control marker" and 19 → 17. Annam then arrived with an ARVN
Critical marking that denied the NVA a −8 against Hue and Da Nang, Coup 2
passed with nobody above 0, Medevac returned twelve Troops, and Vietnamization
— ARVN's pivotal — erased the Sappers card that would have taken my only
Province Base. One Air Lift and Pacify later I stood at 56; the NVA's Terror
took it to 54; the Coup card was the very next draw.

## What the next player should do differently

- **Price every Commitment piece at one point and give it a job the box
  cannot do.** Assault beside a Base, repair capability in a big Support
  space, or a reserve to Air Lift from. Air Lift turns a Saigon garrison into
  a mobile army at no cost; Commitment is the only phase that can feed it.
- **Put a Base on the map, and do it on purpose.** Two games, no Province
  Base ever placed. It is the only way to Train ARVN cubes into a Province,
  and a Base with cubes beside it is what would have survived the March that
  killed my six Troops.
- **Advise every action you can.** Keep Underground Irregulars and Rangers in
  the spaces where the enemy is — Train places Irregulars for free, and ARVN
  Transport will sometimes deliver Rangers for you. Two pieces per space, two
  spaces, no Resources, and it breaks Controls.
- **Pacify Opposition, not just your own Neutral spaces.** Active Opposition
  to Neutral is −4 to the VC at pop 2, and the next two levels are +4 to you.
  A space with no ARVN cubes is immune to Govern and to Subvert.
- **Count what scores at the next Victory check.** Victory is the first phase.
  Casualties returning and Coup pacification are for the check after.
- **Pass only when turn order guarantees the action you are buying.** Never
  when it depends on a bot choosing to act. Both cases are in the journal.
- **Print the menu.** The last two games each lost an action to a menu
  answered from memory. One send per command; the screen before every answer.
- **Test the tools I did not use.** Assault with a US Base in a City; the
  Patronage transfer from Saigon; Air Strike once the VC is safely under its
  threshold. Their values are still unknown after two games.
- **Watch ARVN as a rival, not a partner.** Govern is a double swing against
  you; every Control you create is its score; and it is the faction whose
  Critical events can also win you the game. Keep Support in Saigon and in
  spaces without its cubes.

## Numbers for the record

Scores at each Coup's Victory check:

| Coup | US | VC | NVA | ARVN | Note |
| --- | --- | --- | --- | --- | --- |
| 1 (#125 Nguyen Khanh) | 42 | 27 | 6 | 36 | nobody above 0; US 48 → 42 after Commitment |
| 2 (#128 Nguyen Van Thieu) | 47 | 31 | 17 | 41 | nobody above 0; NVA had been 19 two cards earlier |
| 3 (#127 Nguyen Cao Ky) | 54 | 30 | 19 | 43 | **US wins by 4** |

Thirteen US actions: 7 Op + Special Activity, 1 Event, 1 Limited Op (wasted),
4 Passes. Eleven event cards without a US action (9 Ineligible, 2 squeezed out
by order). Coup decisions: two Support phases (Coup 1 pacified two Cities; Coup
2 had no eligible space), two Commitment phases (6 Troops each, no Bases).
Highest US total 56, lowest 36.

Pacification: 18 levels in 9 spaces for 54 ARVN Resources — +29 US Support,
−6 VC Opposition. Air Lifts: 3, moving 6 Troops. Enemy pieces removed by US
action: 4 VC Guerrillas, 1 VC Base, 6 NVA Troops, all by Advise. Pieces lost:
14 Troops and 1 Irregular to Casualties across the game, 13 of them returned by
Medevac at Coup 2, 2 still in Casualties at the end; nothing Out of Play; no
Base lost. Container losses: 6, all at the card prompt, no state lost.
