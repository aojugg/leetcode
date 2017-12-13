class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        extra=1
        # extra 和第一行决定 列
        #【0】【0】 和第一列决定 行
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j]==0:
        			if j==0:
        				extra=0
        			else:
        				matrix[0][j]=0

        			matrix[i][0]=0
        #遍历第一列
        for i in range(1,m):
        	if matrix[i][0]==0:
        		for j in range(0,n):
        			matrix[i][j]=0
       	#便利第一行
        for j in range(1,n):
        	if matrix[0][j]==0:
        		for i in range(0,m):
        			matrix[i][j]=0
        if matrix[0][0]==0:
        	for i in range(1,n):
        		matrix[0][i]=0
        if extra==0:
        	for i in range(m):
        		matrix[i][0]=0

