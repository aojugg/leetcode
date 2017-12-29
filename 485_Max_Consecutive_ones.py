class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_max=[]
        length=0
        for i in nums:
            if i==1:
                length+=1
            else:
                all_max.append(length)
                length=0
        all_max.append(length)
        return max(all_max)
