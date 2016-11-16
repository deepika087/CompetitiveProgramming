"""
cannot handle large inputs
"""
import copy
class Solution(object):
    def checkIfAnagram(self, s, pCounter, pSize):
        for item in s:
            item = ord(item) - ord('a')
            if(pCounter[item] > 0):
                pCounter[item] = pCounter[item] - 1
                pSize = pSize - 1
            else:
                return False
        return pSize == 0
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pCounter=[0 for _ in range(27)]
        for i in p:
            pCounter[ord(i)-ord('a')] = pCounter[ord(i)-ord('a')] + 1
        result = []
        i=0
        while ( i < len(s)):
            #print " Start for i = ", i
            if ( pCounter[ ord(s[i]) - ord('a')] > 0): #Found one of the occurence
                if (self.checkIfAnagram(s[i:i+len(p)], copy.copy(pCounter), len(p))):
                    result.append(i)
            i = i + 1

        return result


s=Solution()
print s.findAnagrams("baa", "aa")
print s.findAnagrams("cbaebabacd", "abc")
print s.findAnagrams("abab", "ab")