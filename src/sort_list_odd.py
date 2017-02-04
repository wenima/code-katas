"""Module to solve the kata "Sort the Odd" from codewars.com"""

def sort_array(arr):
    odd = sorted([n for n in arr if n % 2 != 0])
    odd.reverse()
    for idx, n in enumerate(arr):
        if n % 2 != 0:
            arr[idx] = odd.pop()
    return arr
