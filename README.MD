#Summary

* the module parenthetics.py is a weekend assignment / Interview challenge as
it seems to make for a good practice to do on a whiteboard.

## Descripton of Kata: Write a quick Python function incorporating one of the data structures learned that takes an unicode string as input and returns 3 possible values:
* Return 1 if the string is “open” (there are open parens that are not closed)
* Return 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
* Return -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)

# General comments

* I whiteboarded the solution to split the list in the middle and then work out the matching parantheses inside out but ran into issues and went for a less elegant solution. I'd like to revisit my original approach as I think it would be faster and more elegant.

# Test coverage:

* via pytest:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| dbl_linked_list.py       |  30   |  0   | 100%  |         |
| parenthetics.py          |  18   |  0   | 100%  |         |
| test_paranthetics.py     |   6   |  0   | 100%  |         |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  54   |  6   | 100%  |         |
