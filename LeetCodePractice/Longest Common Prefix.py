"""

117 / 117 test cases passed.
Status: Accepted
Runtime: 182 ms
"""
import sys
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 1 and strs is not ""):
            return ''.join(strs)
        elif (len(strs) == 1 and strs is ""):
            return ""
        prefix = dict()
        max_prefix = ""
        max_len = -sys.maxint
        strNum = 0
        for str in strs:
            strNum = strNum + 1

            for i in range(1, len(str) + 1):
                temp = str[0:i]

                if (prefix.get(temp, -1) == -1):
                    prefix[temp] = list()
                    prefix[temp].append(strNum)

                else:
                    if (strNum not in prefix[temp]):
                        prefix[temp].append(strNum)

        for (k,v) in prefix.items():
            if (len(v) == strNum):
                #print " Probable k=",k
                if (len(k) > max_len):
                    max_prefix=k
                    max_len=len(k)

        return max_prefix

s = Solution()
print s.longestCommonPrefix(["a"])
print s.longestCommonPrefix(["abc", "abcdeflmn", "abcdef", "abcd", "abc"])


