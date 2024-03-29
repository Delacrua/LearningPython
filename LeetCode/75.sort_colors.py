"""
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)
        i = 0
        while i < end:
            num = nums[i]
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                end -= 1
            elif nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            else:
                i += 1
