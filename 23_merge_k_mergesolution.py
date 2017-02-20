# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(s1,s2):
            q=n=ListNode(0)
            while s1 and s2:
                if s1.val<s2.val:
                    q.next=s1
                    s1=s1.next
                else:
                    q.next=s2
                    s2=s2.next
                q=q.next
            if not s1:
                q.next=s2
            if not s2:
                q.next=s1
            return n.next
        if not lists:
            return []
        if len(lists)==1:
            return lists[0]
        mid=len(lists)/2
        left=mergeKLists(lists[:mid])
        right=mergeKLists(lists[mid:])
        return merge(left,right)
