"""
Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_count = {0: 1}
        temp_sum = 0
        result = 0
        for i in range(len(nums)):
            temp_sum += nums[i]
            if temp_sum - k in freq_count:
                result += freq_count[temp_sum - k]

            if temp_sum in freq_count:
                freq_count[temp_sum] += 1
            else:
                freq_count[temp_sum] = 1

        return result
