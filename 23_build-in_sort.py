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
        ret = []
        for lst in lists:
            while lst:
                ret.append(lst.val)
                lst = lst.next
            
        return sorted(ret)
