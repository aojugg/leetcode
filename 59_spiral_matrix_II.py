class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 79ms
        #4.92%
        if n==0:
            return []
        layer=n//2
        res=[ [0]*n for _ in range(n)]
        num=1
        for i in range(layer):
            start=i
            end=n-i-1
            for j in range(end-start):
                res[i][i+j]=num
                num+=1
            for j in range(end-start):
                res[i+j][end]=num
                num+=1
            for j in range(end-start):
                res[end][end-j]=num
                num+=1
            for j in range(end-start):
                res[end-j][i]=num
                num+=1
        if n%2!=0:
            res[layer][layer]=num
        return res
#***************************************************
    def generateMatrix(self, n):
        #66ms
        #24.59%
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
            
        
