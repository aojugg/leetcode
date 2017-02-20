class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res=0
        n1=0
        if num1=="0" or num2=="0":
            return str(0)
        
        for i in range(len(num1)):
            n1*=10
            n1+=(ord(num1[i])-ord("0"))
          
            
        for j in range(len(num2)):
            res*=10
            res+=(ord(num2[j])-ord("0"))*n1

        return str(res)
                
