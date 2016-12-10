def fake_bin(x):
    """Replace each char in input string x with 0 if char < 5 or 1 if char >=5
    """
    bin_str = ['0' if int(c) < 5 else '1' for c in x]
    return "".join(bin_str)
