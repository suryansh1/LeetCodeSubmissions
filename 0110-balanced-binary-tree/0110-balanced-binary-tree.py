# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkHeight(self, root: Optional[TreeNode]) -> int:

        if root is None : return 0

        return 1 + max(self.checkHeight(root.left), self.checkHeight(root.right))

    def checkBalancedRecursive(self, root: Optional[TreeNode]) -> bool:

        if root is None : return True

        if abs(self.checkHeight(root.left) - self.checkHeight(root.right)) > 1 : return False

        return self.checkBalancedRecursive(root.left) and self.checkBalancedRecursive(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.checkBalancedRecursive(root)



        
        