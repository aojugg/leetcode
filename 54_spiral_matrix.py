class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        if not matrix or len(matrix)==0:
            return res
        
        m=len(matrix)
        n=len(matrix[0])
        layer=(min(m,n)+1)/2
        for i in range(layer):
            for j in range(i,n-i):
                res.append(matrix[i][j])
            for j in range(i+1,m-i):
                res.append(matrix[j][n-1-i])
            if m-1-i>i:
                for j in range(n-1-i-1,i-1,-1):
                    res.append(matrix[m-1-i][j])
            if n-1-i>i:
                for j in range(m-1-i-1,i,-1):
                    res.append(matrix[j][i])
        return res
                    
                
