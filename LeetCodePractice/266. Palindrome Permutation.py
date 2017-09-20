__author__ = 'deepika'

"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

26 / 26 test cases passed.
Status: Accepted
Runtime: 32 ms

About 60% better
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = dict()
        for _s in s:
            if _s in dictionary:
                dictionary[_s] = dictionary[_s] + 1
            else:
                dictionary[_s] = 1

        foundOdd = False
        for k, v in dictionary.items():
            if v % 2 == 0:
                continue
            else:
                if foundOdd:
                    return False
                foundOdd = True
                continue
        return True

