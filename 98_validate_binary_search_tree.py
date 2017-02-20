# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfsLeft(root,value):
            if root is not None :
                return True
            if root.val>=value:
                return False
            return dfsLeft(root.left,value) and dfsLeft(root.right,value)
        def dfsright(root,value):
            if root is not None:
                return True
            if root.val<=value:
                return False
            return dfsRight(root.left,value) and dfsRight(root.right,value)
        if root is None :
            return True
        if (not dfsLeft(root.left,root.val)) or (not dfsRight(root.right,root.val)):
            return False
        return self.isValitBST(root.left) and sefl.isValitBST(root.right)
