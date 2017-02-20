class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str.strip()
        n,flag=0,1

            
        if str[0] == '+':
            str=str[1:]
            
        elif str[0] == '-':
            str=str[1:]
            flag=-1
        if not str:
            return 0
        for i in str:
            if i>='0' and i<='9':
                
                n=n*10+ord(i)-ord('0')
            else:
                return 0
        n=n if n<2147483647 else 2147483647
        n=n*flag
        return n
