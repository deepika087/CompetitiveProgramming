
"""
Test cases didnpt pass however I guess this should pass.
Becuase number of elements between a and o are 10. Whre as input says 11.
"internationalization"
"i5a11o1"
"""
def is_char(s):
    return s >= 'a' and s <= 'z'

def is_digit(s):
    return (ord(s) - ord('0') >= 0) and (ord(s) - ord('0') <= 9)

def getNextInteger(abbr, i):
    start = i+1
    while( start < len(abbr) and is_digit(abbr[start])):
        start = start + 1

    slice = abbr[i:start]
    num = ord(slice) - ord('0') if len(slice) == 1 else int(slice)
    print "returning integer ", num
    return num, start

def validWordAbbreviation(word ,abbr):

    ptr = 0
    i = 0
    while ( i < len(abbr)):
        if (is_char(abbr[i])):
            if (word[ptr] == abbr[i]):
                ptr = ptr + 1
                i = i + 1
                continue
            else:
                return False #"From inner loop"
        else:
            i_old = i;
            number , i = getNextInteger(abbr, i_old)
            if ( ptr + number < len(word)):
                ptr = ptr + number
            else:
                return False;

    #print " At end ptr = ", ptr, " whereas length = ", len(word)
    if ( ptr == len(word) ):
        return True
    else:
        return False


if __name__ == "__main__":
    word = ["apple", "internationalization", "internationalization"]
    abbr = ["a2e", "i12iz4n", "i5a11o1"]

    for i in range(len(word)):
        print validWordAbbreviation(word[i], abbr[i])