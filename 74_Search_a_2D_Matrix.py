class Solution(object):
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row=len(matrix)
        if row==0:
            return False
            
        col=len(matrix[0])
        if col==0:
            return False
        r_mid=-1
        start=0
        end=row-1
        while start<=end:
        	mid=(start+end)/2
        	if target<matrix[mid][0]:
        		end=mid-1
        	elif target>matrix[mid][-1]:
        		start=mid+1
        	else:
        		r_mid=mid
        		break
        if r_mid==-1:
        	return False
        c_start=0
        c_end=col-1
        while c_start<=c_end:
        	c_mid=(c_start+c_end)/2
        	if matrix[mid][c_mid]==target:
        		return True
        	elif matrix[mid][c_mid]<target:
        		c_start=c_mid+1
        	else:
        		c_end=c_mid-1
        return False