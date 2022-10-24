"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return
the result in any order.
"""
import collections  # Not needed on LeetCode
from typing import List  # Not needed on LeetCode


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_freq = collections.Counter(nums1)
        result = []
        for item in nums2:
            if item in nums1_freq and nums1_freq[item] > 0:
                    result.append(item)
                    nums1_freq[item] -= 1
        return result
