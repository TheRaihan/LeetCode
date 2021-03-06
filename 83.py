# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while head:
            if head == head.next:
                cur = head.next.next
            else:
                cur = head.next
            head = head.next
        
        return dummy.next
        