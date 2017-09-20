'''
n, m

n -> n*n grids, intialized to 0
m -> flip m of the grids

n = 3, m = 2

000
000
000

110
000
000

000
101
000

100
010
000

...

function(n, m)

=>

all the combinatios?

count

comb1

comb2

comb3

...

'''


"""
000
000
000

100
000
000

110
100
000

100
000
100
"""
import copy

def customDisplayGrid2(grid):
    line = ''
    for row in grid:
        line += ''.join(str(x) for x in row)
        line += '\n'
    return line


def startDFS(grid, n, m, i, j, result, processed):
    #Possible neighbours for i, j are i, j+1; i+1, j; i+1, j+1;
    if (m == 0):
        print customDisplayGrid2(grid)
        result.add(customDisplayGrid2(grid))
        return

    for k1 in range(-1, 2, 1):
        for k2 in range(-1, 2, 1):
            if (k1 == 0 and k2 == 0):
                continue
            i_prime = i + k1
            j_prime = j + k2
            if ((i_prime, j_prime) in processed):
                continue
            if (0 <= i_prime < n and 0 <= j_prime < n):
                grid[i_prime][j_prime] = 1
                processed.add((i_prime, j_prime))
                startDFS(grid, n, m - 1, i_prime, j_prime, result, processed)
                grid[i_prime][j_prime] = 0
                startDFS(grid, n, m, i_prime, j_prime, result, processed)
                #processed.remove((i_prime, j_prime))

def dfs(n, m):
    processed = set()
    grid = [ [0 for _ in range(n)] for j in range(n)]
    result = set()
    for i in range(n):
        for j in range(n):
            grid[i][j] = 1 #set
            processed.add((i, j))
            tempProcessed = copy.copy(processed)
            startDFS(grid, n, m-1, i, j, result, tempProcessed)
            grid[i][j] = 0 #unset

    print "Total combinations possible: ", len(result)
    #for _r in result:
    #    print _r


dfs(3, 3)



