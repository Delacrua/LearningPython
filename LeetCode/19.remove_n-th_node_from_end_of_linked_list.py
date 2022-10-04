"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        temp = ListNode(-1, next=head)
        current = temp

        while current:
            nodes.append(current)
            current = current.next

        nodes[-(n + 1)].next = nodes[-n].next
        return temp.next
