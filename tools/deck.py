#!/usr/bin/env python3
"""deck.py - lazy, unpredictable event-card draws for Fire in the Lake.

There is no shuffled deck anywhere. Each draw is decided at request time,
uniformly at random (os-level CSPRNG via `secrets`) from the cards that can
legally be next given everything drawn so far. That is statistically the
same as drawing from a physically shuffled deck, and there is nothing on
disk or in memory that could reveal a future card.

Full 1964-1972 scenario deck (rules 2.1):
  six piles of 13 cards, stacked 1964, 1964, 1965, 1965, 1968, 1968.
  Each pile: 12 event cards of its period (a random 12-subset of that
  period's cards not used by an earlier pile), plus 1 Coup! card (#125-130,
  each used once, assigned to piles at random), shuffled together.
  Pivotal events (#121-124) are never in the deck.

The lazy equivalent: for draw number k (0-based), the pile is k // 13. The
candidates are the period's cards not yet drawn (if fewer than 12 events
have been drawn in this pile) plus one unused Coup card (if the pile's Coup
has not been drawn yet). Pick one uniformly. When the Coup slot is picked,
choose uniformly among the Coup cards not yet seen.

Usage:
  deck.py next <seen cards...>      print the next card number
  deck.py selftest                  simulate many decks and check every rule
  deck.py explain <seen cards...>   show pile/position and candidate counts
                                    (never the future: counts only)
"""
import json
import os
import secrets
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_PATH = os.path.join(ROOT, "cards.json")

CARDS_PER_PILE = 13
EVENTS_PER_PILE = 12
COUP_CARDS = [125, 126, 127, 128, 129, 130]
PIVOTAL_CARDS = [121, 122, 123, 124]
FULL_PILES = ["1964", "1964", "1965", "1965", "1968", "1968"]

_rng = secrets.SystemRandom()


def load_periods(cards_path=CARDS_PATH):
    """{card number: '1964'|'1965'|'1968'} for the 120 event cards."""
    with open(cards_path, encoding="utf-8") as f:
        cards = json.load(f)
    periods = {}
    missing = []
    for n in range(1, 121):
        c = cards.get(str(n))
        p = c.get("period") if c else None
        if p in ("1964", "1965", "1968"):
            periods[n] = p
        else:
            missing.append(n)
    if missing:
        raise SystemExit(
            f"cards.json has no period marking for {len(missing)} event cards "
            f"(e.g. {missing[:8]}). Run tools/apply_periods.py first.")
    return periods


