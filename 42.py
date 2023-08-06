# 42. Trapping Rain Water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        leftMax = [0]*length
        rightMax = [0]*length

        for i in range(length):
            if (i-1) >= 0:
                if height[i-1] > leftMax[i] and height[i-1]>leftMax[i-1]:
                    leftMax[i] = height[i-1]
                else:
                    leftMax[i] = leftMax[i-1]
        for i in range(length-1,-1,-1):
            if (i+1) <= length-1:
                if height[i+1] > rightMax[i] and height[i+1] > rightMax[i+1]:
                    rightMax[i] = height[i+1]
                else:
                    rightMax[i] = rightMax[i+1]
        maxIndices = [min(i) for i in zip(leftMax,rightMax)]
        res = sum([i[1]-i[0] for i in zip(height,maxIndices) if i[1]>i[0]])
        return res
