class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        reach=s=e=step=0
        while e <len(nums)-1:
            step+=1
            reach=e
            for i in range(s,e+1):
                if nums[i]+i>reach:
                    reach=nums[i]+i
            s=e+1
            e=reach
        return step
            
