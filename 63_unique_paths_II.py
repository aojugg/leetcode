class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        L=[[-1 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    if obstacleGrid[i][j]==0:
                        L[i][j]=1
                    else:
                        L[i][j]=0
                elif i==0 and j!=0:
                    if obstacleGrid[i][j]==0:
                        L[i][j]=L[i][j-1]
                    else:
                        L[i][j]=0
                elif j==0 and i!=0:
                    if obstacleGrid[i][j]==0:
                        L[i][j]=L[i-1][j]
                    else:
                        L[i][j]=0
                else:
                    if obstacleGrid[i][j]==0:
                        L[i][j]=L[i-1][j]+L[i][j-1]
                    else:
                        L[i][j]=0
        return L[m-1][n-1]
