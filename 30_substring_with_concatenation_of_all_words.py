class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n=len(words)
        w=len(words[0])
        d={}
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
            
        res=[]
        for i in range(len(s)-n*w+1):
            l={}
            j=0
            while j<n:
                t=s[i+j*w:i+j*w+w]
                if t not in d:
                    break
                if t not in l:
                    l[t]=1
                else:
                    l[t]+=1
                
                if l[t]>d[t]:break
                j+=1
            if j==n:
                res.append(i)
        return res
                
                
                
                
                
