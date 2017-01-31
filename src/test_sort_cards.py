"""Test dbl_linked_list data structures."""

import pytest

# CMP_CARDS = [
#     ('A', '3', True),
#     ('K', 'Q', False),
#     ('9', 'J', True),
#     ('T', 'T', True),
# ]

CARDS = [
    (['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'], ['A', '2', '3', '4', '5','6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    (['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K', 'K', '6'], ['A', '2', '3', '4','5', '6', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'K']),
    ]


# @pytest.mark.parametrize('c1, c2, result', CMP_CARDS)
# def test_create_new_cards(c1, c2, result):
#     from sort_cards import Card
#     """Test creation of a new playing card."""
#     card1 = Card(c1)
#     card2 = Card(c2)
#     result = True
#     assert c1.__lt__(c2) is True

@pytest.mark.parametrize('cards, result', CARDS)
def test_sort_cards(cards, result):
    from sort_cards import Card, Deck
    """Test output of sort_cards using classes."""
    d = Deck(cards)
    assert d.sort_cards() == result


@pytest.mark.parametrize('cards, result', CARDS)
def test_sort_cards_using_pq(cards, result):
    from sort_cards_pq import Card, Deck, sort_cards
    """Test output of sort_cards using a PriorityQueue."""
    assert sort_cards(cards) == result
