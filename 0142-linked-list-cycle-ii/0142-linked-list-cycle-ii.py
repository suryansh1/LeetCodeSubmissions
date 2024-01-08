# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycleDict(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None : return None

        seenNodes = set()

        temp = head

        while temp :

            if temp in seenNodes : return temp
                
            else : seenNodes.add(temp)

            temp = temp.next

        return None

    def detectCycleNoDict(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return head

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.detectCycleDict(head)