#Summary

the repository code-katas includes the following completed coding challenges from the CodeWars Python challenges

## Description:
You were given a string of integer temperature values. Create a function ```lowest_temp(t)``` and return the lowest value or ```None/null/Nothing``` if the string is empty.

# Difficulty: kyu7

# Link: https://www.codewars.com/kata/temperature-analysis-i/train/python

# General comments

* The first solution to just pass the kata should have been way shorter but I started specing out the program with the stretch goal in mind and allowing for also a proper ranked suit to be passed in.

# Example test:
```
Test.assert_equals(lowest_temp(''), None)
Test.assert_equals(lowest_temp('-1 50 -4 20 22 -7 0 10 -8'), -8)
```

# Test coverage:

* via pytest:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| sort_cards.py            |  23   |  0   | 100%  |         |
| sort_cards_pq.py         |  26   |  0   | 100%  |         |
| test_sort_cards.py       |  17   |  0   | 100%  |         |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  66   |  0   | 100%  |         |
