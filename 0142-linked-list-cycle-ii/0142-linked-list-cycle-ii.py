# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycleDict(self, head: Optional[ListNode]) -> Optional[ListNode]:

        seenNodes = set()

        temp = head

        # Traversing the LL, the first node that repeats 
        # is the start of the cycle

        while temp :

            if temp in seenNodes:
                return temp

            seenNodes.add(temp)

            temp = temp.next
        
        return None

    def detectCycleNoDict(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

        if fast is None : return fast

        temp = head

        while temp != slow :
            temp = temp.next
            slow = slow.next

        return temp

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.detectCycleDict(head)

        return self.detectCycleNoDict(head)