"""
Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        result = []

        def _dfs(node, targetSum):
            if node:
                if not node.left and not node.right:
                    if node.val == targetSum:
                        result.append(True)
                else:
                    if node.left:
                        _dfs(node.left, targetSum - node.val)
                    if node.right:
                        _dfs(node.right, targetSum - node.val)

        _dfs(root, targetSum)

        return any(result)
