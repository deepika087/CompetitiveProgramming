__author__ = 'deepika'

"""
Runtime: 116 ms, faster than 30.05% of Python online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 13.2 MB, less than 55.16% of Python online submissions for Remove All Adjacent Duplicates In String.
"""

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """


        if len(S) == 0 or len(S) == 1:
            return S

        stack = []

        i = 0
        while i < len(S):

            if len(stack) == 0 or stack[-1] != S[i]:
                stack.append(S[i])


            elif len(stack) > 0 and stack[-1] == S[i]:
                saved = S[i]

                while len(stack) > 0 and stack[-1] == saved:
                    stack.pop()
                # don't handle the look ahead in this problem. Unlike candy crush
            i += 1



        return ''.join(stack)