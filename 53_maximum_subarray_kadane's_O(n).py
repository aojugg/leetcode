class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        max_sum=float('-inf')
        for i in range(nums):
            if res>=0:
                res+=nums[i]
            else:
                res=nums[i]
            if res>max_sum:
                max_sum=res
        return max_sum
            
