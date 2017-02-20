class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #2017/1/12
        #complexity O(n)
        #
        d_t={}
        d_s={}
        for char in t:
            if char not in d_t:
                d_t[char]=1
                d_s[char]=1
                
            else:
                d_t[char]+=1
                d_s[char]+=1
        length=len(t)
        start=0
        minSize=len(s)+1
        minStart=0
        
        for end in range(len(s)):
            if s[end] in d_s and d_s[s[end]]>0:
                d_t[s[end]]-=1
                if d_t[s[end]]>=0:
                    length-=1
                if length==0:
                    
                    while True:
                        if s[start] in d_s and d_s[s[start]] >0:
                            if d_t[s[start]]<0:
                                d_t[s[start]]+=1
                            else:
                                break
                        start+=1
                    if minSize>end-start+1:
                        minSize=end-start+1
                        minStart=start
            
        if minSize<len(s)+1:
            return s[minStart:minStart+minSize]
        else:
            return ''
                
