"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = []
        current = head
        while current:
            nodes.append(current.val)
            current = current.next
        return nodes == nodes[::-1]

    class Solution2(object):
        def isPalindrome_on_o1(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            def reverse(node):
                prev = None
                while node:
                    next_node = node.next
                    node.next = prev
                    prev, node = node, next_node

                return prev

            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            n1 = head
            n2 = reverse(slow.next)
            while n2:
                if n1.val != n2.val:
                    return False

                n1 = n1.next
                n2 = n2.next

            return True
