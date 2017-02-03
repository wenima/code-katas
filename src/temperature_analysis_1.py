"""Module to solve code wars kata:
https://www.codewars.com/kata/temperature-analysis-i/train/python
"""

def lowest_temp(t):
    return min([int(temp) for temp in t.split()]) if t else None
