class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1:
            if (high-low+1) % 2 == 1:
                return (high - low + 1) // 2 + 1
            else:
                return (high - low + 1) // 2
        else: # even first
            return (high - low + 1) // 2
