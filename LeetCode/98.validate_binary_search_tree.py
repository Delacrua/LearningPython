"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root, border_left=float("-inf"), border_right=float("inf")):
        if not root:
            return True
        if root.val <= border_left or root.val >= border_right:
            return False
        return self.isValidBST(root.left, border_left, root.val) and self.isValidBST(root.right, root.val, border_right)
