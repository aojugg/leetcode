class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        t=0
        n=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        r=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        s=''
        for i in range(len(n)):
            t=num//n[i]
            num= num%n[i]
            for j in range(t):
                s+=r[i]
        return s
            
