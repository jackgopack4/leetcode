import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        req_avg_speed = math.ceil(sum(piles)/h)
        l = req_avg_speed
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            time_needed = 0
            for p in piles:
                time_needed += math.ceil(p / mid)
                if time_needed > h:
                    break
            if time_needed <= h:
                r = mid
            else:
                l = mid + 1
        return l
