"""Tests for kata power_of_two from www.codewars.com"""
import pytest


def test_kata_power_of_two_True():
    """Test if the given integer is a power of 2 so any number that is 2^n"""
    from kata_power_of_two import power_of_two
    assert power_of_two(1024) == True

def test_kata_power_of_two_False():
    """Test if the given integer is NOT a power of 2 so any number that is 2^n"""
    from kata_power_of_two import power_of_two
    assert power_of_two(885) == False

#since Codewars didn't check for 0 as input

def test_kata_power_of_two_0():
    """Test if 0 passes as power of 2"""
    from kata_power_of_two import power_of_two
    assert power_of_two(0) == False
