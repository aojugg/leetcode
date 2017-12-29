class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if not candidates:
            return result
        candidates.sort()
        self.dfs(candidates,target,[],0,result)
        return result
    def dfs(self,candidates,target,path,index,result):
        if target==0:
            result.append(path[:])
            return
        for i in range(index,len(candidates)):
            if candidates[i]>target:
                break
            self.dfs(candidates,target-candidates[i],path+[candidates[i]],i,result)




#****************************************
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def help(candidates,target,lo,res,s_l):
            if lo>len(candidates)-1:
                return None
            if candidates[lo]==target:
                s_l.append(candidates[lo])
                res.append(s_l)
            elif candidates[lo]>target:
                return None
            else:
                help(candidates,target-candidates[lo],lo,res,s_l+[candidates[lo]])
                help(candidates,target,lo+1,res,s_l)
                
        res=[]
        candidates.sort()
        help(candidates,target,0,res,[])
        return res
