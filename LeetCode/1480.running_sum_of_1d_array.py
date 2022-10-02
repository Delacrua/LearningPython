"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int] a list of integers where 1 <= nums.length <= 1000
        :rtype: List[int] a list of running sum of integers
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums
