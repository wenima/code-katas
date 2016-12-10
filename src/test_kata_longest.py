"""Tests for kata longest from www.codewars.com"""
import pytest

# TESTS = [
#     ([1, 2, 3, 4, 5], [1, 6, 7, 8, 9], True),
#     ([9, 8, 7], [8, 1, 3], True),
#     ([10910249, 2309234, 23, 2353, 2309491], [1, 2, 3, 4], False),
# ]


# @pytest.mark.parametrize('s, t, TESTS')
def test_kata_longest():
    """Test if the function returns True in case 2 lists of ints have at least one element in common"""
    from kata_longest import longest
    result = 'aehrsty'
    assert longest("aretheyhere", "yestheyarehere") == result