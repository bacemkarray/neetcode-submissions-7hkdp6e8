# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head
        h = head
        
        if head.next == None:
            return False

        while h.next.next != None:
            if h.next.next == t:
                return True
            h = h.next.next
            t = t.next
        
        return False

        