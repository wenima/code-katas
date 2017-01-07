def longest_palindrome (s):
    i = 1
    longest_pali = 0
    for idx, c in enumerate(s, 1):
        has_even = lambda s: s[idx - 1:idx + 1] == s[idx - 1:idx + 1][::-1]
        has_odd = lambda s: s[idx - 1 : idx + 2] == s[idx - 1 : idx + 2][::-1]
        if has_even:
            while True:
                sub_even = s[idx - i:idx + i]
                if not sub_even:
                    break
                if  sub_even == sub_even[::-1]:
                    if len(sub_even) > longest_pali:
                        longest_pali = len(sub_even)
                else:
                    break
                i += 1
                if len(s) == longest_pali:
                    break
        if has_odd:
            while True:
                sub_odd = s[idx - i : idx + i + 1]
                if not sub_odd:
                    break
                if  sub_odd == sub_odd[::-1]:
                    if len(sub_odd) > longest_pali:
                        longest_pali = len(sub_odd)
                else:
                    break
                i += 1
                if len(s) == longest_pali:
                    break
    return 1 if len(s) == 1 else longest_pali
