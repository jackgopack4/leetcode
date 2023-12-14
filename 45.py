class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        farthest = 0
        current = 0
        steps = 1
        for i in range(len(nums)):
            tmp = farthest
            farthest = max([nums[j]+j for j in range(current,farthest+1)])
            if farthest >= len(nums)-1:
                return steps
            steps += 1
            current = tmp
        return steps
