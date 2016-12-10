def longest(s1, s2):
    alphabet = alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    uniq1 = [c for c in s1 if c in alphabet]
    uniq1 = uniq1 + [c for c in s2 if c in alphabet]
    uniq_c = set(uniq1)
    longest = sorted(uniq_c)
    return ''.join(longest)
