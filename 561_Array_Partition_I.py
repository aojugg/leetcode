class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) % 2==1:
            raise Exception
        if len(nums)==0:
            return 0
        
        sorted_nums=sorted(nums)
        sum=0
        for i in range(len(nums)//2):
            sum += min(sorted_nums[2*i],sorted_nums[2*i+1])
        return sum        
