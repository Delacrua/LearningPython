"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def _make_permute(seq):
            if not seq:
                yield seq  # Empty sequence
            else:
                for i in range(len(seq)):
                    rest = seq[:i] + seq[i + 1:]  # Delete current node
                    for x in _make_permute(rest):  # Permute the others
                        yield seq[i:i + 1] + x

        return list(_make_permute(nums))
