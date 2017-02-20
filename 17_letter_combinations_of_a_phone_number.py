#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        cach=[]
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if not digits:
            return
        for i in digits[0]:
            cach.append(i)
        for i in range(1,len(digits)):
            
            while cach:
                n=cach.pop()
                for j in digits[i]:
                    res.append(n+j)
            cach=res
            res=[]

        return cach  
                
            
        
