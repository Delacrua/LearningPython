"""
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        nrows = len(coins) + 1
        ncols = amount + 1

        result = [[float('inf') for _ in range(ncols)] for _ in range(nrows)]

        for row in range(nrows):
            result[row][0] = 0

        for row in range(1, nrows):
            for col in range(1, ncols):
                if col < coins[row - 1]:
                    result[row][col] = result[row - 1][col]
                else:
                    result[row][col] = min(1 + result[row][col - coins[row - 1]], result[row - 1][col])

        return -1 if result[-1][-1] == float('inf') else result[-1][-1]
