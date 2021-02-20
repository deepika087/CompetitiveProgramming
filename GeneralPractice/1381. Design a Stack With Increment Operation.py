__author__ = 'deepika'

"""
My approach was that I will maintain a height map and then when I have to pop I will see that if the current len < any k
then I will accumulate the result and then add it to the popped element.

But Now say I had 5 elements initially popped 3 and now pushed 3 more. So, my heights dictionary will also impact the new
elements which should not be the case.

Runtime: 124 ms, faster than 53.97% of Python online submissions for Design a Stack With Increment Operation.
Memory Usage: 13.6 MB, less than 15.87% of Python online submissions for Design a Stack With Increment Operation.

But as of now approach is pretty basic no pre-computation nothing.
"""

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.heights = dict()
        self.maxSize = maxSize


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1

        val = self.stack.pop()
        return val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(0, min(k, len(self.stack))):
            self.stack[i] += val




s=None
null = None
input1 = ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
input2 = [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
output1 = [null,null,null,2,null,null,null,null,null,103,202,201,-1]

for i in range(0, len(input1)):
    print("Runnning i : ", i)
    if i == 0:
        s=CustomStack(input2[i][0])
    elif input1[i] == "push":
        s.push(input2[i][0])
    elif input1[i] == "increment":
        s.increment(input2[i][0], input2[i][1])
    else: #means pop
        assert s.pop() == output1[i]

