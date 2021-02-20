__author__ = 'deepika'


"""
The problem was something like say you have a list
    [1, [2, 3], 4, [5, 6, [7]]]
    You have to return the sum such that each sum at each level is multiplied by depth in reverse.
    For  instance 1, 4 is at level 1 but total depth of the arr = 4 so 1+4 will be multiplies by 4.
    [2, 3] is at level 2 but it will be multiplies by 3


[1, 2, 3, 4] - Are all at same level.
[1, [2], 3] - 1, 3 are at same level.
"""



def mainFunction(arr):
    sum_of_levels = {}
    saveLevels(arr, 0, sum_of_levels)
    print(sum_of_levels)
    rev_depth = len(sum_of_levels.keys())

    result = 0
    for k, v in sum_of_levels.items():
        result += v * rev_depth
        rev_depth -= 1

    return result

def saveLevels(arr, d, sum_of_levels):


    total = 0
    for item in arr:
        if isinstance(item, list):
            saveLevels(item, d + 1, sum_of_levels)
        else:
            total += item

    sum_of_levels[d] = sum_of_levels.get(d, 0) + total

print(mainFunction([1, 2, 3, 4]))
print(mainFunction([1, 2, [3, 4]]))
print(mainFunction([1, 2, [3, [4] ] ]))
print(mainFunction([1, 2, [3], [4] ]))
print(mainFunction([1, [2, 3], 4, [5, 6, [7]]]))