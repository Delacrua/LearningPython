"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values
along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only
from parent nodes to child nodes).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    count = 0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, targetSum)
        return self.count

    def dfs(self, root, targetSum, count):
        if root.val == targetSum:
            self.count += 1
        if root.left:
            self.dfs(root.left, targetSum - root.val, self.count)
        if root.right:
            self.dfs(root.right, targetSum - root.val, self.count)

    def helper(self, root, targetSum):
        if not root:
            return
        self.dfs(root, targetSum, self.count)
        self.helper(root.left, targetSum)
        self.helper(root.right, targetSum)
