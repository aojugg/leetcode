class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        L=[[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(1,n+1):
            L[1][i]=1
        for i in range(1,m+1):
            L[i][1]=1
        for i in range(2,m+1):
            for j in range(2,n+1):
                    
                    L[i][j]=L[i-1][j]+L[i][j-1]
        return L[m][n]
