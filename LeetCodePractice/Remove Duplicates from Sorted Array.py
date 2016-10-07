
"""
26. Remove Duplicates from Sorted Array
"""
def removeDuplicates(nums):
    N = len(nums)
    i = 1;
    start = 0;
    while(i < N):
        if (nums[i] == nums[i-1]):
            i = i + 1
            continue
        else:
            nums[start + 1] = nums[i]
            start = start + 1;
            i = i + 1
    #print "Nums just before returning : ", nums
    return nums[0:start+1]

if __name__ == "__main__":
    nums = [1, 1, 2, 3, 4, 5 , 6, 6, 7, 7, 8]
    result = removeDuplicates(nums);
    print len(result)
    #print "After Actual result : ", nums