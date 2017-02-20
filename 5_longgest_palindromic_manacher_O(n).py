class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        L='#'+'#'.join(s)+'#'
        RL=[0]*len(L)
        maxright=0
        pos=0
        maxlen=0
        for i in range(len(L)):
            if i<maxright:
                RL[i]=min(RL[2*pos-i],maxright-i)
            else:
                RL[i]=1

            while i-RL[i]>=0 and i+RL[i]<len(L) and L[i-RL[i]]==L[i+RL[i]]:
                RL[i]+=1
            if RL[i]+i-1>maxright:
                maxright=RL[i]+i-1
                pos=i
            maxlen=max(maxlen,RL[i])
        return maxlen-1
