"""Tests for kata multiples from www.codewars.com"""
import pytest

TESTS = [
    (2, 4, 40, [4, 8, 12, 16, 20, 24, 28, 32, 36]),
    (3, 4, 40, [12, 24, 36]),
    (7, 4, 80, [28, 56]),
    (18, 33, 2390, [198, 396, 594, 792, 990, 1188, 1386, 1584, 1782, 1980, 2178, 2376]),
    #(7, 4, 20, []), #had to comment this out as it was throwing an error when passing into the test
]


@pytest.mark.parametrize('s, t, bound, result', TESTS)
def test_kata_multiples(s, t, bound, result):
    """Test if the function returns all mutliples up to the given bound"""
    from kata_multiples import multiples
    assert multiples(s, t, bound) == result

def test_kata_multiples():
    """Test if the function returns all mutliples up to the given bound"""
    from kata_multiples import multiples
    assert multiples(7, 4, 20) == []
