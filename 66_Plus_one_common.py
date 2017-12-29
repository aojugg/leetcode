class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c=1
        for i in range(len(digits)-1,-1,-1):
        	temp=digits[i]+c
        	digits[i]=temp%10;
        	c=temp//10
        if c==1:
        	digits=[1]+digits
        return digits
