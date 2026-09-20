class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.pushLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0