__author__ = 'deepika'

"""
Print max length of valid parenthesis.
this is not same as LeetCdoe qs 32.

Cz in this case if string is ()()() the ouput should be 2.
If the string is ()()(()) then ouput should be 4.

 But in leetcode qs output will be 6 in the first case
 and 8 in second case. This can be done using stacks or left to right scan and then
 right to left scan.
 tutorial : https://leetcode.com/problems/longest-valid-parentheses/solution/
"""

class Solution(object):


    # such that ()(()) answer will be 4. Then this code is fine.
    def longestValidParenthesesIBM(self, arr):
        stack = []
        max_len = 0
        interval = None

        for i in range(len(arr)):
            if len(stack) == 0 and arr[i] == ')':
                interval = None
                continue
            elif arr[i] == '(':
                stack.append(i)
            else:
                popped = stack.pop(-1)
                curr = i

                if interval is None:
                    interval = (popped, curr)
                    max_len = max(max_len, curr - popped + 1)
                else:
                   if popped < interval[0] < curr and popped < interval[1] < curr:
                            interval = (popped, curr)
                            max_len = curr - popped + 1
                   else:
                        candidate_len = curr - popped + 1
                        if candidate_len > max_len:
                            max_len = candidate_len
                            interval = (popped, curr)
        return max_len

s=Solution()
assert s.longestValidParenthesesIBM("(()") == 2
assert s.longestValidParenthesesIBM("()()()") == 2
assert s.longestValidParenthesesIBM("()(())") == 4
assert s.longestValidParenthesesIBM("()(()") == 2