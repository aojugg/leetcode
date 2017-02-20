class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        for i in range(len(nums)):
            tem=0
            while nums[i]!=i+1:
                if nums[i]>len(nums) or nums[i]<=0 or nums[i]==nums[nums[i]-1]:
                    break
                tem=nums[i]
                nums[i]=nums[tem-1]
                nums[tem-1]=tem

                
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
            
