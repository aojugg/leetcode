class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            val=nums.pop()
            nums.insert(0,val)

# *****************************
#[1,2,3,4,5,6,7] k=3
#expected output : [5,6,7,1,2,3,4]
#1.first reverse : [4,3,2,1]
#2.second reverse : [7,6,5]
#3. third reverse [4,3,2,1,7,6,5] to [5,6,7,1,2,3,4]
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(l,i,j):
            while i<j:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
        if len(nums)<=1:
            return 
        k=k%len(nums)
        reverse(nums,0,len(nums)-1-k)
        reverse(nums,len(nums)-k,len(nums)-1)
        reverse(nums,0,len(nums)-1)
        
        
