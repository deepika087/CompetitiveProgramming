# Complete the function below.
"""
All test cases worked
given an array and rotation array. Iterate through element of rotation array
rotate(left) array with those many times and return index of maximum element
in the rotated array. So the size of result should be equal to size of rotation array.
"""
def handleRotation1(arr, rot, max_orig):
    if(rot > max_orig):
        return max_orig - (rot % len(arr));

    else:
        return max_orig - rot;


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
print("Value: ", -13 % 5)
print getMaxElementIndices([1, 2, 4, 3], [0, 2, 3, 4])
#print getMaxElementIndices([1, 2, 3, 4], [1, 2, 4])
print getMaxElementIndices([1, 2, 4, 3], [1, 3])
print getMaxElementIndices([1, 5, 6, 8, 3, 7, 2], [0, 1, 3, 5])
print "Now"
print getMaxElementIndices([5, 6, 2, 8, 1], [0, 1, 3, 4, 5])

print "Other code"
def getMaxElementIndicesT(arr, rot):
  idx = arr.index(max(arr))
  ans=[]
  for r in rot:
    r = r % len(arr)
    if idx-r<0:
      ans.append(len(arr)-abs(idx))
    else:
      ans.append(idx-r)
  return ans
print getMaxElementIndicesT([1, 5, 6, 2, 3, 7, 8], [0, 1, 3, 5, 100, 2])