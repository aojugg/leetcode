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
    def uniquePaths_2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def f(i,j):
        # recursive time limit exceeded
            if i==0 and j==0:
                return 1
            if i==0 and j!=0:
                return 1
            if i!=0 and j==0:
                return 1
            return f(i-1,j) + f(i,j-1)
        return f(m-1,n-1)
    def uniquePaths_3(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #dynamic programing 62ms
        # 33,64%
        res=[[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j]=res[i][j-1]+res[i-1][j]
        return res[m-1][n-1]
