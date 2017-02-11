from random import randint, shuffle

def jumble(string):
    jumbled = []
    for w in string.split():
        non_alpha_idx = [idx for idx, c in enumerate(w) if not c.isalpha()]
        if non_alpha_idx:
            if not non_alpha_idx[0] == len(w) - 1:
                jumbled.append(w)
                continue
        offset = 1 + len([1 for c in w if not c.isalpha()])
        if len(w) - offset < 3:
            jumbled.append(w)
            continue
        inner = [c for c in w[1: - offset]]
        while True:
            if len(inner) < 2:
                break
            shuffle(inner)
            if inner == [c for c in w[1: - offset]]:
                shuffle(inner)
            else:
                break
        jumbled.append(''.join(w[0] + ''.join(inner) + w[-offset:]))
