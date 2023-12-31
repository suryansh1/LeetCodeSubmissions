from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None : return head

        stack = deque()

        temp = head

        while temp is not None :

            stack.append(temp)
            temp = temp.next

        retHead = stack[-1]

        temp = stack.pop()

        while(stack):

            temp.next = stack[-1]

            temp = stack.pop()

        temp.next = None
        
        return retHead