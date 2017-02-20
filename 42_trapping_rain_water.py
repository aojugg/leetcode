class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,minheight,res=0
        r=len(height)-1
        while l<r:
            while l<r and height[l]<=minheight:
                res+=minheight-height[l]
                l+=1
            while l<r and height[r]<=minheight:
                res+=minheight-height[r]
                r-=1
            minheight=min(height[l],height[r])
        return res
            
            
