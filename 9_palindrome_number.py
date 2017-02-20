class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=abs(x)
        x=str(x)
        while x:
            
            if x[0]==x[-1]:
            
                x=x[1:-1]
            else:
                return False
        return True
            
