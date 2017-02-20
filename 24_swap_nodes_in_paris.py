# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        if not head.next:
            return head
        pre=ListNode(0)
        q=pre.next=head
        head=pre
        while q and q.next:
            pre.next=q.next
            q.next=pre.next.next
            
            pre.next.next=q
            pre=q
            q=q.next
        return head.next
