class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c=nums[0]
        end=len(nums)
        for i in range(end):
            c=max(c,i+nums[i])
            if c<=i:
                return False
        return True
            
            
