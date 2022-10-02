"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int] a list of prices
        :rtype: int best difference between sell and buy prices
        """
        max_difference = 0
        buy_index = 0
        sell_index = 1

        while buy_index < len(prices) and sell_index < len(prices):
            if prices[sell_index] > prices[buy_index]:
                max_difference = max(max_difference, prices[sell_index] - prices[buy_index])
            else:
                buy_index = sell_index
            sell_index += 1

        return max_difference
