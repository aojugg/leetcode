# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1,n)
    def dfs(self,start,end):
        if start > end:
            return [None]
        res=[]
        for tem in range(start,end+1):
            l_tree=self.dfs(start,tem-1)
            r_tree=self.dfs(tem+1,end)
            for i in l_tree:
                for j in r_tree:
                    root=TreeNode(tem)
                    root.left=i
                    root.right=j
                    res.append(root)
        return res
