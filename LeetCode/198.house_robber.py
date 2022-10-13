"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        house_number = len(nums)
        if house_number == 1:
            return nums[0]
        elif house_number == 2:
            return max(nums[0], nums[1])
        elif house_number == 3:
            return max(nums[1], nums[0] + nums[2])

        result = [0] * house_number
        result[0], result[1], result[2] = nums[0], nums[1], nums[0] + nums[2]

        for i in range(3, house_number):
            result[i] = nums[i] + max(result[i - 2], result[i - 3])

        return max(result[-1], result[-2])
