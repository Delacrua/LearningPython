"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        if not root:
            return result

        stack = [root]

        while stack:
            level = []

            result.append(stack[-1].val)

            for node in stack:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            stack = level

        return result
