# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #  Initialize a dummy node
        dummy = ListNode(0)
        # Initialize a pointer to the dummy node
        current = dummy

        # compare the values of the node in the two lists and append the smaller one of the result
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append the remaining nodes to the result
        if l1:
            current.next = l1
        else:
            current.next = l2
        
        # Return the result without the dummy node
        return dummy.next