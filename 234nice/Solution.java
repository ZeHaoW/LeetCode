/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        slow = reverse(slow);
        while(slow != null){
            if(slow.val != head.val)
                return false;
            head = head.next;
            slow = slow.next;
        }
        return true;
    }

    private ListNode reverse(ListNode head){
        ListNode tmp = head;
        ListNode prev = head;
        if(head == null) return head;
        while(head.next != null){
            tmp = head.next;
            head.next = head.next.next;
            tmp.next = prev;
            prev = tmp;
        }
        return prev;
    }
}