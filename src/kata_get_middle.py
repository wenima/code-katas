def getMiddle(s):
    """return the middle char from a string. If string is even, return the middle 2 chars"""
    l = len(s)
    lh = l // 2
    if l % 2 == 0:
        return s[lh - 1 : lh + 1]
    else:
        return s[lh]
