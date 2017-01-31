"""Implementation of a solution to the coding challenge posted here
https://www.codewars.com/kata/sort-deck-of-cards/python.

This is an implementation of the stretch goal which requires the use of a
PriorityQueue.

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

from binheap import Binheap
from priorityq import PriorityQueue


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
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

class Deck(object):
    """Object to represent a deck of cards, not necessarily a full 52-card deck."""

    def __init__(self, iterable=None):
        """Initialize a Deck."""
        self._heap = PriorityQueue()
        self._heap = self._heap._binheap
        try:
            for rank in iterable:
                self._heap.push(Card(rank))
        except:
            raise TypeError("Not an iterable")

def sort_cards(cards):
    d = Deck(cards)
    sorted_cards = [d._heap.pop().rank for i in range(d._heap._size)]
    return sorted_cards
