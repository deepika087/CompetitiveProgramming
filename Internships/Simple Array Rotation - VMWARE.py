# Complete the function below.
"""
All test cases worked
given an array and rotation array. Iterate through element of rotation array
rotate(left) array with those many times and return index of maximum element
in the rotated array. So the size of result should be equal to size of rotation array.
"""

def handleRotation(arr, rot, max_orig):

    rot = rot % len(arr)

    if (rot == 0 or rot == len(arr)):
        return max_orig

    if (rot <= max_orig):
        return max_orig - rot

    if (rot > max_orig):
        rot = rot - max_orig
        return len(arr) - rot

def getMaxElementIndices(a, rotate):

    result = []
    max_orig = a.index(max(a))
    for rot in rotate:
        result.append(handleRotation(a, rot, max_orig))
    return result

#print getMaxElementIndices([1, 2, 4, 3], [0, 2])
#print getMaxElementIndices([1, 2, 3, 4], [1, 2, 4])
print getMaxElementIndices([1, 2, 4, 3], [1, 3])

