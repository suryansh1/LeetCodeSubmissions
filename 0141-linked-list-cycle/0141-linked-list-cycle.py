# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        return self.detectCycleDict(head)

        if head is None : return False

        slow = fast = head 
        # fast = head.next

        while fast and fast.next :

            slow = slow.next

            fast = fast.next.next

            if slow == fast : return True

        return False

    def detectCycleDict(self, head: Optional[ListNode]) -> bool:

        if head is None : return False

        seenNodes = set()

        temp = head

        while temp :

            if temp in seenNodes : return True
                
            else : seenNodes.add(temp)

            temp = temp.next

        return False
        