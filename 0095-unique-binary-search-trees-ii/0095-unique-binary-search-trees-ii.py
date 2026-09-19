class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def build(left, right):
            if left > right:
                return [None]

            res = []

            for root in range(left, right + 1):
                left_trees = build(left, root - 1)
                right_trees = build(root + 1, right)

                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        res.append(node)

            return res

        return build(1, n)