class Solution(object):

    def merge_linked_lists(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.val <= right.val:
            merged = left
            merged.next = self.merge_linked_lists(left.next, right)
        else:
            merged = right
            merged.next = self.merge_linked_lists(left, right.next)

        return merged

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def _get_middle(head_node):
            """
            helper function to get middle of linked list
            :param head_node:
            :return:
            """
            slow = head_node
            fast = head_node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if head is None or head.next is None:
            return head
        middle = _get_middle(head)
        right_half_head = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(right_half_head)
        result = self.merge_linked_lists(left, right)

        return result




