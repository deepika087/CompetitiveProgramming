__author__ = 'deepika'


class Solution:

    def generateSubsets(self, nums):

        result = set()

        for i in range(len(nums)):
            current_path = ""
            self.generateSubsetUtil(i, current_path, result, nums)
        return result

    def generateSubsetUtil(self, i, current_path, result, nums):

        #print(current_path)
        result.add(current_path)
        if i >= len(nums):
            return


        self.generateSubsetUtil(i + 1, current_path + str(nums[i]), result, nums)
        self.generateSubsetUtil(i + 1, current_path, result, nums)

s=Solution()
print(s.generateSubsets([1, 2, 3, 4]))
