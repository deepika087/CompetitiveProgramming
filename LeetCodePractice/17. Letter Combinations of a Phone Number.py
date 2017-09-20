__author__ = 'deepika'

class Solution(object):
    def __init__(self):
        self.mapping = {}
        self.mapping[2] = "abc"
        self.mapping[3] = "def"
        self.mapping[4] = "ghi"
        self.mapping[5] = "jkl"
        self.mapping[6] = "mno"
        self.mapping[7] = "pqrs"
        self.mapping[8] = "tuv"
        self.mapping[9] = "wxyz"

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = list(filter(lambda x: x == 1, digits))
        print digits

s=Solution()

