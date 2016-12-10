def digitize(n):
    """takes in a number and returns a list of numbers in reversed order"""
    return [int(x) for x in str(n)[::-1]]