class Deck:
    def __init__(self, periods, piles=FULL_PILES):
        self.periods = periods
        self.piles = piles
        self.by_period = {}
        for n, p in periods.items():
            self.by_period.setdefault(p, set()).add(n)
        for p in set(piles):
            need = piles.count(p) * EVENTS_PER_PILE
            have = len(self.by_period.get(p, ()))
            if have < need:
                raise SystemExit(f"period {p} has {have} cards but the deck needs {need}")

    def validate_seen(self, seen):
        if len(seen) != len(set(seen)):
            raise ValueError("duplicate card in the seen list")
        for k, c in enumerate(seen):
            pile = k // CARDS_PER_PILE
            if pile >= len(self.piles):
                raise ValueError("more cards seen than the deck holds")
            if c in COUP_CARDS:
                continue
            if c in PIVOTAL_CARDS:
                raise ValueError(f"pivotal card #{c} is never drawn from the deck")
            if self.periods.get(c) != self.piles[pile]:
                raise ValueError(f"card #{c} (period {self.periods.get(c)}) cannot be in pile "
                                 f"{pile + 1} ({self.piles[pile]})")
        # per pile: at most 12 events and 1 coup
        for pile in range(len(self.piles)):
            chunk = seen[pile * CARDS_PER_PILE:(pile + 1) * CARDS_PER_PILE]
            coups = [c for c in chunk if c in COUP_CARDS]
            if len(coups) > 1:
                raise ValueError(f"two Coup cards in pile {pile + 1}")
            if len(chunk) - len(coups) > EVENTS_PER_PILE:
                raise ValueError(f"more than {EVENTS_PER_PILE} event cards in pile {pile + 1}")

    def candidates(self, seen):
        """Return (event_candidates, coup_possible) for the next draw."""
        self.validate_seen(seen)
        k = len(seen)
        pile = k // CARDS_PER_PILE
        if pile >= len(self.piles):
            return [], False
        period = self.piles[pile]
        chunk = seen[pile * CARDS_PER_PILE:]
        events_in_pile = sum(1 for c in chunk if c not in COUP_CARDS)
        coup_drawn_in_pile = any(c in COUP_CARDS for c in chunk)
        used = set(seen)
        events = sorted(self.by_period[period] - used) if events_in_pile < EVENTS_PER_PILE else []
        return events, not coup_drawn_in_pile

    def next_card(self, seen):
        events, coup_possible = self.candidates(seen)
        # Each remaining physical card in the pile is equally likely: the 12-e
        # remaining event slots are filled by a uniform subset of `events`, so
        # every event candidate has equal probability, and the Coup card is one
        # more card in the pile.
        slots_left = len(events) and (EVENTS_PER_PILE - self._events_drawn(seen))
        weights = []
        choices = []
        if events:
            # probability mass of "an event comes next" is slots_left / (slots_left + coup)
            for c in events:
                choices.append(c)
                weights.append(slots_left / len(events))
        if coup_possible:
            choices.append("COUP")
            weights.append(1.0)
        if not choices:
            raise ValueError("the deck is exhausted")
        pick = _rng.choices(choices, weights=weights, k=1)[0]
        if pick == "COUP":
            unused = [c for c in COUP_CARDS if c not in seen]
            return _rng.choice(unused)
        return pick

    def _events_drawn(self, seen):
        k = len(seen)
        pile = k // CARDS_PER_PILE
        chunk = seen[pile * CARDS_PER_PILE:]
        return sum(1 for c in chunk if c not in COUP_CARDS)

    def explain(self, seen):
        events, coup_possible = self.candidates(seen)
        k = len(seen)
        pile = k // CARDS_PER_PILE
        pos = k % CARDS_PER_PILE
        return (f"next draw is card {pos + 1} of pile {pile + 1} ({self.piles[pile]}); "
                f"{len(events)} event candidates, Coup {'possible' if coup_possible else 'already drawn'}")


def selftest(periods=None, decks=2000):
    if periods is None:
        # synthetic table so the test does not depend on the real markings
        periods = {n: ("1964" if n <= 40 else "1965" if n <= 80 else "1968") for n in range(1, 121)}
    deck = Deck(periods)
    coup_positions = [0] * CARDS_PER_PILE
    first_cards = {}
    for _ in range(decks):
        seen = []
        while len(seen) < CARDS_PER_PILE * len(FULL_PILES):
            seen.append(deck.next_card(seen))
        # every rule holds for the complete deck
        deck.validate_seen(seen)
        assert sorted(c for c in seen if c in COUP_CARDS) == COUP_CARDS
        for p in range(len(FULL_PILES)):
            chunk = seen[p * CARDS_PER_PILE:(p + 1) * CARDS_PER_PILE]
            assert sum(1 for c in chunk if c in COUP_CARDS) == 1
            assert all(periods[c] == FULL_PILES[p] for c in chunk if c not in COUP_CARDS)
            coup_positions[[i for i, c in enumerate(chunk) if c in COUP_CARDS][0]] += 1
        first_cards[seen[0]] = first_cards.get(seen[0], 0) + 1
    n_positions = decks * len(FULL_PILES)
    print(f"{decks} decks simulated, all constraints held.")
    print("Coup position within pile (should be ~uniform over 13 slots):")
    print("  " + " ".join(f"{c / n_positions:.3f}" for c in coup_positions))
    p64 = sorted(n for n in periods if periods[n] == "1964")
    print(f"First card frequency over the {len(p64)} 1964 cards (expect ~{12 / (13 * len(p64)):.3f} each, "
          f"Coup ~{1 / 13:.3f}):")
    print("  min {:.3f} max {:.3f} coup {:.3f}".format(
        min(first_cards.get(c, 0) / decks for c in p64),
        max(first_cards.get(c, 0) / decks for c in p64),
        sum(first_cards.get(c, 0) for c in COUP_CARDS) / decks))
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    if cmd == "selftest":
        return selftest()
    seen = [int(a) for a in args]
    deck = Deck(load_periods())
    if cmd == "next":
        print(deck.next_card(seen))
        return 0
    if cmd == "explain":
        print(deck.explain(seen))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
