# Post-mortem: TestGame3, US faction, won at the 3rd Coup (margin 8)

Companion to `RULES_LEARNED.md` (mechanics, now covering three games) and
`journal.md` (every turn in full). This is the strategic account: what I
intended, what happened, what I would do differently. Scores are the
program's, read back from the saves with `render.py <game> <n>`, so the Coup
figures below are the numbers the Victory phase actually saw.

## The result in one line

The US won at the third Coup with 58 — 34 points of Support and 24 in the
force pool — the first of the three games in which the map, not the box,
carried the score.

## The plan, and what it turned into

I started from the two previous post-mortems' verdict: build Support on the
map, get US Bases into pop-2 Provinces early, use Advise every action, and
watch the rivals' numbers rather than my own. For once the plan survived
contact.

- **Card #29, the first action of the game.** Tribesmen unshaded removed the
  VC Bases from all three spaces where I had Irregulars and denied the VC a
  Critical shaded side that would have converted those Irregulars into VC
  Guerrillas. Three of the VC's seven Bases gone on turn one, and the tool the
  rest of the game ran on kept.
- **Card #66, the Bases.** Ambassador Taylor unshaded brought two US Bases
  from Out of Play straight onto the map, into Quang Tri-Thua Thien and Binh
  Dinh. Out-of-Play pieces score nothing, so this was free, and it is the thing
  both earlier games said never happened. Those two Provinces produced 8 of my
  34 Support points and were the only spaces where Train could place ARVN
  cubes outside a City.
- **Advise as the weapon, again.** Every enemy piece I removed by operation
  came from Advise or from an Assault that Advise had set up. It cost no
  Resources, no US piece beyond flipping one Irregular Active, and it broke NVA
  Control four times.
- **ARVN's Resources as my budget.** Thirteen levels of pacification for 47 of
  ARVN's Resources, which the bot would otherwise have spent on four-space
  Sweeps.

What the plan did not anticipate was the bots' pivotal events. Three of the
four fired, and each one rewrote the board.

## Why the win came at the third Coup and not the second

This is the finding worth carrying forward. The Victory check read these
numbers:

