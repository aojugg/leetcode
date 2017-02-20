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
        if not lists:
            return []
        for i in range(1,len(lists)):
            n=ListNode(0)
            q=n
            while lists[0] and lists[i]:
                if lists[0].val<lists[i].val:
                    q.next=lists[0]
                    lists[0]=lists[0].next
                    q=q.next
                else:
                    q.next=lists[i]
                    lists[i]=lists[i].next
                    q=q.next
            if not lists[0]:
                    q.next=lists[i]
            if not lists[i]:
                    q.next=lists[0]
            lists[0]=n.next
        return lists[0]
