class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row=len(matrix)
        col=len(matrix[0])
        right=[0*col]
        left=height=right[:]
        res=0
        for i in range(row):
            c_left,c_right=0,n
            for j in range(col):
                if matrix[i][j]==1:
                    height[j]+=1
                else:
                    height[j]=0
            for j in range(col):
                if matrix[i][j]==1:
                    left[j]=max(left[j],c_left)
                else:
                    left[j]=0
                    c_left=j+1
            for j in range(col-1,-1,-1):
                if matrix[i][j]==1:
                    right[j]=min(right[j],c_right)
                else:
                    right[j]=n
                    c_right=j
            for i in range(col):
                res=max(res,(right[j]-left[j])*height[j])
        return res
                
                
        
                        
