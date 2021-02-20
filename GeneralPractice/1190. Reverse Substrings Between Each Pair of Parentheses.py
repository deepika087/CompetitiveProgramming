__author__ = 'deepika'

#Won't work

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        if (len(s) == 1):
            return s

        stack = []
        countOfBrackets = 0
        anotherString = ['S' for i in range(len(s))]
        for i in range(0, len(s)):
            if (s[i] == '('):
                stack.append(['(', i])
                anotherString[i] = '('
                countOfBrackets = countOfBrackets + 1;
            elif s[i] == ')':
                stack.append([')', i]);
                anotherString[i] = ')'
                countOfBrackets = countOfBrackets + 1;

        while(len(stack)):
            closing = stack.pop(-1)
            opening = stack.pop(-1)

            for i in range(opening[1] + 1, closing[1]):
                if anotherString[i] == 'R':
                    anotherString[i] = 'S'
                else:
                    anotherString[i] = 'R'

        print(anotherString)
        newS = ['a' for i in range(len(s))]
        print(newS)
        startJ = 0;
        EndJ = len(newS) - 1
        for i in range(len(anotherString)):
            print("startJ: ", startJ)
            if (anotherString[i] == ')' or anotherString[i] == '('):
                newS[startJ] = anotherString[i]
                startJ += 1
            elif anotherString[i] == 'R':
                newS[EndJ] = s[i]
                EndJ -= 1;
            else:
                newS[i] = anotherString[i]
                #startJ += 1
        print(newS)


s=Solution()
print(s.reverseParentheses("(ed(et(oc))el)"))

