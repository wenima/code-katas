"""Tests for kata sum_of_nth_series from www.codewars.com"""
import pytest

TESTS = [
    (1, '1.00'),
    (2, '1.25'),
    (5, '1.57'),
    (0, '0.00'),
    (100, '2.58'),
]


@pytest.mark.parametrize('s, result', TESTS)
def test_kata_sum_of_the_nth_series(s, result):
    """Test if the function returns the correct sum of the following series up
    to the nth term.
    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +..."""
    from kata_sum_of_nth_terms import series_sum
    assert series_sum(s) == result
