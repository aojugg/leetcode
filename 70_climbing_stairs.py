class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 2
        if n==1:
            return 1
        if n==0:
            return 0
        return climbStaris(n-1)+climbStairs(n-2)
