__author__ = 'deepika'


class Solution:

    def SolveGame(self, extraSteps, n): # numbers from 0 to N-1

        N = n * n;
        visited = [ False for i in range(N) ]

        queue = []
        queue.append( [0] )

        dist = 0
        while len(queue) > 0:

            nextLevel = []


            while len(queue) > 0:
                path = queue.pop(-1)
                popped = path[0]

                if popped == N-1:
                    return dist, path

                neighbours = self.getNeighbours(popped, extraSteps, visited, N)

                if len(neighbours) > 0:
                    for neighbour in neighbours:
                        if neighbour in extraSteps:
                            newPath = [extraSteps[neighbour]]
                            newPath.append(neighbour)
                            newPath.extend(path)
                            nextLevel.append(newPath)
                        else:
                            newPath = [neighbour]
                            newPath.extend(path)
                            nextLevel.append(newPath)
                visited[popped] = True

            dist += 1
            queue = nextLevel

        return None, None

    def getNeighbours(self, vertex, extraSteps, visited, N):
        neighbours = []

        count = 1
        while count <= 6 and count < N:
            V1 = vertex + count

            if V1 >= N:
                break

            if not visited[V1]:
                """
                if V1 in extraSteps:
                    neighbours.append(extraSteps[V1]) # Now if you do this you lose the info for V1 cz you go to extraSteps[V1]
                """
                neighbours.append(V1)

            count += 1
        return neighbours


s=Solution()
moves = dict()
# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
print(s.SolveGame(moves, 6))

