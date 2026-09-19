class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        k %= n

        if k == 0:
            return head

        # Make it circular
        tail.next = head

        # Find new tail
        steps = n - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head