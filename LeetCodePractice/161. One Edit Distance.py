__author__ = 'deepika'


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (abs(len(s) - len(t)) not in [0, 1]):
            return False
        if (len(s) == 1 and len(t) == 0):
            return True
        if (len(t) == 1 and len(s) == 0):
            return True
        if (len(s) == 0 and len(t) == 0):
            return False
        i, j = 0, 0
        diff = 0
        while(i < len(s) or j < len(t)):
            if ( i >= len(s)):
                j = j + 1
            elif (j >= len(t)):
                i = i + 1
            elif (s[i] == t[j]):
                i = i + 1
                j = j + 1
                continue
            elif (len(s) == len(t)):
                i = i + 1
                j = j + 1

            elif (len(s) > len(t)):
                i = i + 1
            else:
                j = j + 1
            diff = diff + 1
            if (diff > 1):
                return False
        return diff == 1

s=Solution()
print s.isOneEditDistance("a", "ac")
print s.isOneEditDistance("abcd", "abce")
print s.isOneEditDistance("abc", "bc")
print s.isOneEditDistance("abc", "ac")
