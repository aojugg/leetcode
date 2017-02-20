class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=0
        n=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        r=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        n=0
        while t <len(s):
            if s[i] =='M':
                n+=1000
            elif s[i]=='C':
                if s[i+1]=='M':
                    n+=900
                    i+=1
                elif s[i+1]=='D':
                    n+=400
                    i+=1
                else:
                    n+=100
            elif s[i]=='D':
                n+=500
            elif s[i]=='X':
                if s[i+1]=='C':
                    n+=90
                    i+=1
                elif s[i+1]=='L':
                    n+=40
                    i+=1
                else:
                    n+=10
            elif s[i]=='L':
                n+=50
            elif s[i]=='I':
                if s[i+1]=='X':
                    n+=9
                    i+=1
                elif s[i+1]=='V':
                    n+=4
                    i+=1
                else:
                    n+=1
            elif s[i]=='V':
                n+=5
            i+=1
        return n
            
        
