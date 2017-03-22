__author__ = 'deepika'
"""
520 Detect Capital

550 / 550 test cases passed.
Status: Accepted
Submitted: 0 minutes ago
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if (len(word) == 0):
            return False
        capital = list(filter(lambda x: x.isupper(),word ))
        #print " len(capital)", len(capital)
        if (len(capital) == len(word)):
            return True
        if(len(capital) == 1 and word[0].isupper()):
            return True
        if (len(capital) ==0):
            return True
        return False


s=Solution()
print s.detectCapitalUse("USA")
print s.detectCapitalUse("FlaG")
print s.detectCapitalUse("Leetcode") #Expected true