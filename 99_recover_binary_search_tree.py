# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,l,lp):
        if root:
            self.inorder(root.left,l,lp)
            l.append(root.val)
            lp.append(root)
            self.inorder(root.right,l,lp)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        l=[]
        lp=[]
        self.inorder(root,l,lp)
        l.sort()
        for i in range(len(list)):
            lp[i].val=l[i]
        return root
