__author__ = 'deepika'

def check_for(array, i, j):
    element = array[i][j]
    n = len(array)
    m = len(array[0])

    for k in range(-1, 2, 1):
        for l in range(-1, 2, 1):
            if k == 0 and l == 0:
                continue
            i_prime = i + k
            j_prime = j + l
            if (i_prime >= n or i_prime < 0 or j_prime >= m or j_prime < 0):
                continue
            if array[i_prime][j_prime] <= element:
                return False
    return True

def find_minima(size, array):
    n = len(array)
    m = len(array[0])

    result = []
    for i in range(n):
        for j in range(m):
            print "Checking for :", array[i][j]
            if check_for(array, i, j):
                result.append(array[i][j])

    if len(result) == 0:
        return []
    result = sorted(result)
    if len(result) > 3:
        result = result[0:3]
    for i in result:
        print i

n = 5
m = [
    [5., 5., 5., 5., 5.],
    [5., 1., 5., 5., 5.],
    [5., 5., 5., 4., 5.],
    [5., 5., 4., 2., 3.],
    [0., 5., 5., 3., 4.]
]

print find_minima(n, m)
