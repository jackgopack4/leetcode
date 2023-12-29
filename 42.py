# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        # idea - go from L to R, measuring max based on left height
        # left pass
        if len(height) <= 2:
            return 0
        maxHeight = 0
        maxHeld = [0]*len(height)
        for i in range(0,len(height)):
            if height[i] < maxHeight:
                maxHeld[i] = maxHeight-height[i]
            else:
                maxHeight = height[i]

        maxHeight = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] < maxHeight:
                maxHeld[i] = min(maxHeight-height[i],maxHeld[i])
            else:
                maxHeight = height[i]
                maxHeld[i] = 0

        return sum(maxHeld)
