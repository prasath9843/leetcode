import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Min-heap to store (node value, index, node)
        heap = []
        
        # Push the head of each linked list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Dummy head for result linked list
        dummy = ListNode(0)
        curr = dummy
        
        # Process heap until empty
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
