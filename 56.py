class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        for start,end in intervals:
            if start <= prevEnd:
                if end > prevEnd:
                    prevEnd = end
            else:
                res.append([prevStart,prevEnd])
                prevStart = start
                prevEnd = end
        res.append([prevStart,prevEnd])
        return res
