class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums)<=2:
        #    return len(nums)
        i=0
        for num in nums:
            if i<2 or num>nums[i-2]:
                nums[i]=num
                i+=1
        return i
    def removeKD(self, nums,k):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums)<=2:
        #    return len(nums)
        i=0
        for num in nums:
            if i<k or num>nums[i-k]:
                nums[i]=num
                i+=1
        return i
    
        
