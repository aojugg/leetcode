class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        prev=nums[0]
        for i in nums[1:]:
            if prev==i:
                nums.remove(i)
            else:
                prev=i
        return len(nums)
    
# return length of nums,so dont have to remove elements in the array
# create a varable store the length.
    def removeDuplicates2(self,nums):
        if len(nums)<=1:
            return len(nums)
        cur=0
        for i in range(1,len(nums)):
            if nums[cur]!=nums[i]:
                cur+=1
                nums[cur]=nums[i]
                #non duplicated elements before flag cur
        return cur+1         
