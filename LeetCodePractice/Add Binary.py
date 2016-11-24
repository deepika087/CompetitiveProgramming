"""
67. Add Binary

294 / 294 test cases passed.
Status: Accepted
Runtime: 49 ms
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #print " Received a = ", a, " b =  ",b
        if(len(a) < len(b)):
            diff = len(b) - len(a)
            diff = '0'*diff
            a = diff + a
            return self.addBinary(a, b)
        elif (len(b) < len(a)):
            return self.addBinary(b, a)
        else:
            carry = 0
            result=[0 for i in range(len(a))]
            while(i >= 0):
                part1=a[i]
                part2=b[i]

                if (part1 == '0' and part2 == '0'):
                    result[i] = 0 + carry
                    carry = 0 #Carry will definetely get nullified here
                elif( part1 == '1' and part2 == '1' ):
                    if (carry == 0):
                        result[i] = 0
                        carry = 1
                    else:
                        result[i] = 1
                        carry = 1
                else:
                    if (carry == 0): #1/0 or 0/1
                        result[i] = 1
                        carry = 0
                    else:
                        result[i] = 0
                        carry = 1
                i = i - 1
        #print carry, result
        if (carry == 1):
            return str(carry) + "".join([str(i) for i in result])
        else:
            return "".join([str(i) for i in result])
s=Solution()
print s.addBinary("11", "1")
print s.addBinary("10101", "11")