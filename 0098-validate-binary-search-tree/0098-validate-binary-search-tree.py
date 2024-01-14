# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def validateRecursively(self, root: TreeNode, lowerBound: int, upperBound: int) -> bool:

        if root is None : return True

        if root.val <= lowerBound or root.val >= upperBound : return False

        # if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val) : return False

        return self.validateRecursively(root.left, lowerBound, root.val) and self.validateRecursively(root.right, root.val, upperBound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None : return True

        return self.validateRecursively(root, -math.inf, math.inf)

        # if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val) : return False

        # return self.isValidBST(root.left) and self.isValidBST(root.right)