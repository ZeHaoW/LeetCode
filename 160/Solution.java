/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int count1 = 0, count2 = 0;
        ListNode prev_a = headA;
        ListNode prev_b = headB;
        while(prev_a != null){
            prev_a = prev_a.next;
            count1++;
        }
        while(prev_b != null){
            prev_b = prev_b.next;
            count2++;
        }
        if(count1 >= count2){
            int diff = count1 - count2;
            for(int i = 0; i < diff; i++)
                headA = headA.next;
        }
        else{
            int diff =  count2 - count1;
            for(int i = 0; i < diff; i++)
                headB = headB.next;
        }
        while(headA != null && headB != null){
            if(headA != headB){
                headA = headA.next;
                headB = headB.next;
            }
            else
                return headA;
        }
        return null;
    }
}