# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder (self, root: Optional[TreeNode], return_list : [int]):

        if not root :

            return

        return_list.append(root.val)

        self.preorder(root.left, return_list)

        self.preorder(root.right, return_list)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root : return None

        return_list = []

        self.preorder(root, return_list)

        return return_list