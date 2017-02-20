class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    # 先沿着对角线翻转一次，再沿着水平中线翻转一次。
        s=len(matrix)
        for i in range(s):
            for j in range(s-i):
                matrix[i][j],matrix[s-j-1][s-i-1]=matrix[s-j-1][s-i-1],matrix[i][j]
        for i in range(s/2):
            for j in range(s):
                matrix[i][j],matrix[s-1-i][j]=matrix[s-1-i][j],matrix[i][j]
            
