"""
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""


class Solution:
    def threeSumClosest(self, nums, target):

        result = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)

        for index, num in enumerate(nums):
            left, right = index + 1, len(nums) - 1

            while left < right:
                current_sum = num + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                elif abs(target - current_sum) < abs(target - result):
                    result = current_sum
                elif current_sum > target:
                    right -= 1
                else:
                    left += 1

        return result
