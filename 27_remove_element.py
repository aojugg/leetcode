#remove element
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i=0
        #每次循环时，都会检查nums的长度，（remove之后，nums的长度会减小）
        while(i<len(nums)):
            if val==nums[i]:
                nums.remove(val)
                # remove之后，后一个索引的值会添加到当前索引，所以需要后退一个位置
                i-=1
            i+=1
        return len(nums)
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[cur]=nums[i]
                cur+=1
        return cur
