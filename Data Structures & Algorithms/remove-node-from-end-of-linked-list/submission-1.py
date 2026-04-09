# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        # the difference between the end of the list (n) and the kth node (k) is equal to the index of k
        # so if you just place the two pointers k away from each other then by the time the first pointer reaches the end, the other would be at the required spot. 
        dummy = ListNode()
        dummy.next = head
        p1 = head
        p2 = head
        p2_prev = dummy
        while n > 0:
            p1 = p1.next
            n -= 1

        while p1:
            p1 = p1.next
            p2_prev = p2
            p2 = p2.next
        
        p2_prev.next = p2.next

        return dummy.next
    