class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m=len(s1)
        n=len(s2)
        L=[[0 for i in range(n+1) for i in range(m+1)]]
        L[0][0] =True
        for i in range(1,m+1):
            L[i][0]=L[i-1][0] and s3[i-1]==s1[i-1]
        for i in range(1,m+1):
            L[0][i]=L[0][i-1] and s3[i-1]==s2[i-1]
            
        for i in  range(m+1):
            for j in range(n+1):
                
                if s3[i+j-1]==s1[i-1] and s3[i+j-1]==s2[j-1]:
                    
                    L[i][j]=L[i-1][j] or L[i][j-1]
                elif s3[i+j-1]==s1[i-1] and s3[i+j-1]!=s2[j-1]:
                    L[i][j]=L[i-1][j]
                elif s3[i+j-1]!=s1[i-1] and s3[i+j-1]==s2[j-1]:
                    L[i][j]=L[i][j-1]
                else:
                    L[i][j]=False
        return L[m][n]    
