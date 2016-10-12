"""
8. String to Integer (atoi)

Passed all 1047 / 1047 test cases passed.
Runtime: 99 ms
"""

class Solution(object):
    def isCharacter(self, character):
        return (ord(character) >= ord('a') and ord(character) <= 'z') or (ord(character) >= ord('A') and ord(character) <= 'Z')

    def isSpace(self, character):
        return ord(character) == ord(' ')

    def myAtoi(self, str):
        if (len(str) == 0):
            return 0
        if (len(str) == 1 and (str[0] =='+' or str[0] == '-')):
            return 0;
        if ( ('+' in str and '-' in str) or "++" in str or "--" in str ):
            return 0
        if (str.isalpha()):
            return 0
        i = 0
        while(ord(str[i]) in [ord(' '), ord('0')]):
            i = i + 1;
        if (i != 0):
            str = str[i:]
            #print " New str = ", str, " of len = ", len(str)

        i = 0
        while( i < len(str) and not ( self.isCharacter(str[i]) ) and not self.isSpace(str[i]) ):
            i = i + 1;

        if (i != 0):
            str = str[:i]
        else:
            return 0

        if (' ' in str):
            return 0;

        negativeNumber = False
        if ord(str[0]) == ord('-'):
            negativeNumber = True

        result = 0
        power = 0
        for i in range(len(str)-1, -1, -1):
            if (i == 0 and ord(str[0]) in [ord('-'), ord('+')] ):
                continue

            val = ord(str[i]) - ord('0')
            result = result + val * pow(10, power)
            power = power + 1

            if ( not negativeNumber and result > 2147483647):
                return 2147483647
            if (negativeNumber and -result < -2147483648):
                return -2147483648
        return -result if negativeNumber == True else result



if __name__ == "__main__":
    sol = Solution()
    s = " b11228552307"
    print sol.myAtoi(s)
    s = "++c"
    print sol.myAtoi(s)
    s = "123  456"
    print sol.myAtoi(s)
    s = "abc"
    print sol.myAtoi(s)
    s = "-2147483649"
    print sol.myAtoi(s)
    s = "-2147483648"
    print sol.myAtoi(s)
    s = "-2147483647"
    print sol.myAtoi(s)
    s = "2147483648"
    print sol.myAtoi(s)
    s = "   +0 123"
    print sol.myAtoi(s)
    s = "  -0012a42" # start from fixing this
    print sol.myAtoi(s)
    s = "    010"
    print sol.myAtoi(s)
    s = "7865"
    print sol.myAtoi(s)
    s = "+-2"
    print sol.myAtoi(s)
