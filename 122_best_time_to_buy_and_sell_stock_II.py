class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        i=1
        while i<len(prices):
            if prices[i]>prices[i-1]:
                res+=(prices[i]-prices[i-1])
            i+=1
        return res
#********************
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        max_p=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_p+=prices[i]-prices[i-1]
        return max_p
