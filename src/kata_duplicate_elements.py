def duplicate_elements(m, n):
    for i in m:
        if i in n:
            return True
    else:
        return False
