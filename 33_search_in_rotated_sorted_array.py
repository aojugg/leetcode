class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=nums[l] and  nums[mid]<=nums[r]:
                if target==nums[mid]:
                    return mid
                elif target<nums[mid]:
                    l=l
                    r=mid-1
                else:
                    l=mid+1
                    r=r
            elif nums[mid]>=nums[l] and nums[mid]>=nums[r]:
                if target==nums[mid]:class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=nums[l] and  nums[mid]<=nums[r]:
                if target==nums[mid]:
                    return mid
                elif target<nums[mid]:
                    l=l
                    r=mid-1
                else:
                    l=mid+1
                    r=r
            elif nums[mid]>=nums[l] and nums[mid]>=nums[r]:
                if target==nums[mid]:
                    return mid
                elif target>=nums[l] and target<nums[mid]:
                    l=l
                    r=mid-1
                else:
                    l=mid+1
                    r=r
            else:
                if target==nums[mid]:
                    return mid
                elif target<=nums[r] and target>=nums[mid]:
                    l=mid+1
                    r=r
                else:
                    l=l
                    r=mid-1
        if nums[l]==target:
            return l
        else:
            return -1
        

                    return mid
                elif target>=nums[l] and target<nums[mid]:
                    l=l
                    r=mid-1
                else:
                    l=mid+1
                    r=r
            else:
                if target==nums[mid]:
                    return mid
                elif target<=nums[r] and target>=nums[mid]:
                    l=mid+1
                    r=r
                else:
                    l=l
                    r=mid-1
        if nums[l]==target:
            return l
        else:
            return -1
        
