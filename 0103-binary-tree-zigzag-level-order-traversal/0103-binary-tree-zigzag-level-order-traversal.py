class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        left = True

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left:
                level.reverse()

            res.append(level)
            left = not left

        return res