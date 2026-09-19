class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur = root

        while cur:
            dummy = Node(0)
            tail = dummy

            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right:
                    tail.next = cur.right
                    tail = tail.next

                cur = cur.next

            cur = dummy.next

        return root