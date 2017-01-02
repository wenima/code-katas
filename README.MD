#Summary

this repository contains 2 modules:
* sort_cards.py which contains the code to pass the original [weekend assignment](https://codefellows.github.io/sea-python-401d5/assignments/kata_sort_cards.html) and with the stretchgoal in mind
* sort_cards_pq.py which contains the code for achieving the stretch goal as described in the link above.

## Description:
Write a function sort_cards() that sorts a shuffled list of cards, so that any given list of cards is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards looks like this:

```
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
```

# General comments

* The first solution to just pass the kata should have been way shorter but I started specing out the program with the stretch goal in mind and allowing for also a proper ranked suit to be passed in.

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
