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
#***************
    def canJump_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
             
        max_r=0
        for i in range(len(nums)):
            if max_r<i:
                return False
            max_r=max(max_r,i+nums[i])
        return True
            
