"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if nums[middle] >= nums[left]:  # checking if the left of middle element is the sorted sub-array
                if nums[left] <= target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            else:  # else the right part of middle element will be the sorted subarray
                if nums[middle] <= target <= nums[right]:
                    left = middle
                else:
                    right = middle - 1

        return left if nums[left] == target else -1
