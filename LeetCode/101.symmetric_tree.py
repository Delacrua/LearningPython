"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True

            elif not left or not right:
                return False

            elif left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)

            return False

        return dfs(root.left, root.right)
