__author__ = 'deepika'


"""
https://aonecode.com/amazon-online-assessment-zombie-matrix
"""
class Solution:
    def humanDays(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])

        zombie = 1
        human = 0

        dist = [ [ float('inf') for i in range(n)] for _ in range(m)]
        queue = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == zombie:
                    queue.append( (i, j) )

        maxDays = -float('inf')
        numzombies = len(queue)
        numHuman = m*n - numzombies

        if numHuman == 0:
            return 0

        days = 0

        while queue:

            days += 1


            nextLevel = []
            while queue:
                popped = queue.pop(0)

                for dirs in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    newI = popped[0] + dirs[0]
                    newJ = popped[1] + dirs[1]

                    if newI >= 0 and newI < m and newJ >= 0 and newJ < n:
                        if matrix[newI][newJ] == human:
                            matrix[newI][newJ] = zombie
                            numHuman -= 1

                            queue.append( (newI, newJ) )
                            nextLevel.append( popped )

                            break # Cz one zombie can only move ones in a day


            #days += 1
            queue = nextLevel
            print(matrix)
            if numHuman == 0:
                break
        return days

s=Solution()
print(s.humanDays(
[[1],
[0],
[0],
[0]]))
print(s.humanDays([[0, 1, 1, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 1],
[0, 1, 0, 0, 0]]))



