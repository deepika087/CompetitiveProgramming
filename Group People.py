__author__ = 'deepika'


def display(gap):
    grid = [[ 0 for _ in range(5)] for k in range(10)]
    save = 1
    start = save
    for i in range(10):
        if (start > 1):
            start = save + 5
            save = start
        for j in range(5):
            if (j == 1):
                start = start + gap
            grid[i][j] = start % 50 if start % 50 != 0 else 50
            start = start + 1
    print customDisplayGrid2(grid)

def customDisplayGrid2(grid):
    line = ''
    for row in grid:
        line += ', '.join(str(x) for x in row)
        line += '\n'
    return line


if __name__ == "__main__":
    grid = [[ 0 for i in range(5)] for j in range(10)]
    gap = 0
    for i in range(10):
        print "For week: ", i + 1
        display(gap)
        gap = gap + 5



