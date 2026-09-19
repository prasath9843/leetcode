class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small = ListNode(0)
        large = ListNode(0)

        s = small
        l = large

        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                l.next = head
                l = l.next

            head = head.next

        l.next = None
        s.next = large.next

        return small.next