__author__ = 'deepika'


class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """

        leftHashMap = {}
        rightHashMap = {}

        left = Counter()
        right = Counter(s)

        for i in range(0, len(s)):
            pass



