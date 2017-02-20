class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        chaoshi
        """
        res=[]
        self.count=0
        def dfs(start,temp):
            if self.count==k:
                res.append(temp)
                return 
            for i in range(start,n+1):
                self.count+=1
                dfs(i+1,temp+[i])
                self.count-=1
        dfs(1,[])
        return res
            