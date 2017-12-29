#杨辉三角
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows == 1:
            return [[1]]
        dp=[[0]*(i+1) for i in range(numRows)]
        dp[0]=[1]
        dp[1]=[1,1]
        for i in range(2,numRows):
            for j in range(0,i+1):
                if j==0:
                    dp[i][j]=1
                elif j==i:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        res=[]
        for i in range(numRows):
            res.append(dp[i])
        return res
