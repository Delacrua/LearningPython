"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a continuous subsequence of the array.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]

        product = 1
        for num in nums:
            product *= num
            max_product = max(max_product, product)
            if product == 0:
                product = 1

        product = 1
        for num in reversed(nums):
            product *= num
            max_product = max(max_product, product)
            if product == 0:
                product = 1

        return max_product
