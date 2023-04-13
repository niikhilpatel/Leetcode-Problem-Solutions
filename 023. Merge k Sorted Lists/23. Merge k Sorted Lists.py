# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # create a min heap and push the head nodes of all lists
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        # Create a dummy nodes and a pointer to it
        dummy = ListNode(0)
        ptr = dummy

        # Iterate while the heap is not empty
        while heap:
            # pop the smallest node from the heap
            val, i, node = heapq.heappop(heap)

            # Add the node to the final merge list
            ptr.next = node
            ptr = ptr.next

            #  Add the next node from the same list to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Retur the merge list
        return dummy.next