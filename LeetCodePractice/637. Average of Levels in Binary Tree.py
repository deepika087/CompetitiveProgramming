"""
64 / 64 test cases passed.
Status: Accepted
Runtime: 76 ms
"""
import math
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue1 = []
        queue2 = []
        queue1.append(root)
        count = 0
        result = []
        while(len(queue1) or len(queue2)):
            #print "queue1: ", len(queue1), " queue2: ", len(queue2)
            sumT = 0
            numEle = 0
            while (len(queue1) > 0):
                popped = queue1.pop(0)
                if popped:
                    sumT = sumT + popped.val
                    numEle = numEle + 1
                    if (popped.left):
                        queue2.append(popped.left)
                    if (popped.right):
                        queue2.append(popped.right)
            count = count + 1
            result.append(sumT* 1.0/numEle)
            if (len(queue2) == 0):
                break

            sumT = 0
            numEle = 0
            while(len(queue2) > 0):
                popped = queue2.pop(0)
                if popped:
                    sumT = sumT + popped.val
                    numEle = numEle + 1
                    if (popped.left):
                        queue1.append(popped.left)
                    if (popped.right):
                        queue1.append(popped.right)
            count = count + 1
            result.append(sumT* 1.0/numEle)
            if (len(queue1) == 0):
                break
        return result

root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)

root2=TreeNode(1)
root2.right=TreeNode(3)

s=Solution()
print s.averageOfLevels(root)
