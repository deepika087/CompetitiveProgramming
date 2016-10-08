
"""
171. Excel Sheet Column Number
"""

def titleToNumber(s):
    mapping = dict()
    for i in range(26):
        mapping[chr(i + 65)] = i + 1

    result = 0
    powerCount = 0
    #print type(s[0])
    #print chr(ord(s[0])), mapping.get(chr(ord(s[0])))
    for i in range(len(s), 0, -1):
        result = result + pow(26, powerCount) * mapping.get(chr(ord(s[i-1])))
        powerCount = powerCount + 1
    return result

if __name__ == "__main__":

    s = "AA"
    print titleToNumber(s)
    s = "AB"
    print titleToNumber(s)

