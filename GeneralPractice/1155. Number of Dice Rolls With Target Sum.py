__author__ = 'deepika'

"""
Adding dp will be the right way
dp[d + 1][target + 1]
if i = 0 no matter what the target it that will also be 0


def numRollsToTarget(self, d, f, target):
        count = 0
        dp_table = [[-1 for _ in range(target+1)] for _ in range(d+1)]
        dp_table[0][0] = 1
        for c in range(1, target+1):
            dp_table[0][c] = 0
        def recur(die, target): I think we should also check if die > 0
            if dp_table[die][target] != -1:
                return dp_table[die][target]
            total_ways = 0
            for i in range(1, f+1):
                if target-i >= 0:
                    total_ways += recur(die-1, target-i)
            dp_table[die][target] = total_ways
            return dp_table[die][target]
        recur(d, target)
        return dp_table[d][target] % (10**9+7)

"""

class Solution(object):

    total_ways = 0

    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """

        current_sum = 0
        current_face = []
        current_die = 0
        self.numRollsToTargetUtil(d, f, target, current_face, current_sum, current_die)

        return self.total_ways

    def numRollsToTargetUtil(self, d, f, target, current_face, current_sum, current_die):

        #print(current_face)
        if current_sum > target:
            return

        if current_die > d:
            return
        if current_die == d and current_sum == target:
            print(current_face)

        for j in range(1, f+1):
            current_face.append(j)
            self.numRollsToTargetUtil(d, f, target, current_face, current_sum + j, current_die + 1)
            current_face.pop(-1)


s=Solution()
print("Test Case 1")
print(s.numRollsToTarget(1, 6, 3))
print("Test case 2")
print(s.numRollsToTarget(2, 6, 7))
print("Test case 3")
print(s.numRollsToTarget(3, 6, 10))