# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 122ms 28.27%
        if len(intervals)<2:
            return intervals
        res=[]
        intervals=sorted(intervals,key=lambda x:x.start)
        intervals.reverse()
        while len(intervals)>1:
            f=intervals.pop()
            s=intervals.pop()
            if f.end>=s.start and s.end>f.end:
                intervals.append(Interval(f.start,s.end))
            elif f.end>=s.start and f.end>=s.end:
                intervals.append(Interval(f.start,f.end))
            else:
                res.append(f)
                intervals.append(s)
        res.append(intervals.pop())
        return res
    #*****************
    def merge_2(self, intervals):
        #119ms
        #33.33%
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
        
