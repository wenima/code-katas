"""Tests for kata flatten_me from www.codewars.com"""
import pytest

TESTS = [
    ([1, [2, 3], 4], [1, 2, 3, 4]),
    ([['a', 'b'], 'c', ['d']], ['a', 'b', 'c', 'd']),
    ([1, [2, 3], 4], [1, 2, 3, 4]),
    ([['a', 'b'], 'c', ['d']], ['a', 'b', 'c', 'd']),
    (['!', '?'], ['!', '?']),
    ([[True, False], ['!'], ['?'], [71, '@']], [True, False, '!', '?', 71, '@']),
]


@pytest.mark.parametrize('s, result', TESTS)
def test_kata_flatten_me(s, result):
    """Test if flatten_me outputs a list from an input list which may or may
    not holds lists"""
    from kata_flatten_me import flatten_me
    assert flatten_me(s) == result
