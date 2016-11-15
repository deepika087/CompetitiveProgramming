"""
Incomplete but will be solved something like http://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/
"""
class Solution(object):

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #return self.find132patternUtil(nums, 0, len(nums)-1)
        smallest = [-1 for i in range(len(nums))]
        greatest = [-1 for i in range(len(nums))]
        min_so_far = 0
        max_so_far = len(nums) - 1
        for i in range(1, len(nums)):
            if (nums[i] < nums[min_so_far]):
                min_so_far = i
                smallest[i] = -1
            elif(nums[i] == nums[min_so_far]):
                smallest[i] = -1
            else:
                smallest[i] = min_so_far
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < nums[max_so_far]):
                max_so_far = i
                greatest[i] = -1
            elif(nums[i] == nums[max_so_far]):
                greatest[i] = -1
            else:
                greatest[i] = max_so_far
        print "Smallest = ", smallest, " greatest = ", greatest
        for i in range(len(nums)):
            min_so_far = smallest[i]
            max_so_far = greatest[i]
            if ( min_so_far != -1 and max_so_far != -1 and min_so_far != max_so_far and i < min_so_far < max_so_far):
                #print nums[min_so_far] , nums[i], nums[max_so_far]
                return True
        #print "Smallest = ", smallest, " greatest = ", greatest
        return False



s=Solution()
print s.find132pattern([1,0,1,-4,-3]) #Expected : False
print s.find132pattern([2,4,1,3])

print s.find132pattern([-2,1,2,-2,1,2])
print s.find132pattern([1,0,1,-4,-3])
print s.find132pattern([1, 2, 3, 4])
print s.find132pattern([3, 1, 4, 2])
print s.find132pattern([-1, 3, 2, 0])

"""
 def bruteForce(self, nums):
        i=1;
        while(i < len(nums) and i + 1 < len(nums)):
            if (nums[i-1] < nums[i+1] <nums[i]):
                #print "Triplet : ", nums[i-1] , nums[i+1] , nums[i]
                break;

            i = i + 1
"""