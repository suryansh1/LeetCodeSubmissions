# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def hasCycleFloyd(self, head: Optional [ListNode]) -> bool :

        slow = fast = head 

        while fast and fast.next :

            slow = slow.next

            fast = fast.next.next

            if slow == fast : return True

        return False

 
    def hasCycleDict(self, head: Optional[ListNode]) -> bool:
        
        seenNodes = set()

        temp = head

        while temp :

            if temp in seenNodes : return True

            seenNodes.add(temp)

            temp = temp.next

        return False
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        return self.hasCycleDict(head)

        # return self.hasCycleFloyd(head)

        
    