"""Tests for series function."""
import pytest


TEST_STRINGS = [
    ("Robin Singh", ["Robin", "Singh"]),
    ("CodeWars", ["CodeWars"]),
    ("I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]),
    ("1 2 3", ["1", "2", "3"]),
    ("", [""]),
]


@pytest.mark.parametrize('s, result', TEST_STRINGS)
def test_string_to_array(s, result):
    """Test if string_to_array outputs a list from an input string"""
    from kata_string_to_array import string_to_array
    assert string_to_array(s) == result
