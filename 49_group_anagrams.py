class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        res=[]
        for i in strs:
            s=''.join(sorted(i))
            if s not in d:
                d[s]=[i]
            else:
                d[s]+=[i]
        for i in d:
            tem=d[i]
            tem.sort()
            res.append(tem)
        return res
