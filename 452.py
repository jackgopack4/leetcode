class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #points.sort(key=lambda x:x[1])
        points = sorted(points, key=lambda x:x[1])
        latestSeen = -float('inf')
        arrows = 0
        for start, end in points:
            if start > latestSeen:
                arrows += 1
                latestSeen = end
        return arrows
