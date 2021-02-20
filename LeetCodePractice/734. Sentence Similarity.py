__author__ = 'deepika'

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        if len(words1) == len(words2) and len(words1) == 0:
            return True
        if ([words1[0], words2[0]] in pairs or words1[0] == words2[0] or [words2[0], words1[0]] in pairs):
            return self.areSentencesSimilar(words1[1:], words2[1:], pairs)
        else:
            return False

s=Solution()
assert s.areSentencesSimilar(["great"], ["great"], []) == True
assert s.areSentencesSimilar(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["acting","drama"], ["skills","talent"]]) == True

assert s.areSentencesSimilar(["great","acting","skills"], ["fine","painting","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]) == False