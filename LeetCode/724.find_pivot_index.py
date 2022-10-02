"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int] a list of integers  1 <= len(nums) <= 10**4
        :rtype: int an index of pivot element
        """
        left_sum = 0
        right_sum = sum(nums[1:])
        length = len(nums)
        for i in range(length):
            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]
                if i != length - 1:
                    right_sum -= nums[i + 1]
        return -1
