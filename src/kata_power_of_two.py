def power_of_two(n):
    """Take an integer n and return True if n is a power of 2, False if not"""
    return True if str(bin(n)).count('1') == 1 else False
