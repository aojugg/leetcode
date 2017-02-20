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
