# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        

        stack = deque()

        stack.append(cloned)

        while stack :

            cur = stack.pop()

            if cur.val == target.val : return cur

            if cur.left : stack.append(cur.left)

            if cur.right : stack.append(cur.right)

        return None

        