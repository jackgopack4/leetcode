class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        def findLeft(n:int)->int:
            l = 0
            r = len(self.nums)
            while l < r:
                mid = l + (r-l) // 2
                if nums[mid] < n:
                    l = mid+1
                else:
                    r = mid
            return l

        l = findLeft(target)
        r = findLeft(target+1)-1
        if l <= r:
            return [l,r]
        else:
            return [-1,-1]
