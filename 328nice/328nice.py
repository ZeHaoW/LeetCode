# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        even = head.next
        while head.next != None:
            p = head.next
            head.next = head.next.next
            if p.next == None:
                break
            p.next = p.next.next
            head = head.next
        head.next = even
        return odd
