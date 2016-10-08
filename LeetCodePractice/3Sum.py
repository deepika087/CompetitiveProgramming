
"""
15. 3Sum
"""
import copy

def twoSum2(nums, target):

    hashT = dict();
    result = []
    for i in range(len(nums)):
        item = nums[i]
        if (hashT.get(target - item, -1) != -1):
            result.append((nums[hashT.get(target - item)], nums[i]))
        else:
            hashT[item] = i
    return result

"""
Solution 1 : use O(n) solution to find 2 sum given -c as target
For every element it does n processing
So, complexity is n^2
"""
def threeSum(nums):
    finalResult = []
    backup_nums = copy.copy(nums)
    for target in nums:
        backup_nums.remove(target)
        #print " After first removal backup_nums = ", backup_nums
        results = twoSum2(backup_nums, -target)
        #print " For target = ", target, "result = ", results
        for result in results:
            list_temp = []
            list_temp.append(result[0])
            list_temp.append(result[1])
            list_temp.append(target)
            list_temp = sorted(list_temp)
            if (list_temp not in finalResult):
                finalResult.append(list_temp)
        backup_nums = copy.copy(nums)
        #print " After final removal backup_nums = ", backup_nums
    return sorted(finalResult)

"""
This sorts array O(nlogn)
For every i, goes from i+1 to len(nums) - 1
And find triplet.
So complexity is O(nlogn) + not exactly n^2, complexity less than that
"""
def threeSum2(nums):
    nums = sorted(nums)
    #nums = list(set(nums))
    finalResult = []

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while( left < right):
            total = nums[i] + nums[left] + nums[right]

            if ( total == 0 and sorted([nums[left], nums[i], nums[right]]) not in finalResult):
                finalResult.append(sorted([nums[left], nums[i], nums[right]]))
                left = left + 1
                right = right - 1;
            elif (total > 0):
                right = right - 1;
            else:
                left = left + 1
    return sorted(finalResult)

if __name__ =="__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print threeSum2(nums)