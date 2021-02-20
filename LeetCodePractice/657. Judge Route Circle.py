__author__ = 'deepika'

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        start = [0, 0]
        for pos in moves:
            if pos == 'U':
                start[1] += 1
            elif pos == 'D':
                start[1] -= 1
            elif pos == 'R':
                start[0] += 1
            else:
                start[0] -= 1

        return start == [0, 0]

s=Solution()
assert s.judgeCircle("UD") == True
assert s.judgeCircle("LL") == False