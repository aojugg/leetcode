class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        index=-1
        while l<=r:
            mid=(l+r)/2
            if nums[mid]==target:
                index=mid
                break
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if index==-1:
            return [-1,-1]
        p=s=mid
        for i in range(mid-1,-1,-1):
            if nums[i]==target:
                p=i
            else:
                break
        for j in range(mid+1,len(nums)):
            if nums[j]==target:
                s=j
            else:
                break
        return [p,s]
                
                
        
        
