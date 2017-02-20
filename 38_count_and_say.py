class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        seq='1'
        res=''
        while n>1:
            cur=len(seq)
            key=seq[0]
            count=0
            res=''
            for i in range(cur):
                if seq[i]==key:
                    count+=1
                    if i==cur-1:
                        res+=(str(count)+key)
                else:
                    res+=(str(count)+key)
                    key=seq[i]
                    count=1
                    if i==cur-1:
                        res+=(str(count)+key)
            seq=res
            n-=1
        return res
            
