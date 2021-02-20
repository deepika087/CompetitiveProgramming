__author__ = 'deepika'


def coinDenomination(coins, target, index, result):
    if target == 0:
        print result
        return 1

    running_sum = 0
    for i in range(index, len(coins)):
        if target - coins[i] >= 0:
            running_sum += coinDenomination(coins, target - coins[i], i, result + str(coins[i]))
    return running_sum

#res = coinDenomination([1, 2, 3], 5, 0, "")
#print "Number of ways: ", res


class Solution:

    def coinDenomination(self, coins, target):

        running_sum = 0
        index = 0
        combination_so_far = ""

        self.coinDenominationUtil(index, running_sum, coins, target, combination_so_far)

    def coinDenominationUtil(self, index, running_sum, coins, target, combination_so_far):

        if index >= len(coins):
            return

        if running_sum > target:
            return

        if running_sum == target:
            print(combination_so_far)
            return #If you don't add return here. It will result in duplicate results.

        self.coinDenominationUtil(index, running_sum + coins[index], coins, target,  combination_so_far + "," + str(coins[index]))
        self.coinDenominationUtil(index + 1, running_sum, coins, target, combination_so_far)

s=Solution()
s.coinDenomination([4, 6, 11], 31)
s.coinDenomination([4, 6, 11], 9)
s.coinDenomination([1, 2, 3], 5)