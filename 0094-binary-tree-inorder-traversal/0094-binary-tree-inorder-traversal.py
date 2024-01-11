# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    return_answer = []


    def inorderTraversalRecursive(self, root: Optional[TreeNode], answer_list : list[int]):

        if root is None : return

        self.inorderTraversalRecursive(root.left, answer_list)

        # self.return_answer.append(root.val)

        answer_list.append(root.val)

        # print(root.val, self.return_answer)

        self.inorderTraversalRecursive(root.right, answer_list)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None : return []

        # print(self.return_answer)

        answer_list = []
        
        self.inorderTraversalRecursive(root, answer_list)

        # return self.return_answer

        return answer_list