# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        
        sz = 0
        while head:
            head = head.next
            sz+=1
            
        n = sz - n 
        
        i=0
        while i!=n and cur and prev:
            i+=1
            cur = cur.next
            prev = prev.next
        
        if cur:
            prev.next = cur.next
        
        return dummy.next
        