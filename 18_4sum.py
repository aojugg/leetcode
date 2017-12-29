class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s<target:
                        k+=1
                    elif s>target:
                        l-=1
                    else:
                        if [nums[i],nums[j],nums[k],nums[l]] not in res:
                            res.append([nums[i], nums[j], nums[k],nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1; l -= 1
                
        return res
                        
