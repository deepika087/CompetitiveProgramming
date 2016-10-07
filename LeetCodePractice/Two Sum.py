

"""
1. Two Sum
Tried two approaches. One works for only positive integer. other works for both positive and negative
"""
def twoSum2(nums, target):

    hashT = dict();
    for i in range(len(nums)):
        item = nums[i]
        if (hashT.get(target - item, -1) != -1):
            return hashT.get(target - item), i
        else:
            hashT[item] = i
            #print hashT

#The solution below will only work for positive integer. If it is a mix of both positive and negative this will fail
def twoSum(nums, target):

    hash = [-1 for i in range(max(max(nums), target)+1)];
    for i in range(len(nums)):
        item = nums[i]
        if (target - item >= 0):
            if (hash[target - item] != -1): # Element already seen
                return hash[target - item], i
            else:
                hash[item] = i

if __name__=="__main__":
    nums = raw_input('')
    nums = nums.replace(',', ' ').split();
    nums = [int(x) for x in nums]
    target = int(raw_input(''))
    print twoSum2(nums, target)

