class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        max_p=0
        best_b=prices[0]
        for i in range(1,len(prices)):
            if prices[i]-best_b>max_p:
                max_p=prices[i]-best_b
            if prices[i]<best_b:
                best_b=prices[i]
        return max_p
        

