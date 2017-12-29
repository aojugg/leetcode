#
class Solution:
# dict
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)<=1:
            return None
        d={}
        index1=-1
        index2=-1
        for i in range(len(numbers)):
            if numbers[i] not in d:
                d[target-numbers[i]]=i
            else:
                index1=d[numbers[i]]
                index2=i
        if index1<index2:
            return [index1+1,index2+1]
        else:
            return [index2+1,index1+1]


# two pointer
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
