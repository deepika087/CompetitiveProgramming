__author__ = 'deepika'

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) in [0, 1]:
            return  True

        seen = False if nums[0] <= nums[1] else True

        for i in range(1, len(nums) - 1):
            if i + 1 < len(nums) and nums[i] <= nums[i + 1]:
                continue
            else:
                if seen:
                    return False
                else:
                    seen = True
                    if i + 1 == len(nums) - 1:
                        continue
                    if nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i - 1] # this fix works
                        continue
                    else:
                        if i + 2 < len(nums) and nums[i] <= nums [i + 2]:
                            nums[i] = nums[i + 2]
                            continue
                        else:
                            return False
        return True

s=Solution()
assert s.checkPossibility([4,2,3]) == True
assert s.checkPossibility([4,2,1]) == False
assert s.checkPossibility([-1,4,2,3]) == True
assert s.checkPossibility([3,4,2,3]) == False
assert s.checkPossibility([2,3,3,2,4]) == True
assert s.checkPossibility([1,2,4,5,3]) == True