# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None or (root.left is None and root.right is None) : return root
                
        leftSubtree = self.invertTree(root.left)

        rightSubtree = self.invertTree(root.right)

        root.left, root.right = rightSubtree, leftSubtree

        return root
