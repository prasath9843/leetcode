class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev    