class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (len(numbers) == 1):
            result.append(0)
            result.append(0)
            return result
        left=0
        right=len(numbers)-1
        while(left < right):
            if (numbers[left] + numbers[right] == target):
                result =[]
                result.append(left + 1)
                result.append(right + 1)
                return result
            if (numbers[left] + numbers[right] < target):
                left = left + 1
            else:
                right = right - 1
        result.append(0)
        result.append(0)
        return result

s=Solution()
print s.twoSum([2, 7, 11, 15], target=9)
