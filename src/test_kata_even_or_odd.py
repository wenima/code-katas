"""Tests for kata even_or_odd from www.codewars.com"""
import pytest

def test_kata_fake_bin_2():
    """Test if result is 'Even' for even numbers."""
    from kata_even_or_odd import even_or_odd
    assert even_or_odd(2) == 'Even'

def test_kata_fake_bin_3():
        """Test if result is 'Odd' for odd numbers."""
        from kata_even_or_odd import even_or_odd
        assert even_or_odd(3) == 'Odd'
