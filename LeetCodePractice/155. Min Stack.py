__author__ = 'deepika'

"""
18 / 18 test cases passed.
Status: Accepted
Runtime: 85 ms
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        else:
            element = self.minStack[-1]
            if element > x:
                self.minStack.append(x)
            else:
                self.minStack.append(element)


    def pop(self):
        """
        :rtype: void
        """
        if self.minStack:
            self.minStack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

