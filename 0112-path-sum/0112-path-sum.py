class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: empty tree
        if not root:
            return False
        
        # If it's a leaf node, check the sum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur for left and right subtree
        remaining_sum = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_sum) or
                self.hasPathSum(root.right, remaining_sum))
