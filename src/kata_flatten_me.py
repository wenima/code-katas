def flatten_me(lst):
    """flattens a given list which may or may not contain another list"""
    new_arr = []
    for n in lst:
        try: #ducktyping
            for x in n: #trying to see if the element of the list is an iterable
                new_arr.append(x)
        except TypeError:
            new_arr.append(n)
    return new_arr
