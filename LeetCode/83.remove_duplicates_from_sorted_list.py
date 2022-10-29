"""
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
"""


# Definition for singly-linked list.
from typing import Optional  # Not needed on LeetCode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr is not None and curr.next is not None:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
