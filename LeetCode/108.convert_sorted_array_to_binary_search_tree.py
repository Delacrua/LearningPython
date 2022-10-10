"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.make_bst(nums, 0, len(nums))

    def make_bst(self, nums, start, end):
        if start >= end:
            return None
        return TreeNode(
            nums[(start + end) // 2],
            left=self.make_bst(nums, start, (start + end) // 2),
            right=self.make_bst(nums, 1 + ((start + end) // 2), end)
        )
