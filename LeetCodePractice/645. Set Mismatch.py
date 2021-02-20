__author__ = 'deepika'

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.dictionary = {}
        missing, duplicate = None, None
        for i in nums:
            if i in self.dictionary:
                self.dictionary[i] = self.dictionary[i] + 1
