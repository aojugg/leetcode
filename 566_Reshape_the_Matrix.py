class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(nums)
        n=len(nums[0])
        if n*m != r*c:
            return nums
        temp = []
        for line in nums:
            temp.extend(line)
        res = []
        for i in range(r):
            res.append(temp[i*c:i*c+c])
        return res
