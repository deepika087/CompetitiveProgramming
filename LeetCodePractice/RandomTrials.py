__author__ = 'deepika'


N=4
for l in range(2, N+1):
    for i in range(N-1, -1, -1):
        j = i + l - 1
        if (j < N):
            print i, j