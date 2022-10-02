"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = cur_new = ListNode(val='head')

        while list1 and list2:
            if list1.val <= list2.val:
                cur_new.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                cur_new.next = ListNode(val=list2.val)
                list2 = list2.next
            cur_new = cur_new.next

        while list1 or list2:
            if list1:
                cur_new.next = ListNode(val=list1.val)
                list1 = list1.next
            if list2:
                cur_new.next = ListNode(val=list2.val)
                list2 = list2.next
            cur_new = cur_new.next

        return new_head.next
