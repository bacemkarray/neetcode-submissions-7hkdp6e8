# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s.next
        s.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        h1 = head
        h2 = prev
        while h2:
            temp1 = h1.next
            temp2 = h2.next

            h1.next = h2
            h2.next = temp1
            
            h1 = temp1
            h2 = temp2
        

        