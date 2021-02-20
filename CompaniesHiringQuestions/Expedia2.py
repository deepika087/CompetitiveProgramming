__author__ = 'deepika'

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def  volleyball( A,  B):

    if A==0 and B==0:
        return 1
    elif A<0 or B<0:
        return 0
    elif A<25 and B<25:
        return nCr(A+B, A)
    else:
        if A >= 25 or B >= 25:
            if A == 25 and B < 24:
                return nCr(24+B, B)
            elif B == 25 and A < 24:
                return nCr(24+A, A)
            if abs(A - B) == 2:
                return nCr(48, 24) * 2^(B-24)
            else:
                print "Dunno 1"
        else:
            print "dunno2", A, B

print volleyball(3, 25)
print volleyball(24, 17)