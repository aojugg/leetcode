# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1=l1
        p2=l2
        node=ListNode(0)
        q=node
        while p1 is not None and p2 is not None:
            if p1.val<p2.val:
                q.next=p1
                p1=p1.next
                q=q.next
            else:
                q.next=p2
                p2=p2.next
                q=q.next
        if not p1:
            q.next=p1
        if not p2:
            q.next=p2
        return node.next
        
