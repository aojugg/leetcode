class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]] 
        for num in nums:
        	for temp in res[:]:
        		x=temp[:]
        		x.append(num)
        		res.append(x)
        return res

#*******************************************
    def subsets_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #66ms
        #61.25%
        res=[[]]
        for i in nums:
            for j in res[:]:
                temp=j[:]
                temp.append(i)
                res.append(temp)
        return res
