def series_sum(n):
    """Sum up to the nth parameter of the following series:
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

###Rules:

Return result as string and rounded to 2  decimal places.
If the given value is 0 then it should return 0.00.
Only handles natural numbers."""
    return "{0:0.2f}".format(sum([1 / (i * 3 - 2) for i in range(1, n+1)]))
