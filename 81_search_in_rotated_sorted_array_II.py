class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        #75ms
        #37.50%
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            print(lo,hi)
            mid=(hi+lo)//2
            if target==nums[mid]:
                return True
            if nums[mid]<nums[lo]:
                # left hand is ascending
                if target==nums[mid]:
                    return True
                elif target<=nums[hi] and target>nums[mid]:
                    lo=mid+1
                elif target<nums[mid] or target>nums[hi]:
                    hi=mid-1
            elif nums[mid]>nums[lo]:
                #right hand is ascending
                if target==nums[mid]:
                    return True
                elif target>nums[mid] or target<nums[lo]:
                    lo=mid+1
                elif target<nums[mid] and target>=nums[lo]:
                    hi=mid-1
            else:
                lo+=1
        return False
