"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = prev_node = None
        while head is not None:
            curr_node = head
            head = head.next
            curr_node.next = prev_node
            prev_node = curr_node
        return curr_node
