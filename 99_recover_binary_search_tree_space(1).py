# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def FindTwoNodes(self,root):
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val >root.val:
                self.n2=root
                if self.n1==None:
                    self.n1=self.prev
            self.prev=root
            self.FindTwoNodes(root.right)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1=self.n2=None
        self.prev=None
        self.FindTwoNodes(root)
        self.n1.val,self.n2.val=self.n2.val,self.n1.val
        return root
