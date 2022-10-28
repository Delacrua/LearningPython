"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.
"""
from typing import Optional  # Not needed on LeetCode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = curr = ListNode(next=head)
        while curr is not None and curr.next is not None:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return temp.next

