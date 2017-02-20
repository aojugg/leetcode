class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        if len(nums)<3:
            return res
        nums.sort()
        for i in len(nums):
            if nums[i]>0:
                break
            b=i+1
            e=len(nums)-1
            while b<e:
                if nums[i]+nums[b]+nums[e]==0:
                    res.append([nums[i],nums[b],nums[e]])
                    b+=1
                    e-=1
                elif nums[i]+nums[b]+nums[e]<0:
                    b+=1
                else:
                    e-=1
        return res
            
