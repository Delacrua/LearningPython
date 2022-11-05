"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()

        negatives, positives, zeroes = [], [], []
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeroes.append(num)

        neg_set, pos_set = set(negatives), set(positives)

        if zeroes:
            for num in pos_set:
                if -1 * num in neg_set:
                    result.add((-1 * num, 0, num))

        if len(zeroes) >= 3:
            result.add((0, 0, 0))

        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                target = -1 * (negatives[i] + negatives[j])
                if target in pos_set:
                    result.add(tuple(sorted([negatives[i], negatives[j], target])))

        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = -1 * (positives[i] + positives[j])
                if target in neg_set:
                    result.add(tuple(sorted([positives[i], positives[j], target])))

        return result
