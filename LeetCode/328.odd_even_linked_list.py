"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        odd_head, curr_odd = head, head
        even_head, curr_even = head.next, head.next

        while curr_odd.next is not None and curr_even.next is not None:
            curr_odd.next = curr_even.next
            curr_even.next = curr_even.next.next

            curr_odd = curr_odd.next
            curr_even = curr_even.next

        curr_odd.next = even_head
        return odd_head
