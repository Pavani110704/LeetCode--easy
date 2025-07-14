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

        if head is None or head.next is None:
            return True

        # Step 1: Find the middle using slow/fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare first half and reversed second half
        first = head
        second = prev  # Head of reversed second half
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
