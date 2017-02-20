class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t :
            return 0
        if len(s)<len(t):
            return 0
        m=len(s)
        n=len(t)
        L=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            L[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                L[i][j]=L[i-1][j]
                if s[i-1]==t[j-1]:
                    L[i][j]+=L[i-1][j-1]
        return L[m][n]
                
