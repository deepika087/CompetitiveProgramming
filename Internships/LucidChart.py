import sys
import re

def longest_subsequence(grid):
    m = len(grid)
    n = len(grid[0])

    max = -1
    max_visited = list();

    for i in range(m):
        for j in range(n):
            #Create a bfs run
            if (i,j) not in max_visited:
                print "Running for i = ", i, " and j = ", j
                queue = list([])
                visited = list()

                queue.append((i,j))

                while(queue):
                    popped = queue.pop(0)
                    #popped = grid[popped[0]][popped[1]]
                    source = grid[popped[0]][popped[1]]
                    iPrime = popped[0]
                    jPrime = popped[1]


                    #Search for valid neighbours
                    left = grid[iPrime][jPrime-1] if jPrime-1 >= 0 and (iPrime,jPrime-1) not in visited else -sys.maxint
                    right = grid[iPrime][jPrime+1] if jPrime+1 < n and (iPrime,jPrime+1) not in visited else -sys.maxint
                    bottom = grid[iPrime+1][jPrime] if iPrime+1 < m and (iPrime+1,jPrime) not in visited  else -sys.maxint
                    up = grid[iPrime-1][jPrime] if iPrime-1 >= 0 and (iPrime-1,jPrime) not in visited else -sys.maxint
                    diagLeft = grid[iPrime-1][jPrime-1] if iPrime-1>=0 and jPrime-1>=0 and (iPrime-1,jPrime-1) not in visited else -sys.maxint
                    diagRight = grid[iPrime-1][jPrime+1] if iPrime-1>=0 and jPrime+1<n and (iPrime-1,jPrime+1) not in visited else -sys.maxint
                    diagDownLeft = grid[iPrime+1][jPrime-1] if iPrime+1<m and jPrime-1>=0 and (iPrime+1,jPrime-1) not in visited else -sys.maxint
                    diagDownRight = grid[iPrime+1][jPrime+1] if iPrime+1<m and jPrime+1<n and (iPrime+1,jPrime+1) not in visited else -sys.maxint

                    if left > -sys.maxint and abs(source - left) > 3:
                        queue.append([left] + popped)
                        visited.append((i,j-1))
                    if right > -sys.maxint and abs(source - right) > 3:
                        queue.append([right] + popped)
                        visited.append((i,j+1))
                    if bottom > -sys.maxint and abs(source - bottom) > 3:
                        queue.append([bottom] + popped)
                        visited.append((i+1,j))
                    if up > -sys.maxint and abs(source - up) > 3:
                        queue.append([up] + popped)
                        visited.append((i-1,j))
                    if diagLeft > -sys.maxint and abs(source - diagLeft) > 3:
                        queue.append([diagLeft] + popped)
                        visited.append((i-1,j-1))
                    if diagRight > -sys.maxint and abs(source - diagRight) > 3:
                        queue.append([diagRight] + popped)
                        visited.append((i-1,j+1))
                    if diagDownLeft > -sys.maxint and abs(source - diagDownLeft) > 3:
                        queue.append([diagDownLeft] + popped)
                        visited.append((i+1,j-1))
                    if diagDownRight > -sys.maxint and abs(source - diagDownRight) > 3:
                        queue.append([diagDownRight] + popped)
                        visited.append((i+1,j+1))

                    # find the path with max len
                    for q in queue:
                        if (len(q) > max):
                            max = len(q);
                            print "Updated max to ", max , " for list = ", q;
                    max_visited = max_visited + q;
                    print "Coordinates to be ignored :" , max_visited
                # Keep a track of max so far

def dfs_approach(grid):
    m = len(grid)
    n = len(grid[0])

    max = -1
    for i in range(m):
        for j in range(n):
            row = (i, j)
            items = []

            stack = []
            stack.append(grid[i][j])
            while(len(stack) > 0):

                source = stack.pop(0)

                left = grid[i][j-1] if j-1 >= 0 else -sys.maxint
                right = grid[i][j+1] if j+1 < n else -sys.maxint
                bottom = grid[i+1][j] if i+1 < m else -sys.maxint
                up = grid[i-1][j] if i-1 >= 0 else -sys.maxint

                diagLeft = grid[i-1][j-1] if i-1>=0 and j-1>=0 else -sys.maxint
                diagRight = grid[i-1][j+1] if i-1>=0 and j+1<n else -sys.maxint
                diagDownLeft = grid[i+1][j-1] if i+1<m and j-1>=0 else -sys.maxint

                diagDownRight = grid[i+1][j+1] if i+1<m and j+1<n else -sys.maxint

