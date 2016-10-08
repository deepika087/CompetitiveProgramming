
"""
95 test cases passed. Absolutely correct
"""

def longestPalindrome(s):

    charcount = dict()
    n = 0
    for i in s:
        if (charcount.get(i, -1) == -1):
            charcount[i] = 1
            n = 1
        else:
            charcount[i]  = charcount[i] + 1
            n = n + 1
    print charcount
    result = 0
    taken = False
    someExtraCanBeAdded = False
    #print "Total number of element = ", n

    if (len(charcount.items()) == 1):
        return charcount.items()[0][1]
    for (k, v) in charcount.items():

         if (v % 2 ==0 ):
            result = result + v
         elif ( v %2 != 0 and v > 1):
            result = result + (v - 1)
            someExtraCanBeAdded = True # It means some character was ignored to keep it palin added for test case ababababa.
         elif ( v%2 != 0 and v == 1 and not taken):
            taken = True
            result = result + 1

    if ( not taken and someExtraCanBeAdded): #Added for test case ababababa
        result = result + 1
    return result


if __name__ == '__main__':
    s = ["ccc"]
    s.append("ababababa")
    s.append("abccccdd")
    for i in s:
        print i , "  " , longestPalindrome(i)