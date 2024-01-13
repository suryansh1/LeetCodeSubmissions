# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def computePathSum(self, root: Optional[TreeNode], curSum: int, targetSum: int) -> bool:
        '''This works if path from root to any node sums up to targetSum, not just leaf node like the question asked'''

        # The problem doesn't consider [1,2] as reaching sum 1, as root.val==1
        # but path from root to leaf == 3

        if root is None : return False

        if curSum + root.val == targetSum : return True

        return self.computePathSum(root.left, curSum + root.val, targetSum) or self.computePathSum(root.right, curSum + root.val, targetSum)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None : return False

        targetSum -= root.val

        if not root.left and not root.right and targetSum == 0 : return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        # return self.computePathSum(root, 0, targetSum)
        