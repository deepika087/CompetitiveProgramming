__author__ = 'deepika'


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    count = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        path = []
        self.pathSumUtil2(root, sum, path)
        return self.count

    """
    The issue with this approach is the it cuts the sum_so_far. For ex:
        5 -> 3 : sum = 8 so I reset sum_so_Far = 0
        what is 5 -> 3 -> -3 -> 0 This is a valid path as well with sum  =0
    """
    def pathSumUtil(self, root, sum, sum_so_far):
        if root is None:
            return 0

        if sum_so_far == sum or root.val == sum:
            self.count += 1
            sum_so_far = 0
        elif root.val > sum:
            sum_so_far = 0
        else:
            sum_so_far += root.val

        self.pathSumUtil(root.left, sum, sum_so_far)
        self.pathSumUtil(root.right, sum, sum_so_far)

    """
        Can be further optimized using hashamps.

        Cz starting from every i we traverse backwards and do the cummulative sum.
    """
    def pathSumUtil2(self, root, sum, path):
        if root is None:
            return 0

        path.append(root.val)

        sumT = 0
        for i in range(len(path) - 1, -1, -1):
            sumT += path[i]
            if sumT == sum:
                self.count += 1

        self.pathSumUtil2(root.left, sum, path)
        self.pathSumUtil2(root.right, sum, path)

        path.pop()

s=Solution()
root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(-3)
root.left.left=TreeNode(3)
root.left.right=TreeNode(2)
root.left.left.left=TreeNode(3)
root.left.left.right=TreeNode(-2)
root.left.right=TreeNode(2)
root.left.right.right=TreeNode(1)
root.right.right=TreeNode(11)

print(s.pathSum(root, 8))

