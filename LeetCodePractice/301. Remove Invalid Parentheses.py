class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        str = list(s)
        stack = []
        for i in range(len(str)):
            if str[i] == '(':
              stack.append(i)
            elif str[i] == ')':
              if not stack:
                #print "Hit this for str : ", str, " at i = ",i
                str[i] = '*'
              else:
                stack.pop()

        for i in stack:
            str[i] = '*'

        return ''.join(str).replace('*', '')

s=Solution()
print s.removeInvalidParentheses("()())()")