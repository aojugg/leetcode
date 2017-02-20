class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m=len(triangle)
        n=len(triangle[-1])
        L=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    L[i][j]=triangle[i][j]
                elif j==0 and i!=0:
                    L[i][j]=L[i-1][j]+triangle[i][j]
                elif j==i:
                    L[i][j]=L[i-1][j-1]+triangle[i][j]
                else:
                    
                    L[i][j]=min(L[i-1][j],L[i-1][j-1])+L[i][j]
        return sorted(L[-1])[0]
