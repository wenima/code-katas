"""Tests for series function."""
import pytest


TEST_STRINGS = [
    ("Robin Singh", ["Robin", "Singh"]),
    ("CodeWars", ["CodeWars"]),
    ("I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]),
    ("1 2 3", ["1", "2", "3"]),
    ("", [""]),
]


# def test_dict_keys(:
#     """Test whether dictionary contains all biograms as keys."""
#     from trigrams import make_dict
#     result = True
#     dict_ex = make_dict(test_biograms
#     for n in test_biograms:
#         if n not in dict_ex:
#             result = False
#             break
#     assert result

@pytest.mark.parametrize('s, result', TEST_STRINGS)
def test_string_to_array(s, result):
    """Test if string_to_array outputs a list from an input string"""
    from kata_string_to_array import string_to_array
    assert string_to_array(s == result)
