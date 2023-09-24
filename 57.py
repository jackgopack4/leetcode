class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(a:List[int],b:List[int])->bool:
            return (min(a[1],b[1])-max(a[0],b[0])) >= 0
        def merge(a:List[int],b:List[int])->List[int]:
            return [min(a[0],b[0]),max(a[1],b[1])]
        l = 0
        r = len(intervals)-1
        ans = len(intervals)
        mid = l + (r-l)//2
        while l <= r:
            mid = l + (r-l)//2
            if intervals[mid][0] > newInterval[0]:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        index_to_insert = ans
        if(index_to_insert) > len(intervals):
            intervals.append(newInterval)
            return intervals
        if index_to_insert > 0:
            prev = intervals[index_to_insert-1]
            
            if overlap(prev,newInterval):
                newInterval = merge(prev,newInterval)
                del intervals[index_to_insert-1]
                index_to_insert -= 1

        if index_to_insert > len(intervals)-1:
            intervals.insert(index_to_insert,newInterval)
            return intervals
        cur = intervals[index_to_insert]
        while overlap(cur,newInterval):
            newInterval = merge(cur,newInterval)
            del intervals[index_to_insert]
            if index_to_insert < len(intervals):
                cur = intervals[index_to_insert]
            else:
                cur = [100001,100002]
        intervals.insert(index_to_insert,newInterval)
        return intervals
