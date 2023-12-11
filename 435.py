class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        newIntervals = sorted(intervals,key=lambda x:x[1])
        res = 0
        mostRecentEndTime = -float('inf')

        for start,end in newIntervals:
            if start >= mostRecentEndTime:
                mostRecentEndTime = end
            else:
                res += 1
        return res
