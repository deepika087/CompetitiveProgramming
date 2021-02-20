__author__ = 'deepika'

"""
Code to do DFS using Backtracking.
U r given a grid all initialized to 0. Yu have to reach rightmost bottom point of the grid.
The only caveat is that the path should be random. That is everytime you run the algo different
path should be returned.

Imp points in this Algo. Use -1 to mark the point that has been visitied. Rather than using visited array
Push only the popped element and the neighbour on to the stack.

If dead end occurs, decrease the counter and backtrack to the neighbour just visited.

Java Random

import java.util.Random
new Random().nextInt(max - min) + min
"""

import random

def findValidNeighbours(popped, grid):
    row = popped[0]
    col = popped[1]

    result = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            else:
                rowPrime = row + i
                colPrime = col + j
                if rowPrime < 0 or colPrime < 0 or rowPrime >= len(grid) or colPrime >= len(grid[0]):
                    continue
                if grid[rowPrime][colPrime] > 0 or  grid[rowPrime][colPrime] == -1 :
                    continue
                else:
                    result.append((rowPrime, colPrime))
    return result

def validRandomElement(a, b):
    return random.randint(a, b)

def printGrid(grid):
    print "------------------------\n"
    for row in grid:
        result = []
        for x in row:
            if x == -1:
                result.append(0)
            else:
                result.append(x)
        print result

def dfs(grid):
    rows = len(grid)
    cols = len(grid[0])

    stack = []
    counter = 1

    grid[0][0] = counter
    counter = counter + 1
    stack.append((0, 0))
    while stack:

        popped = stack.pop(-1)
        neighbours = findValidNeighbours(popped, grid)

        if len(neighbours) == 0:
            print "----> DEAD END <----- at position: ", popped, " stack : ", stack
            counter = counter - 1
            grid[popped[0]][popped[1]] = -1
            continue

        index = 0 if len(neighbours) == 1 else validRandomElement(0, len(neighbours)-1)
        _neighbour = neighbours.pop(index)
        stack += [popped]
        stack += [_neighbour]

        grid[_neighbour[0]][_neighbour[1]] = counter
        counter = counter + 1
        printGrid(grid)

        if (grid[rows - 1][cols - 1] > 0):
            print "Breaking cz reached end"
            break

dfs([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ])
