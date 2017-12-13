class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        temp=[]
        def dfs(res,temp,nums,j):
        	res.append(temp[:])
        	for i in range(j,len(nums)):
        		temp.append(nums[i])
        		dfs(res,temp,nums,i+1)
        		del temp[-1]
        dfs(res,temp,nums,0)
        return res
