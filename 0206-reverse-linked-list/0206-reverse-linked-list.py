from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseListStack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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


    def reverseListPreCurNext(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None : return head

        pre = None
        cur = head
        next = head.next

        while cur.next :

            cur.next = pre
            pre = cur
            cur = next            
            next = next.next 

        cur.next = pre
        return cur






    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # return self.reverseListStack(head)

        return self.reverseListPreCurNext(head)