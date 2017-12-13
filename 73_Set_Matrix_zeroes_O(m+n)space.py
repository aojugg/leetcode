class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[1 for _ in range(m)]
        col=[1 for _ in range(n)]
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j]==0:
        			row[i]=0
        			col[j]=0
        #hang
        for i in range(m):
        	if row[i]==0:
        		for j in range(n):
        			matrix[i][j]=0
        for j in range(n):
        	if col[j]==0:
        		for i in range(m):
        			matrix[i][j]=0
