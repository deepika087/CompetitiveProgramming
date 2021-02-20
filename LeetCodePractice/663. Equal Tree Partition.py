

class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.finalResult = False

    def sumTree(self, root):
        if root is None:
            return 0
        return self.sumTree(root.left) + root.data + self.sumTree(root.right)

    def checkEqualTree(self, root):
        seen = []

        def sum_(node):
            if not node: return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            print seen
            return seen[-1]

        total = sum_(root)
        print "total : " , total
        seen.pop()
        print "new seen : ", seen, total/2
        return (total/2) in seen # this should work

    def checkEqualTree_mine(self, root):

        if root is None:
            return 0

        sumT = self.sumTree(root)

        self.checkEqualUtil(root, sumT)

    def checkEqualUtil(self, root, sumT):
        if root is None:
            return 0

        tempSum = self.checkEqualUtil(root.left, sumT) + root.data + self.checkEqualUtil(root.right, sumT)
        print("Tempsum " + str(tempSum))
        if (tempSum == sumT - tempSum):
            print("At tempSum = " + str(tempSum))
            self.finalResult = True
        return tempSum


s=Solution()
n1 = Node(5)
n1.left = Node(10)
n1.right = Node(10)
n1.right.left = Node(2)
n1.right.right = Node(3)

s.checkEqualTree(n1)
print(s.finalResult)


s2 = Solution()
n2 = Node(1)
n2.left = Node(2)
n2.right = Node(10)
n2.right.left = Node(2)
n2.right.right = Node(20)
s2.checkEqualTree(n2)
print(s2.finalResult)


s3 = Solution()
n3 = Node(0)
n3.left = Node(-1)
n3.right = Node(1)
s3.checkEqualTree(n3)
print(s3.finalResult)

s4 = Solution()
n4 = Node(0)
n4.left = Node(-1)
n4.right = Node(1)
s4.checkEqualTree(n4)
print(s4.finalResult)





