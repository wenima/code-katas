"""Implementation of a solution to the coding challenge posted
https://www.codewars.com/kata/sort-deck-of-cards/python.

The following is assumed:

Spades --> 3
Hearts --> 2
Diamonds --> 1
Clubs --> 0

(T)en     --> 10
(J)ack    --> 11
(Q)ueen   --> 12
(K)ing    --> 13
(A)ce     -->  1
"""

SUITS = {
    's': ('Spades', 3),
    'h': ('Hearts', 2),
    'd': ('Diamonds', 1),
    'c': ('Clubs', 0)
}

RANKS = {
    'A': ('Ace', 1),
    '2': ('Two', 2),
    '3': ('Three', 3),
    '4': ('Four', 4),
    '5': ('Five', 5),
    '6': ('Six', 6),
    '7': ('Seven', 7),
    '8': ('Eight', 8),
    '9': ('Nine', 9),
    'T': ('Ten', 10),
    'J': ('Jack', 11),
    'Q': ('Queen', 12),
    'K': ('King', 13)
}

class Card(object):
    """Object to represent a standard playing card."""

    def __init__(self, rank='2', suit='c'):
        self.rank = rank
        self.suit = suit
        self.value = RANKS[self.rank][1]

    def __lt__(self, other):
        return ((self.value < other.value))

class Deck(object):
    """Object to represent a deck of cards, not necessarily a full 52-card deck."""

    def __init__(self, iterable=None):
        """Initialize a Deck."""
        self._heap = []
        self._size = 0
        try:
            for rank in iterable:
                self.push(Card(rank))
        except:
            raise TypeError("Not an iterable")

    def push(self, value):
        self._heap.append(value)
        self._size += 1

    def sort_cards(self):
        return [c.rank for c in sorted(self._heap)]
