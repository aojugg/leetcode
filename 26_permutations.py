class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub=[]
        res=[]
        self.dfs(nums,sub)
        return self.res
    def dfs(self,Nums,sublist):
        if len(sublist)==len(Nums):
            self.res.append(sublist[:])
        for i in Nums:
            if i in sublist:
                continue
            sublist.append(i)
            self.dfs(Nums,sublist)
            sublist.remove(i)
            
        
