__author__ = 'deepika'

"""
Details
Runtime: 80 ms, faster than 29.35% of Python online submissions for Validate Stack Sequences.
Memory Usage: 13 MB, less than 8.33% of Python online submissions for Validate Stack Sequences.

changed the line popped[j] in stack -> i >= len(pushed)
Idea is you have something to pop and it doesn't match the top of stack
    -> Now, either it is still in push array, for this i >= len(pushed)
    -> Or, this order is not possible

Runtime: 100 ms, faster than 11.35% of Python online submissions for Validate Stack Sequences.
Memory Usage: 12.8 MB, less than 66.67% of Python online submissions for Validate Stack Sequences.

Further, removed a line
Runtime: 124 ms, faster than 6.81% of Python online submissions for Validate Stack Sequences.
Memory Usage: 12.8 MB, less than 66.67% of Python online submissions for Validate Stack Sequences.
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if (len(popped) != len(pushed) ):
            return False

        if (len(popped) == len(pushed) and len(popped) == 0):
            return True

        stack = []
        i = 0
        j = 0
        while True:
            if i < len(pushed) and len(stack) == 0: #pop is not possible on empty stack so put whatever you have
                stack.append(pushed[i])
                i = i + 1

            while i < len(pushed) and j < len(popped) and stack[-1]!= popped[j]: # while last on stack not equal to popped
                stack.append(pushed[i])
                i = i + 1

            while len(stack) > 0 and j < len(popped) and stack[-1] == popped[j]: #skip putting it in stack
                stack.pop()
                j = j + 1
                continue

            # If the code is reaching here and we still have something worth popping but it is out of order
            if len(stack) > 0 and j < len(popped) and i >= len(pushed):
               return False

            if len(stack) == 0 and i >= len(pushed) and j >= len(popped):
                return True


s=Solution()
print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(s.validateStackSequences([1, 0], [1, 0])) #Push 1 pop 1 push 0 pop 0


