#
from functools import reduce
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
   
        if len(nums)<3:
            return []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                
                l=j+1
                r=len(nums)-1
                while l<r:
                    tem=reduce(lambda x,y:x+y ,[nums[i],nums[j],nums[l],nums[r]])
                    
                    if tem==target:
                        if [nums[i],nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1                            
                    elif tem<target:
                        l+=1
                    else:
                        r-=1
        return res
                    
