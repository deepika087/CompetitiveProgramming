"""
6. ZigZag Conversion
"""
def convert(s, numRows):
    result = []
    if (numRows == 1):
        return s
    startPoint = 0
    toggle = True
    seed1 = 2 * numRows - 2;
    seed2 = 0
    while(startPoint <= numRows - 1):
        saveStartPoint = startPoint;
        result.append(startPoint)
        last_used = 2
        while(startPoint < len(s)):
            if (toggle == False):
                startPoint = startPoint +  seed1
            else:
                if (last_used == 1):
                    startPoint = startPoint +  seed2
                    last_used = 2;
                else:
                    startPoint = startPoint + seed1
                    last_used = 1
            result.append(startPoint) # always seed1 if toggle seed2 = 0
            if (seed2 == 0 or seed1 == 0):
                toggle = False # Don't flip

        startPoint = saveStartPoint + 1
        seed2 = seed2 + 2
        seed1 = seed1 - 2
        toggle = True;

        if (seed1 == 0):
            seed1 = seed2;
            toggle = True

    result = filter(lambda x: x < len(s), result)
    sb = []
    for i in result:
        sb.append(s[i])
    return ''.join(sb)
    #return result

if __name__=="__main__":
    n = 1
    stringS = "A"
    #print len(str)
    print (convert(stringS, n))