def startNavigation(grid, i, j, visited, path):
    #if ( i < 0 or j < 0 or i > len(grid) or j > len(grid[0])):
    #    return
    if (j-1 >= 0 and visited[i][j-1] == False and abs(grid[i][j] - grid[i][j-1]) > 3):
        visited[i][j-1] = True;
        print "Selected ", grid[i][j-1], " at i = ", i , " and j = ", j-1, " with path = ", path
        path += [grid[i][j-1]]
        startNavigation(grid, i, j-1, visited, path)

    if (j+1 < len(grid[0]) and visited[i][j+1] == False and abs(grid[i][j] - grid[i][j+1]) > 3):
        visited[i][j+1] = True;
        path += [grid[i][j+1]]
        print "Selected ", grid[i][j+1], " at i = ", i , " and j = ", j+1, " with path = ", path
        startNavigation(grid, i, j+1, visited, path)

    if (i+1 < len(grid) and visited[i+1][j] == False and abs(grid[i][j] - grid[i+1][j]) > 3):
        visited[i+1][j] = True;
        path += [grid[i+1][j]]
        print "Selected ", grid[i+1][j], " at i = ", i+1 , " and j = ", j, " with path = ", path
        startNavigation(grid, i+1, j, visited, path)

    if (i-1 >= 0 and visited[i-1][j] == False and abs(grid[i][j] - grid[i-1][j]) > 3):
        visited[i-1][j] = True;
        path += [grid[i-1][j]]
        print "Selected ", grid[i-1][j], " at i = ", i-1 , " and j = ", j, " with path = ", path
        startNavigation(grid, i-1, j, visited, path)

    if (i-1>=0 and j-1>=0 and visited[i-1][j-1] == False and abs(grid[i][j] - grid[i-1][j-1]) > 3):
        visited[i-1][j-1] = True
        path += [grid[i-1][j-1]]
        print "Selected ", grid[i-1][j-1], " at i = ", i-1 , " and j = ", j-1, " with path = ", path
        startNavigation(grid, i-1, j-1, visited, path)

    if (i-1>=0 and j+1<len(grid[0]) and visited[i-1][j+1] == False and abs(grid[i][j] - grid[i-1][j+1]) > 3):
        visited[i-1][j+1] = True
        path += [grid[i-1][j+1]]
        print "Selected ", grid[i-1][j+1], " at i = ", i-1 , " and j = ", j+1, " with path = ", path
        startNavigation(grid, i-1, j+1, visited, path)

    if (i+1<len(grid) and j-1>=0 and visited[i+1][j-1] == False and abs(grid[i][j] - grid[i+1][j-1]) > 3):
        visited[i+1][j-1] = True
        path += [grid[i+1][j-1]]
        print "Selected ", grid[i+1][j-1], " at i = ", i+1 , " and j = ", j-1, " with path = ", path
        startNavigation(grid, i+1, j-1, visited, path)

    if (i+1<len(grid) and j+1<len(grid[0]) and visited[i+1][j+1] == False and abs(grid[i][j] - grid[i+1][j+1]) > 3):
        visited[i+1][j+1] = True
        path += [grid[i+1][j+1]]
        print "Selected ", grid[i+1][j+1], " at i = ", i+1 , " and j = ", j+1, " with path = ", path
        startNavigation(grid, i+1, j+1, visited, path)

    #If reached here
    return

def longest_subsequence_dfs(grid):
    m = len(grid)
    n = len(grid[0])


    for i in range(m):
        for j in range(n):
            print "starting from node : ", grid[i][j]
            visited = [ [False for _ in range(n)] for _ in range(m)]
            visited[i][j] = True
            path = [grid[i][j]]
            startNavigation(grid, i, j, visited, path)
            print "Path after navigation", path, " with len = ", len(path)


def main():
    dims = [int(i) for i in sys.stdin.readline().split()]
    num_rows, num_cols = dims
    grid = [[int(i) for i in sys.stdin.readline().split()] for _ in range(num_rows)]

    res = longest_subsequence_dfs(grid)
    print(str(res) + "\n")

if __name__ == "__main__":
    main()