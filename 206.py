# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        arr.reverse()
        
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next
        
        return dummy.next
        
""" 
better solution
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next, prev,cur =  prev,cur,nxt
        return prev