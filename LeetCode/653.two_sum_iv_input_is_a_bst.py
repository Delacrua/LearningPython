"""
Given the root of a Binary Search Tree and a target number k, return true if there
exist two elements in the BST such that their sum is equal to the given target.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        
        def _dfs(node):
            if node:
                if k - node.val in visited:
                    return True
                visited.add(node.val)
                return _dfs(node.left) or _dfs(node.right)

        return _dfs(root)
    