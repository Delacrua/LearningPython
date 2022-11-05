"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
            else:
                res.remove(i)
        return list(res)[-1]
