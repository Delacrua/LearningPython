"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value does
not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree
remains a BST after insertion. You can return any of them.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        node = root

        while node:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right

        return root
