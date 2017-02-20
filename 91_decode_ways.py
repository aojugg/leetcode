class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n=len(s)
        L=[0]*(n+1)
        L[0]=1 
        for i in range(1,n+1):
            if s[i-1]!="0":
                L[i]+=L[i-1]
            if i!=1 and s[i-2:i]<"27" and s[i-2:i]>"09":
                L[i]+=L[i-2]
        return L[n]
