# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTreeBFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None : return True

        if (p is None and q is not None) or (p is not None and q is None):

            return False

        queue = deque()

        queue.append(p)

        queue.append(q)
        
        while (queue):

            pNode = queue.popleft()

            qNode = queue.popleft()

            if (pNode is None and qNode is not None) or (pNode is not None and qNode is None): return False

            if pNode is None and qNode is None : 
                continue

            if pNode.val != qNode.val : return False

            queue.append(pNode.left)

            queue.append(qNode.left)

            queue.append(pNode.right)

            queue.append(qNode.right)


        return True

    def isSameTreeDFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        if not p and not q : return True

        if (p and not q) or (q and not p) : return False

        stack = deque()

        stack.append(p)

        stack.append(q)

        while stack :

            qNode = stack.pop()

            pNode = stack.pop()

            if pNode and not qNode or qNode and not pNode : return False

            if not pNode and not qNode : continue

            if pNode.val != qNode.val : return False

            stack.append(pNode.left)

            stack.append(qNode.left)

            stack.append(pNode.right)

            stack.append(qNode.right)

        return True


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # return self.isSameTreeDFS(p,q)
        
        return self.isSameTreeBFS(p,q)

        # if p is None and q is None : return True

        # if (p is None and q is not None) or (p is not None and q is None):

        #     return False

        # if p.val == q.val :

        #     if p.left is None and q.left is None and p.right is None and q.right is None : return True

        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # return False