class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        index=0
        res=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                if  not stack:
                    index=i+1
                else:
                    
                    stack.pop()
                    if not stack:
                        res=max(res,i-index+1)
                    else:
                        res=max(res,i-stack.pop())
                        
