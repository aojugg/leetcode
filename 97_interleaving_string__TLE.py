class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m=len(s1)
        n=len(s2)
        if m>0 and n>0:
            if s3[-1]==s1[-1] and s3[-1]==s2[-1]:
                return self.isInterleave(s1[:-1],s2,s3[:-1]) or self.isInterleave(s1,s2[:-1],s3[:-1])
            elif s3[-1]==s1[-1] and s3[-1]!=s2[-1]:
                return self.isInterleave(s1[:-1],s2,s3[:-1])
            elif s3[-1]!=s1[-1] and s3[-1]==s2[-1]:
                return  self.isInterleave(s1,s2[:-1],s3[:-1])
            else:
                return False
        elif m==0 and n>0:
            if s2==s3:
                return True
            else:
                return False
        elif m>0 and n==0:
            if s1==s3:
                return True
            else:
                return False
        else:
            if not s3:
                return True
            else:
                return False
