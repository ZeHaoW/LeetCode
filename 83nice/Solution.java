/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode newHead = head.next;
        if(newHead.val == head.val){
            newHead = head.next.next;
            head.next = newHead;
            head = deleteDuplicates(head);
        }
        else{
            newHead = deleteDuplicates(newHead);
        }
        return head;
    }
}