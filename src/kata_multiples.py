# Python version: return multiples of 2 numbers in a list
def multiples(s1,s2,s3):
    if s2 % s1 == 0:
        return [x for x in range(s2, s3, s2)]
    else:
        (a1, a2) = (s1, s2) #stroring original values in a tuple to avoid aliasing
        while s2:
            s1, s2 = s2, s1 % s2
        lcm = a1 * a2 // s1 #// integer division
    return [x for x in range(lcm, s3, lcm)]
