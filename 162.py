class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def checkNeighbors(i:int):
            if i == 0:
                return nums[i] > nums[i+1]
            elif i == len(nums)-1:
                return nums[i] > nums[i-1]
            else:
                return nums[i-1] < nums[i] > nums[i+1]
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if checkNeighbors(0):
                return 0
            else:
                return 1

        l = 0 
        r = len(nums)
        mid = (l + r) // 2
        while not checkNeighbors(mid):
            mid = (l + r) // 2
            if nums[mid-1] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return mid
