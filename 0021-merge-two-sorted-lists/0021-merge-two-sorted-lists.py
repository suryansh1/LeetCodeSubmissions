# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None : return list2

        if list2 == None : return list1

        temp1, temp2 = list1, list2

        prehead = ListNode(-1)

        prev = prehead
        
        while (temp1 is not None) and (temp2 is not None) :

            if temp1.val <= temp2.val :                
          
                prev.next = temp1
                temp1 = temp1.next
            
            else :

                prev.next = temp2
                temp2 = temp2.next

            prev = prev.next
            
        prev.next = temp1 if temp1 is not None else temp2

        return prehead.next