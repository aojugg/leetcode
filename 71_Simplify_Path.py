class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stock=path.split("/")
        stack=[]
        for i in range(len(stock)):
        	if stock[i]=="." or stock[i]=="":
        		continue
        	elif stock[i]=="..":
        	    if len(stack)!=0: #pop 前注意stack不为空
        		    stack.pop()
        	else:
        		stack.append(stock[i])
        
        return "/"+"/".join(stack)