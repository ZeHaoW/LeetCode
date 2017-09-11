/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null)
            return l2;
        if(l2 == null)
            return l1;
        if(l1.val <= l2.val){
            ListNode newList = l1;
            ListNode newHead = l1.next;
            newList.next = mergeTwoLists(newHead, l2);
            return newList;
        }
        else{
            ListNode newList = l2;
            ListNode newHead = l2.next;
            newList.next = mergeTwoLists(l1, newHead);
            return newList;
        }
    }
}