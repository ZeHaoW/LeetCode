/**
* Definition for singly-linked list.
* public class ListNode {
*     int val;
*     ListNode next;
*     ListNode(int x) { val = x; }
* }
*/
class Solution {
  public ListNode removeElements(ListNode head, int val) {
    if(head == null) return head;
    while(head != null && head.val == val) {
      ListNode prev = head.next;
      head.next = null;
      head = prev;
    }
    if(head != null){
      ListNode tmp = head;
      while(tmp.next != null){
        if(tmp.next.val == val){
          tmp.next = tmp.next.next;
        }
        else tmp = tmp.next;
      }
    }
    return head;
  }
}
