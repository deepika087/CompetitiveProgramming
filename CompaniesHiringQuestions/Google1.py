__author__ = 'deepika'

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def findEmptyLeft(roses, index, K):
    if index - 0 < K:
        return False

    i = 0
    count = 0
    max_count = 0
    while True:
        if i == index:
            max_count = max(max_count, count)
            break

        if i < index and roses[i] == 1:
            max_count = max(max_count, count)
            count = 0
            i = i + 1
            continue

        if i >= index:
            return False

        if roses[i] == 0:
            count = count + 1
            i = i + 1

    if max_count == K:
        return True
    return False

def findEmptyRight(roses, index, K):
    if len(roses) - index < K:
        return False

    i = index + 1
    count = 0
    max_count = 0
    while True:
        if i == len(roses):
            max_count = max(max_count, count)
            break

        if i < len(roses) and roses[i] == 1:
            max_count = max(max_count, count)
            count = 0
            i = i + 1
            continue

        if i >= len(roses):
            break

        if roses[i] == 0:
            count = count + 1
            i = i + 1

    if max_count == K:
        return True
    return False


def solution(P, K):
    # write your code in Python 2.7
    roses = [ 0 for i in range(len(P))]

    prev = None
    for i in range(len(P)):
        roses[P[i] - 1] = 1
        #if i == 0:
        emptyLeft = findEmptyLeft(roses, P[i] - 1, K)
        if emptyLeft:
            return i + 1

        emptyRight = findEmptyRight(roses, P[i] - 1, K)
        if emptyRight:
            return i + 1

    return -1


print solution([2, 5, 1, 4, 3], 2)
print solution([2, 4, 3, 1, 5], 2)
print solution([2, 1, 4, 3], 1)
print solution([2, 5, 6, 4, 3, 1], 2)



