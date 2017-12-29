class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        L=[[0 for i in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    L[i][j]=grid[0]
                elif i==0 and j!=0:
                    L[i][j]=L[i][j-1]+grid[i][j]
                elif j==0 and i!=0:
                    L[i][j]=L[i-1][j]+grid[i][j]
                else:
                    L[i][j]=min(L[i-1][j],L[i][j-1])+grid[i][j]
        return L[m-1][n-1]

#**************************************************
    def minPathSum_2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #102ms
        #38.56%
        m=len(grid)
        n=len(grid[0])
        res=[[0] *n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    res[i][j]=grid[i][j]
                elif i==0 and j!=0:
                    res[i][j]=grid[i][j]+res[i][j-1]
                elif i!=0 and j==0:
                    res[i][j]=grid[i][j]+res[i-1][j]
                else:
                    res[i][j]=min(res[i-1][j],res[i][j-1])+grid[i][j]
        return res[m-1][n-1]
