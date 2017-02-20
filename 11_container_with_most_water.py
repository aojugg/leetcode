class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        max_c=0
        while l!=r:
            l_h=height[l]
            r_h=height[r]
            tem=min(l_h,r_h)*(r-l)
            max_c=max(max_c,tem)
            if l_h<r_h:
                l+=1
            else:
                r-=1
        return max_c
        