| Coup | US | ARVN | VC | NVA | Outcome |
| --- | --- | --- | --- | --- | --- |
| 1 (#126 Young Turks) | 37 | 44 | 21 | 12 | nobody above 0 |
| 2 (#127 Nguyen Cao Ky) | **50** | 40 | 26 | 13 | nobody above 0 |
| 3 (#125 Nguyen Khanh) | **58** | 31 | 18 | 11 | **US wins by 8** |

At Coup 2 the US stood at exactly 50 against a threshold of 50. The rule is
score **above** 0, so 50 is a draw with the threshold and not a win. **One
point anywhere in the fifteen cards before it would have ended the game a
full campaign early**, and instead the game ran on through Easter Offensive,
Vietnamization and Tet Offensive.

I went looking for where that point was. The honest answer is that it was
hard to find, and that is itself the lesson:

- The Coup 1 Commitment phase allows **two** Bases to move and I moved one
  (Saigon's, +1). Pleiku-Darlac's Base sat in an Active Opposition pop-1
  Province I never pacified and never assaulted from; in the box it is worth a
  point. But moving two pieces instead of one triggers the withdrawal penalty
  — one VC shift of a population toward Active Opposition — so the net is
  between +1 and 0 depending on which space the VC picks. Not free.
- On card #9 I chose the event (+3, to exactly 50) over a Train-pacify that
  the Resource/Econ gate had cut to one level (+2, to 49). That call was
  right by a point and still landed me on the line.
- Card #73 Great Society took 3 points out of my Available box on a card where
  I was third in order and never acted.

So the point was not lying around; it had to be manufactured earlier, and the
way to manufacture it was **turn order**. Sixteen of the thirty-two cards
passed without a US action, and three of those were cards where I was eligible
but squeezed out at third or fourth in the order. My one pass of the game
(#55 Trucks) bought a guaranteed first eligibility on Claymores and worked
exactly as intended. I should have made two or three more of them.

## What went right

- **The opening three actions.** Tribesmen (three VC Bases), Brinks Hotel
  (Control of two pop-2 Highlands for nothing but two flipped Irregulars) and
  Ambassador Taylor (two free Bases) built the whole engine in the first six
  cards, and the NVA obligingly played Brinks Hotel's unshaded side for me
  because its marking pointed that way.
- **Linebacker II, played for the denial.** I spent the US pivotal not on its
  own text but to erase #105 Rural Pressure, a VC Critical card aimed at
  three of my Police-held Support spaces, worth about 4 points. It also cost
  the NVA two Bases and two cards of eligibility. A pivotal replaces the
  current card outright, so half its value is what you delete.
- **Honolulu Conference, card #64.** Aid +10, Patronage −5 and a full
  Support-phase pacification in one action: ARVN 43 → 38 and US 52 → 56, on
  the exact card where ARVN's Govern had just taken 8 points off me.
- **Reading the Tru'ng markings.** The bots' Critical markings predicted their
  events every time, and twice I left an event I wanted to a bot marked for the
  same side rather than spend my own action on it.
- **Recovering from the interface.** Three container losses and one mid-action
  crash cost nothing, because the patched build saves after every action.

## What went wrong, in order of cost

1. **Sitting on exactly 50 at Coup 2.** Covered above. A campaign of extra
   play, and every bot pivotal, came out of that one point.
2. **Three actions damaged or lost to chained sends.** On card #109 a "2"
   chained into a Special Activity menu that had dropped Advise opened Air
   Strike instead of Air Lift; the abort that followed cleared only the
   Special Activity, and further chained answers then fired an Assault I had
   not planned. On card #108 a "2" chained into a Limited Op's final Train
   menu hit "Finished" instead of "Transfer patronage", and the action did
   nothing at all. That is the same mistake that decided TestGame1 and cost
   TestGame2 an action, now three games running. The rule I wrote and then
   broke: one send per prompt, print the menu first. After #108 I held to it
   and made no further errors.
3. **Building Support where ARVN had cubes.** Hue, Quang Tri and Binh Dinh
   were all pacified to Active Support with ARVN Troops and Police standing in
   them, and ARVN's Govern took eight points back in two consecutive cards.
   Govern needs ARVN cubes in the space; Support held by US pieces alone, or
   in Saigon, is immune. I knew this from the last post-mortem and built the
   engine that way anyway, because ARVN cubes were also what made the spaces
   defensible.
4. **Under-rating the Trail.** I declined Trucks unshaded (Trail 4 → 2) on
   card #55, calling its effect transient. At Trail 4 the NVA Marches free
   outside South Vietnam, which is how a stack in the Parrot's Beak crossed the
   map into Quang Tin in a single March two cards later. Kevin had to tell me
   the rule. The pass I made instead was still correct, but I priced the
   alternative wrongly.
5. **Never testing the Patronage transfer.** Offered three times across the
   game, executed none — twice lost to the chained sends above, once declined
   for a 12-point pacification. Three games, three failures to learn what it
   does.
6. **A near-miss on the Saigon Base.** The VC's Nguyen Huu Tho put a Base and
   a Guerrilla into Saigon, and I could not Assault it because an Underground
   Guerrilla shields a Base. I Swept to Activate the Guerrilla, then never got
   another action in Saigon before the Coup. Had the VC rolled better on its
   Attacks, twelve points of Active Support sat behind that Base all game.

## The decisive stretch

From card #123 to card #72, the last nine cards of the campaign, the US went
from 60 to 58 while surviving the worst of the game. Easter Offensive took
five Controls, two US Troops and put the NVA on 17 of 18. Two cards later a
Train in Binh Dinh with six ARVN cubes and Advise removals in Quang Tri and
Pleiku put me on 60 and the NVA back to 14. ARVN's Patrol-and-Govern chain
then took 8 points in two cards, and Honolulu Conference took most of them
back while cutting ARVN by 5. The final card before the Coup, in Monsoon,
added a level in Binh Dinh and an Advise that broke NVA Control in Pleiku:
58 against 11, 18 and 31.

The margin of 8 flattered the position. When Kevin continued the game past the
win, the VC's Tet Offensive fired on the very next card — nine free Terrors, a
Base and two Guerrillas into each of two Cities, free Attacks everywhere — and
took the US from 58 to 46 and the VC from 26 to 34 in one turn. Under the
standard rule, where only the final Coup counts, that position was not safe at
all. A human-win-any-Coup game rewards getting over the line early; it does
not measure whether you could have held.

## What the next player should do differently

- **Count the margin, not the score, from the middle of each campaign.**
  Victory needs strictly more than the threshold. Know the exact number you
  need two cards before the Coup card can appear, and spend an action buying
  it. A point you can see is worth more than a plan you like.
- **Pass more often, and always for turn order.** Sixteen idle cards is too
  many. A pass that guarantees first eligibility on the next card converts a
  card you would lose into a full action; the one I made won its exchange
  outright.
- **Pacify where ARVN has no cubes, and put your own Troops there.** Govern is
  the single largest leak in the US score and it reaches only spaces with ARVN
  cubes outside Saigon. Draining ARVN's Available box helps but does not close
  it: the bot reached Govern through its Patrol branch with the Available check
  already failed.
- **Take Out-of-Play pieces onto the map whenever an event offers them.** They
  score nothing in that box, so they are free; Available pieces already score,
  so moving those out costs a point each.
- **Use the Coup Commitment casualty placement.** Troop casualties that are not
  rotated Out of Play are placed on the map by you, for free, anywhere
  COIN-controlled. Two Troops into a Passive Support City with Police makes it
  a strict-test pacification target for the next Coup.
- **Kill the VC's Agitate engine early.** Tax shifts a space one level toward
  Support, which looks like a gift, and banks 2 into the Agitate Total, which
  is spent in the Coup Support phase after the Victory check where nothing can
  answer it. The VC banked 18 that way and cashed 8 of it the moment the game
  continued.
- **Expect every bot pivotal in a long game.** The roll target is the number of
  cards in the RVN Leader box, so each Coup makes all four likelier. Easter
  Offensive, Vietnamization and Tet Offensive all fired here. Plan the third
  campaign as if they will.
- **One send per prompt.** Three games, three actions lost to the same habit.

## Numbers for the record

Sixteen US actions across thirty-two cards: 7 Events (one of them the US
pivotal), 6 Op + Special Activity, 2 Limited Ops (one wasted), 1 Pass. Sixteen
cards with no US action: eleven Ineligible, five eligible but squeezed out by
turn order.

Pacification: 13 levels in 6 spaces for 47 ARVN Resources; Total Support 15 →
34. Enemy pieces removed by US action: 3 VC Bases and 2 NVA Bases, 12 NVA
Troops, 6 VC Guerrillas, 5 NVA Guerrillas — roughly 28 pieces, of which every
one came from an event, an Advise, or an Assault.

US losses: 3 Troops sent Out of Play by Great Society, 8 Troops and 3
Irregulars to Casualties over the game, no Base ever lost. Four US Bases were
on the map at the end (Saigon's having been banked at Coup 1 for a point).
Coup decisions: three Support phases (5 levels, 2 levels, none available),
three Commitment phases (1 Base to Available; 2 casualties placed; 4
casualties placed). Container losses: 3, plus one mid-action crash that rolled
a half-entered Patrol back cleanly.
