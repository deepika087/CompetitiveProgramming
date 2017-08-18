class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateParenthesisUtil("", result, n, n)
        return result

    def generateParenthesisUtil(self, string_so_far, result, left, right):
        if (left > right):
            return
        if left:
            self.generateParenthesisUtil(string_so_far + '(', result, left-1, right)
        if (right > left):
            self.generateParenthesisUtil( string_so_far + ')', result, left, right-1)
        if not right:
            result.append(string_so_far)
            return

s=Solution()
print s.generateParenthesis(3)
