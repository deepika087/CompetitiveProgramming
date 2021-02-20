__author__ = 'deepika'

import sys
"""
My first approach was to handle 0 to k chars and then remove from left and take from right.
but that will not work cz assume baabe. k = 4 from baab result is aa but adding e doesn't mean
have can add e as part of the substring because abe won't be valid.

Second thought was to keep end marker. check if isVowel(s[i]) and i == end + 1
bbut then you have totally ignored the fact that e indeed was a vowel.

"""

class Solution(object):
    def isVowel(self, character):
        return  character in ['a', 'e', 'i', 'o', 'u']

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        numOfVowels = 0
        maxSeen = -sys.maxint

        for i in range(0, k):
            if self.isVowel(s[i]):
                numOfVowels += 1

        maxSeen = numOfVowels

        for i in range(k, len(s)):
            if self.isVowel(s[i - k]):
                if (numOfVowels > 0):
                    numOfVowels -= 1
            if self.isVowel(s[i]):
                numOfVowels += 1
            maxSeen = max(maxSeen, numOfVowels)

        return maxSeen

s=Solution()
print(s.maxVowels(s = "abciiidef", k = 3)) #3
print(s.maxVowels(s = "aeiou", k = 2)) #2
print(s.maxVowels(s = "leetcode", k = 3)) #2
print(s.maxVowels(s = "rhythms", k = 4)) #0
print(s.maxVowels(s = "tryhard", k = 4)) #1
print(s.maxVowels(s = "weallloveyou", k = 7))