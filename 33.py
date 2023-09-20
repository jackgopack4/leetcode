class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findRotationPoint():
            l = 0
            r = len(nums)-1
            while l < r:
                mid = l + (r+1-l)//2
                if nums[l+1]<nums[l]:
                    return l+1
                elif nums[mid]>nums[l]:
                    l = mid
                else:
                    r -= 1
            if l >= len(nums)-1:
                return -1
            else:
                return l
        def binarySearch(l:int, r:int) -> int:
            while l < r:
                mid = l+(r-l)//2
                if nums[mid] > target:
                    r = mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    return mid
            if l > r:
                return -1
            else:
                if nums[mid] != target:
                    return -1
                return mid
        rotationPoint = findRotationPoint()
        if rotationPoint == -1:
            return binarySearch(0,len(nums))
        else:
            return max(binarySearch(0,rotationPoint),binarySearch(rotationPoint,len(nums)))
            
