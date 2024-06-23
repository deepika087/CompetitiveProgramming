from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        all_results = []
        self.dfs(num, 0, target, "", all_results)
        return all_results

    def dfs(self, nums, i, target, path_so_far, all_results):
        if i >= len(nums):
            return
        path_so_far += str(nums[i])

        if i == len(nums) - 1:
            print(path_so_far)

            if not path_so_far.startswith('0') and \
                    not path_so_far.find('/0') >= 0 and \
                    eval(path_so_far) == target:
                all_results.append(path_so_far)
        else:
            for operator in ['+', '-', '*', '/']:
                self.dfs(nums, i + 1, target, path_so_far + operator, all_results)
                self.dfs(nums, i + 1, target, path_so_far, all_results)

# Example usage


s = Solution()
#print(s.addOperators("123", 6))
#print(s.addOperators("232", 8))
#print(s.addOperators("3456237490", 9191))
print(s.addOperators("125", 7))
print("done")
