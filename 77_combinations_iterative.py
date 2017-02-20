class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        iterative
        """
        res=[]
        temp=[]
        num=1
        while True:
        	l=len(temp)
        	if l==k:
        		res.append(temp[:])
        	if l==k or n-num+1<k-l:
        		if not temp:
        			return res
        		num=temp.pop()+1
        	else:
        		temp.append(num)
        		num+=1
