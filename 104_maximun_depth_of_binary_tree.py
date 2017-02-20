# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.temp=0
        def helper(root,num):
            if root:
                if root.val is not None:
                    
                    num+=1
                    self.temp=max(self.temp,num)
                    helper(root.left,num) 
                    helper(root.right,num)
        helper(root,0)
        return self.temp
