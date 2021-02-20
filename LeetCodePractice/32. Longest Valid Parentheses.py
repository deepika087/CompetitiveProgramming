class Solution(object):
    #such that ()()() will return 6 and ()(()) will return 6
    def longestValidParentheses(self, arr):
        #tutorial : https://leetcode.com/problems/longest-valid-parentheses/solution/
        stack = []
        max_len = 0
        for i in range(len(arr)):
            if arr[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    popped = stack.pop(-1)
                    if arr[popped] == '(':
                        continue
                else:
                    stack.append(i)
        if (len(stack) == 0):
            return len(arr)
        print stack
        a = len(arr)
        b = 0
        longest = 0
        while stack:
            b = stack.pop(-1)
            longest = max(longest, a-b-1)
            a = b
        longest = max(longest, a)
        return longest


    def longestValidParenthesesEasier(self, string):
        n = len(string)

        # Create a stack and push -1 as initial index to it.
        stk = []
        stk.append(-1)

        # Initialize result
        result = 0

        # Traverse all characters of given string
        for i in xrange(n):

            # If opening bracket, push index of it
            if string[i] == '(':
                stk.append(i)

            else:    # If closing bracket, i.e., str[i] = ')'

                # Pop the previous opening bracket's index
                stk.pop()

                # Check if this length formed with base of
                # current valid substring is more than max
                # so far
                if len(stk) != 0:
                    print "Value: ", stk[len(stk)-1] # I think this is next to top
                    result = max(result, i - stk[len(stk)-1])

                # If stack is empty. push current index as
                # base for next valid substring (if any)
                else:
                    stk.append(i)

        return result


s=Solution()
print s.longestValidParenthesesEasier("()")
print s.longestValidParenthesesEasier("(()")
print s.longestValidParenthesesEasier("()()()")
print s.longestValidParenthesesEasier(")()())()()(")

#assert s.longestValidParenthesesIBM(")()())()()(") == 4

