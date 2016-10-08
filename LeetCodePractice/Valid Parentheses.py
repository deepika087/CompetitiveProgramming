
"""
20. Valid Parentheses
"""
class Solution:

    def _isOpening(self, bracket):
        if (ord(bracket) in [ord('['), ord('{'), ord('(')]):
            return True
        return False

    def _isClosing(self, bracket):
        if (ord(bracket) in [ord(']'), ord('}'), ord(')')]):
            return True
        return False

    def _isSame(self, openbracket, bracket2):
        if ( openbracket == '(' and bracket2 == ')'):
            return True
        if (openbracket == '[' and bracket2 == ']'):
            return True
        if (openbracket == '{' and bracket2 == '}'):
            return True
        return False

    def isValid(self, s):
        stack = []

        for bracket in s:
            if ( self._isClosing(bracket) and len(stack) == 0):
                return False
            if ( self._isOpening(bracket)):
                stack.append(bracket)
            else:
                openbracket = stack.pop(-1)
                if not( self._isSame(openbracket, bracket)):
                    return False
                else:
                    continue
        return True if (len(stack) == 0) else False


if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    print sol.isValid(s)
    s = "(]"
    print sol.isValid(s)
    s = "([)]"
    print sol.isValid(s)