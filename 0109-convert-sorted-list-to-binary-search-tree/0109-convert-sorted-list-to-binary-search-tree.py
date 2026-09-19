class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root