class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f(n) = f(n-1) > 0 ? f(n-1) + nums[n] : nums[n]
        # f(n) 以nums[n]为最后一位元素的子序列的最大值
        #res= max( f(n) for n in range(1,length of nums ))
        
        dp=[0 for i in range(len(nums))]
        dp[0]=nums[0]
        max_val=dp[0]
        for i in range(1,len(nums)):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
            max_val=max(max_val,dp[i])
        return max_val
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f(n) = f(n-1) > 0 ? f(n-1) + nums[n] : nums[n]
        # f(n) 以nums[n]为最后一位元素的子序列的最大值
        #res= max( f(n) for n in range(1,length of nums ))
        
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
