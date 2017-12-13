class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a=-1
        b=-1
        c=-1
        for i in range(len(nums)):
        	if nums[i]==0:
        		c+=1
        		nums[c]=2
        		b+=1
        		nums[b]=1
        		a+=1
        		nums[a]=0
        	elif nums[i]==1:
        		c+=1
        		nums[c]=2
        		b+=1
        		nums[b]=1
        	else:
        		c+=1
        		nums[c]=2