__author__ = 'deepika'


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result = set()
        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                if word2 in word1:
                    result.add(word2)
        return result

s=Solution()
print(s.stringMatching(words = ["mass","as","hero","superhero"]))
print(s.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))