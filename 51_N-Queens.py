class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens,xy1,xy2):
            p=len(queens)
            if p==n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy1 and p+q not in xy2:
                    dfs(queens+[q],xy1+[p-q],xy2+[p+q])
        result =[]
        dfs([],[],[])
        return [ ["."*i +"Q"+"."*(n-i-1) for i in e ] for e in result]
