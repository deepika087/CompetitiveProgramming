#Definition for a binary tree node.
"""
33 / 33 test cases passed.
Status: Accepted
Runtime: 66 ms
"""
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        s1=deque();
        s2=deque();
        result=[]
        #Optimization
        s1.append(root)

        while(True):

            nextLevelList = []
            while(len(s1) > 0):
                temp = s1.pop()
                if (temp):
                    nextLevelList.append(temp.val)
                    if(temp.left):
                        s2.append(temp.left)
                    if (temp.right):
                        s2.append(temp.right)
            if(len(nextLevelList) > 0):
                result.append(nextLevelList)

            nextLevelList=[]
            while(len(s2) > 0):

                temp=s2.pop()
                if (temp):
                    nextLevelList.append(temp.val)
                if(temp.right):
                    s1.append(temp.right)
                if(temp.left):
                    s1.append(temp.left)

            if(len(nextLevelList) > 0):
                result.append(nextLevelList)
            if (len(s1) == 0 and len(s2) == 0):
                break;
        return result

s=Solution()
t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.left.left=TreeNode(4)
t.left.right=TreeNode(5)
t.right.left=TreeNode(6)
t.right.right=TreeNode(7)
t.left.left.left=TreeNode(8)
t.left.left.right=TreeNode(9)
print s.zigzagLevelOrder(t)




        