__author__ = 'deepika'


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if (len(s) == 1):
            return 1
        i = 0
        count = 1 #For all single integer case

        while i < len(s) - 1:
            main_part = s[i:i+2]
            if main_part >= '10' and  main_part <= '26':
                print(main_part)
                count += self.numDecodings(s[0:i]) + 1 + self.numDecodings(s[i+2:])
            i = i + 1
        return count

s=Solution()
#print s.numDecodings("12")
print s.numDecodings("226")
#assert s.numDecodings("12") == 2
#assert s.numDecodings("226") == 3

