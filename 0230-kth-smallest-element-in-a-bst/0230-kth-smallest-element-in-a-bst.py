class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        cur = root

        while True:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1

            if k == 0:
                return cur.val

            cur = cur.right