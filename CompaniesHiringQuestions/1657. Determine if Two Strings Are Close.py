__author__ = 'deepika'

import collections

"""
Runtime: 276 ms, faster than 88.84% of Python online submissions for Determine if Two Strings Are Close.
Memory Usage: 15.5 MB, less than 27.59% of Python online submissions for Determine if Two Strings Are Close.
"""
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        dict1 = dict()
        for w in word1:
            if w not in dict1:
                dict1[w] = 0
            dict1[w] += 1

        dict2 = dict()
        for w in word2:
            if w not in dict1:
                return False

            if w not in dict2:
                dict2[w] = 0
            dict2[w] += 1

        commonDict = dict()
        for element in dict1.items():
            if element[1] not in commonDict:
                commonDict[element[1]] = []
            commonDict[element[1]].append(element[0])

        for element in dict2.items():
            if element[1] not in commonDict: #Value doesn't exist
                return False
            commonDict[element[1]].append( element[0] )

        print(commonDict)
        for (k, v) in commonDict.items():
            if len(v) % 2 != 0:
                return False
        return True





s=Solution()
assert s.closeStrings("uau", "ssx") == False
assert s.closeStrings("abbzccca", "babzzczc") == True
assert s.closeStrings(word1 = "cabbba", word2 = "abbccc") == True
assert s.closeStrings("abc", "xyz") == False
assert s.closeStrings("abc", "bca") == True
assert s.closeStrings("a", "aa") == False

