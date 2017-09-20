__author__ = 'deepika'
"""
12 / 12 test cases passed.
Status: Accepted
Runtime: 52 ms
"""
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return (1)
        list1, list2 = list(), list()
        for i in range(n):
            list1.append(i + 1)

        while True:
            while list1:
                poppedA = list1.pop(0)
                poppedB = list1.pop()
                list2.append((poppedA, poppedB))

            if len(list1) == 0 and len(list2) == 1:
                return str(list2[0]).replace(" ", "")

            while list2:
                poppedA = list2.pop(0)
                poppedB = list2.pop()
                list1.append((poppedA, poppedB))

            if len(list2) == 0 and len(list1) == 1:
                return str(list1[0]).replace(" ", "")

s=Solution()
print s.findContestMatch(2)
print s.findContestMatch(4)
print s.findContestMatch(8)
print s.findContestMatch(16)