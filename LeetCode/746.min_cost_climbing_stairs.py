"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost_1, min_cost_2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            current = cost[i] + min(min_cost_1, min_cost_2)
            min_cost_1 = min_cost_2
            min_cost_2 = current

        return min(min_cost_1, min_cost_2)

