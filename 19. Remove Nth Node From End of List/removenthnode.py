# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #  Create two pointers, one fast and one slow
        slow = fast = head
        # Move the fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
        # If the fast pointer is None, then remove the head node
        if not fast:
            return head.next
        # Move both pointers until the fast pointer reaches the end
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        # Remove the Nth node by changing the next pointer of the (N-1)th node
        prev.next = slow.next
        return head