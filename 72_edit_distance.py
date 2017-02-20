class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)
#        if m==0:
#            return n
#        if n==0:
#            return m
        L=[ [0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                tem=0
                t=0
                if j==0:
                    L[i][j]=i
                elif i==0:
                    L[i][j]=j
                else:
                    tem=min(L[i-1][j]+1,L[i][j-1]+1)
                    t=L[i-1][j-1]+1 if word1[i-1]!=word2[j-1] else L[i-1][j-1]
                    L[i][j]=min(tem,t)
        return L[m][n]
          
          
