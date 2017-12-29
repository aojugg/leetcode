class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        for i in range(n-1,-1,-1):
        	if digits[i]==9:
        		digits[i]=0
        	else:
        		digits[i]+=1
        		return digits
        return [1]+digits
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag=0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                if digits[i]==9:
                    flag=1
                    digits[i]=0
                else:
                    digits[i]+=1
            else:
                if flag==1:
                    if digits[i]==9:
                        digits[i]=0
                    else:
                        digits[i]+=1
                        flag=0
        if flag==1:
            digits.insert(0,1)
        
        return digits
        


        
