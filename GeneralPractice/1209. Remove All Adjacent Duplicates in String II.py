__author__ = 'deepika'


"""
I want to use writer and other pointer approach for this problem.
This writer approach doesn't work because say abbcc k = 2 say you have vanished bb.
Now writer is at a and i is at c. Now how do you increment writer? and also, when you decrement writer
Will it be enough?? because we don't want to strictly decrease it by 1.

Runtime: 100 ms, faster than 37.22% of Python online submissions for Remove All Adjacent Duplicates in String II.
Memory Usage: 14.5 MB, less than 44.40% of Python online submissions for Remove All Adjacent Duplicates in String II.

"""

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        if len(s) < k:
            return s

        stack = []
        i = 0

        while i < len(s):

            if len(stack) == 0 or stack[-1][0] != s[i]:
                stack.append( [s[i], 1] )
                i += 1

            elif len(stack) > 0 and stack[-1][0] == s[i] and stack[-1][1] < k:
                stack[-1][1] += 1

                if stack[-1][1] >= k:
                    saved = s[i]

                    if len(stack) > 0 and stack[-1][0] == saved:
                        stack.pop()

                    # No look ahead even in this case.
                    # while i < len(s) and s[i] == saved:
                    #    i += 1
                i += 1


        print('' if len(stack) == 0 else ''.join(map(lambda x: x[0] * x[1], stack)))
        return '' if len(stack) == 0 else ''.join(map(lambda x: x[0] * x[1],  stack))

s=Solution()
assert s.removeDuplicates(s = "abcd", k = 2) == "abcd"
assert s.removeDuplicates(s = "deeedbbcccbdaa", k = 3) == "aa"
assert s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2) == "ps"







