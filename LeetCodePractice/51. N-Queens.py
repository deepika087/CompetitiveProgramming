"""
9 / 9 test cases passed.
Status: Accepted
Runtime: 145 ms
"""

import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        arr = [-1 for i in range(n)]
        queen = 0
        solutions=[]
        self.solveNQueensUtil(arr, n, queen, solutions)
        #print "Received solutions" , solutions
        finalresult = []
        for _ in solutions:
            finalresult.append(self.display(_))
        return finalresult

    def display(self, vec):
        result = []
        for col in vec:
            s = ['.'] * len(vec)
            s[col] = 'Q'
            res1 = ''.join(s)
            #res1 = "\"" + res1 + "\""
            result.append(res1)
        return result

    def solveNQueensUtil(self, arr, n, queen, solutions):
        if (queen == n):
            return True
        #set queen row wise. Pick a row and find the best column.
        for i in range(n):
            if (self.check_and_place(arr, queen, i) and self.solveNQueensUtil(arr, n, queen + 1, solutions)):
                solutions.append(copy.copy(arr))
        return False

    def check_and_place(self, arr, row, col):
        for j in range(row):
            #print "row:", row, " col:", col, " j:", j, " arr: ", arr
            if (arr[j] == col or ((row - j) == abs(col - arr[j]))):
                return False

        arr[row] = col
        return True

s=Solution()
print s.solveNQueens(4)
print s.solveNQueens(1)
