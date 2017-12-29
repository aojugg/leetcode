class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t=nums[-1]
        change=len(nums)-1
        flag=float('inf')
        index=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<t:
                t=nums[i]
                change=i
                break
            else:
                t=nums[i]
        if len(nums)!=1 and change==len(nums)-1:
            nums.reverse()
            
        for i in range(change+1,len(nums)):
            if nums[i]> nums[change]:
                if nums[i]-nums[change]<flag:
                    
                    index=i
                    flag=nums[i]-nums[change]
       
        nums[change],nums[index]=nums[index],nums[change]
        for j in range(change+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[j]>nums[k]:
                    nums[j],nums[k]=nums[k],nums[j]

    #*********
    class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 6 5 4 8 7 5 1
        temp=nums[-1]
        index=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=temp:
                temp=nums[i]
                continue
            else:
                index=i
                break
        min_v=float('inf')
        next_index=0
        for i in range(index+1,len(nums)):
            if nums[i]>nums[index]:
                if nums[i]<min_v:
                    min_v=nums[i]
                    next_index=i
        nums[index] , nums[next_index] =nums[next_index],nums[index]
        sub_array=nums[index+1:]
        sub_array.sort()
        nums[index+1:]=sub_array
                    
                
            
