__author__ = 'deepika'

"""
Success
Details
Runtime: 248 ms, faster than 42.86% of Python online submissions for Push Dominoes.
Memory Usage: 21 MB, less than 20.41% of Python online submissions for Push Dominoes.
"""


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """


        force = [0] * len(dominoes)
        N = len(dominoes)
        if N == 0:
            return ""

        # from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f
        f=0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0 )
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)
      #  return "".join('.' if force[i] == '0' else 'R' if force[i] > 0 else 'L' for i in range(N))

s=Solution()
print(s.pushDominoes("RL"))
print(s.pushDominoes("R.L"))
print(s.pushDominoes("R.......L"))
