# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversalRecursive(self, root: Optional[TreeNode], answer_list : list[int]):

        if root is None : return

        self.inorderTraversalRecursive(root.left, answer_list)

        answer_list.append(root.val)

        self.inorderTraversalRecursive(root.right, answer_list)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None : return []

        answer_list = []
        
        self.inorderTraversalRecursive(root, answer_list)

        return answer_list