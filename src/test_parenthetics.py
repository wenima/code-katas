"""Test the Paranthetics Code Kata assignemnt.

Following statements are true:

A string of parantheses is broken if it a close parantheses ')' is encountered
before it's opened and should return -1.

A string of parantheses is deemed open if one or more open parantheses ('(')
are not matched by a closing parantheses and should return 1.

Finally, a string of parantheses is considered balanced if all parantheses are
matched."""


import pytest

PS= [')))(((']

TEST_PS = [
    (')))(((', -1),
    ('((()))(', 1),
    ('((()))', 0),
    ('()()()()()()', 0),
    ('())))(((()', -1),
    ('()()())()()()', -1),
    ('(()(()(', 1),
    ('(((((())))', 1)
]


@pytest.mark.parametrize('s, result', TEST_PS)
def test_if_string_is_broken(s, result):
    from parenthetics import parse_parentheses
    assert parse_parentheses(s) == result
