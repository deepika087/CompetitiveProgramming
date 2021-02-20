__author__ = 'deepika'

def binarySearch(sortedBwd, part2):
    if (len(sortedBwd) == 1):
        return 0,sortedBwd[0][1]

    lo = 0
    hi = len(sortedBwd) - 1

    while (lo < hi):
        mid = hi - (hi - lo)/2
        if sortedBwd[mid][1] == part2:
            return mid, sortedBwd[mid][1]

        if (sortedBwd[mid][1] < part2):
            lo = mid + 1
        else:
            hi = mid - 1

    return lo, sortedBwd[lo][1]

def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    sortedFwd = sorted(forwardRouteList, key= lambda x: x[1])
    sortedBwd = sorted(returnRouteList, key= lambda x: x[1])

    probableResult = []
    minFwd = sortedFwd[0]
    minBwd = sortedBwd[0]


    for i in range(0, len(sortedFwd)):
        part1 = sortedFwd[i][1]
        part2 = maxTravelDist - part1

        if (part2 <= 0):
            continue
        index, resPart2 = binarySearch(sortedBwd, part2)
        if part1 + resPart2 <= maxTravelDist:
            probableResult.append([sortedFwd[i][0], sortedBwd[index][0], part1 + resPart2 ])


    probableResult = sorted(probableResult , key= lambda x: x[2], reverse=True)

    if len(probableResult) == 0:
        return []

    max_so_far = probableResult[0][2]


    result = [ [ probableResult[0][0], probableResult[0][1] ] ]
    for i in range(1, len(probableResult)):
        if max_so_far == probableResult[i][2]:
            result.append([ probableResult[i][0], probableResult[i][1] ])
        else:
            break

    print(result)








optimalUtilization(10000, [[1, 3000], [2, 5000], [3, 7000], [4, 10000]], [[1, 2000], [2, 3000], [3, 4000], [4, 5000]])
optimalUtilization(7000, [ [1, 2000], [2, 4000], [3, 6000] ], [[1, 2000]])