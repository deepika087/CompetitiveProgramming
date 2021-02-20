__author__ = 'deepika'


"""
Details
Runtime: 20 ms, faster than 59.57% of Python online submissions for Maximum Nesting Depth of the Parentheses.
Memory Usage: 13.5 MB, less than 45.57% of Python online submissions for Maximum Nesting Depth of the Parentheses.
"""
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        depth = 0
        maxD = -1
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            elif s[i] == ')' and depth > 0:
                depth -= 1
            maxD = max(maxD, depth)
        return maxD
