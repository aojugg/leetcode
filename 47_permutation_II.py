class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        sub=[]
        self.dfs(nums,[],res)
        return res
    def dfs(self,n,s,res):
        if not n and s not in res:
            
            res.append(s)
        for i in range(len(n)):
            self.dfs(n[:i]+n[i+1:],s+[n[i]],res)
