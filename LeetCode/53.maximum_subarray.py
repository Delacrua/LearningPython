"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = nums[0]
        current_sum = 0
        for i in nums:
            if (current_sum < 0):
                current_sum = 0
            current_sum += i
            max_subarray_sum = max(max_subarray_sum, current_sum)
        return max_subarray_sum
