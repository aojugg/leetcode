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
