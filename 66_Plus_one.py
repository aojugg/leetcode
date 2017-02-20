class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(n-1,-1,-1):
        	if digits[i]==9:
        		digits[i]=0
        	else:
        		digit[i]+=1
        		return digits
        return [1]+digits
        


        