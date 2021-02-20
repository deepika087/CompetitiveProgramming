__author__ = 'deepika'
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op not in ["C","D","+"]:
                stack.append(int(op))
            else:
                if op == "C":
                    stack.pop()
                elif op == "D":
                    lastElement = stack[-1]
                    stack.append(lastElement * 2)
                elif op == "+":
                    last1 = stack[-1]
                    last2 = stack[-2]
                    stack.append(last1 + last2)
                else:
                    print "Received something unusual: ", op
        return sum(stack)

s=Solution()
assert s.calPoints(["5","2","C","D","+"]) == 30
assert s.calPoints(["5","-2","4","C","D","9","+","+"]) == 27

