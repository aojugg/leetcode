class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if m<1 or n<1:
            return
        if m==1 and n==1:
            return 1
        return uniquePaths(m-1,n)+uniquePaths(m.n-1)
