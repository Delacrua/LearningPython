"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        major_element = None
        for num in nums:
            if count == 0:
                major_element = num
            count += 1 if major_element == num else -1
        return major_element