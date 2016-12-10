"""Tests for kata digitize from www.codewars.com"""
import pytest

def test_kata_digitize():
    """Test if return value is a list containing the input number as digits in
    reverse order."""
    from kata_digitize import digitize
    assert digitize(348597) == [7,9,5,8,4,3]
