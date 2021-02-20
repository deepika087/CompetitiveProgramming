__author__ = 'deepika'
import sys

# Given an array with pairs such that difference in minimum between a[i] and a[j] such that i < j
def closestNumbers(numbers):
    num = []
    for i in range(len(numbers)):
        num.append((numbers[i], i))
    num = sorted(num, key=lambda x: x[0])
    print num

    minElement = sys.maxint
    for i in range(1, len(numbers)):
        if num[i][0] - num[i-1][0] <= minElement:
            if num[i][0] - num[i-1][0] < minElement:
                result = []
            minElement = num[i][0] - num[i-1][0]
            result.append([num[i], num[i-1]])

    print result
    newRes = []
    for _res in result:
        partA = _res[0]
        partB = _res[1]

        if partA[0] < partB[0]:
            newRes.append([partA[0], partB[0]])
        else:
            newRes.append([partB[0], partA[0]])
    newRes = sorted(newRes, key=lambda x: x[0])
    for _r in newRes:
        print _r[0] ,_r[1]
    #print newRes


closestNumbers([4, 2, 1, 3])