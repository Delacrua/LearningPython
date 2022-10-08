"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    diameter = 0

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left + right > self.diameter:
            self.diameter = left + right
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.height(root)
        return self.diameter
