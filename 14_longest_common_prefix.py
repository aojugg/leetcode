class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s=strs[0]
        p=len(s)
        for i in range(1,len(strs)):
            j=0
            while j<len(strs[i]) and j<p:
                if s[j] == strs[i][j]:
                    j+=1
                    
                else:
                    p=min(p,j)
        return s[:p]
