/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode SwapNodes(ListNode head, int k) {
        ListNode startK =null,trailing = null,current=head;
        int i=1;
        
        while(current!=null)
        {
            
            if(trailing!=null)
                trailing = trailing.next;
            
            if (i==k){
                startK=current;                
                trailing=head;
            }
            
            current = current.next;
            i++;
        }
        
        i = startK.val;
        startK.val = trailing.val;
        trailing.val = i;
        return head;
    }
}