class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if reached <= nums[i] + i:
                reached = i
        return reached <= 0
