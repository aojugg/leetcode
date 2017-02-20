class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        start=0
        remain=0
        debt=0
        for i in range(n):
            remain+=gas[i]-cost(i)
            if remain<0:
                debt+=remain
                start=i+1
                remain=0
        return start if remain+debt>=0 else -1
