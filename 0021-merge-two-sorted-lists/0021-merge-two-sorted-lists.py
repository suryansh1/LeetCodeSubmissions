# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if list1 is None : return list2

        if list2 is None : return list1

        # Two ways

        # 1. With extra space O(n)
            # create a new list 
            # traverse the lists
            # Add elements from both lists to new list
            # return New List

        # 2. Without extra space

            # Traverse both lists using temp1 and temp2 pointers

            # Update next pointers accordingly

        temp1, temp2 = list1, list2

        # retHead = list1 if temp1.val <= temp2.val else list2

        retHead = ListNode(-1)

        cur = retHead

        while temp1 and temp2 :

            if temp1.val <= temp2.val :
                
                cur.next = temp1
                temp1 = temp1.next
                

            else :

                cur.next = temp2
                temp2 = temp2.next
 
            cur = cur.next

        if temp1 is None : cur.next = temp2

        elif temp2 is None : cur.next = temp1


        return retHead.next



        



            
                
                   

             


            # Return head of merged list
