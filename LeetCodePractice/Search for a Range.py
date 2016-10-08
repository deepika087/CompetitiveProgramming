
"""
34. Search for a Range
"""
def firstOccurance(nums , target, left, right):
    if (left > right):
        return -1;

    mid = left + (right - left)/2
    #mid is such that prev element is less than it or mid == 0
    if ((mid == 0 and nums[mid] == target) or (nums[mid - 1] < nums[mid] and nums[mid] == target)):
        return mid
    elif (nums[mid] < target): #First occurence is on the left
        return firstOccurance(nums, target, mid + 1, right)
    else:
        return firstOccurance(nums, target, left, mid - 1)

def lastOccurance(nums, target, left, right):
    if (left > right):
        return -1;
    mid = left + (right - left)/2
    if (mid < 0):
        return -1;
    if ( (mid == right and nums[mid] == target)  or (mid + 1 < len(nums) and nums[mid + 1] > nums[mid] and nums[mid] == target)):
        return mid
    elif (nums[mid] == target or nums[mid] < target):
        return lastOccurance(nums, target, mid + 1, right)
    else:
        return lastOccurance(nums, target, left, mid - 1)

def searchRange(nums, target):
    if target not in nums:
        return (-1, -1)
    fo = firstOccurance(nums, target, 0, len(nums) - 1)
    lo = lastOccurance(nums, target, 0, len(nums) - 1)
    return (fo, lo)

if __name__ =="__main__":
    nums = [1, 2, 3]
    target = 1
    print searchRange(nums, target)

    nums = [2,2]
    target = 1
    print searchRange(nums, target)

    nums = [1]
    target = 0
    print searchRange(nums, target)

    nums= [5, 7, 7, 7, 7, 7, 8, 8, 8, 10]
    target = 8
    print searchRange(nums, target)

    nums = [5, 7, 8, 8, 8, 8, 8 ,8 , 9]
    print searchRange(nums, target)

