"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.p_val = []
        self.q_val = []

    def p_nodes(self, p):
        if p is None:
            self.p_val.append(None)
            return
        self.p_val.append(p.val)
        self.p_nodes(p.left)
        self.p_nodes(p.right)

    def q_nodes(self, q):
        if q is None:
            self.q_val.append(None)
            return
        self.q_val.append(q.val)
        self.q_nodes(q.left)
        self.q_nodes(q.right)

    def isSameTree(self, p, q):
        self.q_nodes(q)
        self.p_nodes(p)
        if self.q_val == self.p_val:
            return True
        return False
