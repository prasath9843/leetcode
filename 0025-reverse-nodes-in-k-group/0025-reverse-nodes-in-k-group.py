class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            end = prev

            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next

            curr = prev.next
            nxt = curr.next

            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next

            prev = curr