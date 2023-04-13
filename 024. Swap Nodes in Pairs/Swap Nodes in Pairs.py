# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If the list has 0 or 1 nodes, return the head
        if not head or not head.next:
            return head

        # Set up pointer for the first two nodes
        prev = None
        curr = head
        nxt = head.next

        # Update the head to the second node
        new_head = nxt

        # Lopp through the list and swap pairs of nodes
        while curr and nxt:
            # Update the pointers for the next iteration
            if prev:
                prev.next = nxt
            curr.next = nxt.next
            nxt.next = curr

            # update pointers for the next pairs of nodes
            prev = curr
            curr = curr.next
            if curr:
                nxt = curr.next

        return new_head
