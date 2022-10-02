"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ans = [0 for _ in range(n + 1)]
        ans[1], ans[2] = 1, 2
        for i in range(3, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[n]

