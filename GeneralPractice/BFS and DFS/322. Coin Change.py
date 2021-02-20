__author__ = 'deepika'


"""
TLE need to use memoization in order to speed it up

int coinChange(vector<int>& coins, int amount) {
        vector<int> min(amount+1,INT_MAX);
        min[0]=0;
        for(int i=1;i<=amount;i++)
        {
            for(int j=0;j<coins.size();j++)
            {
                if(coins[j]<=i)
                {
                    if(min[i-coins[j]]!=INT_MAX && min[i-coins[j]]+1<min[i])
                        min[i]=min[i-coins[j]]+1;
                }
            }
        }
        if(min[amount]==INT_MAX)
            return -1;
        return min[amount];
    }

"""
import sys
class Solution(object):


    def coinChangeAmazon(self, denominations, amount):

        if len(denominations) == 0:
            return 0

        if amount == 0:
            return 0

        def coinChangeUtil(denominations, amount, current_amount, current_coins):


            if current_amount > amount:
                return

            for i in range(len(denominations)):
                pass







    numCoins = sys.maxint

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if len(coins) == 0:
            return 0

        if amount == 0:
            return 0

        for coin in range(len(coins)):
            self.startDFS(coin, coins, amount, coins[coin], 1)

        save = self.numCoins
        self.numCoins = sys.maxint
        return save if save != sys.maxint else -1

    def startDFS(self, i, coins, amount, amount_so_far, num_of_coins):

        if i < 0 or i >= len(coins):
            return

        if amount_so_far == amount:
            self.numCoins = min(self.numCoins, num_of_coins)

        if amount_so_far > amount:
            return

        for j in range(len(coins)):
            self.startDFS(j, coins, amount, amount_so_far + coins[j], num_of_coins + 1)

s=Solution()
print(s.coinChange(coins = [1, 2, 5], amount = 11))
print(s.coinChange(coins = [2], amount = 3))