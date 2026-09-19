class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def check(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)