class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val

                while cur and cur.val == val:
                    cur = cur.next

                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next