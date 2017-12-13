class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=1
        c=0
        la=len(a)
        lb=len(b)
        res=""
        if la==0:
        	return b
        if lb==0:
        	return a
        while i<=la or i<=lb:
        	if i<=la:
        		n1=int(a[-i])
        	else:
        		n1=0
        	if i<=lb:
        		n2=int(b[-i])
        	else:
        		n2=0
        	temp=n1+n2+c
        	if temp>1:
        		c=1
        	else:
        		c=0
        	res=str(temp%2)+res
        	i+=1
        if c==1:
        	return "1"+res
        else:
        	return res

