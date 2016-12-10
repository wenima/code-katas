"""Tests for kata fake_bin."""
import pytest


TESTS = [
    # [expected, input]
    ["45385593107843568", "01011110001100111"],
    ["509321967506747", "101000111101101"],
    ["366058562030849490134388085", "011011110000101010000011011"],
    ["15889923", "01111100"],
    ["800857237867", "100111001111"],
]


@pytest.mark.parametrize('s, result', TESTS)
def test_kata_fake_bin(s, result):
    """Test if string returned is correctly replaced where each n < 5 is
    replaced with 0 and each n >= is replaced with 1 """
    from kata_fake_bin import fake_bin
    assert fake_bin(result)
