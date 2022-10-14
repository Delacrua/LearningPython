"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned
into two subsets such that the sum of elements in both subsets is equal.
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        variants = {0}

        for i in range(len(nums)):
            variants_copy = variants.copy()
            for variant in variants_copy:
                if variant + nums[i] == target:
                    return True
                variants.add(variant + nums[i])

        return target in variants
