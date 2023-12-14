class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps_remaining = [float('inf')]*len(nums)
        jumps_remaining[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= (len(nums) - 1): # we can reach end in one jump
                jumps_remaining[i] = 1
            else:
                for j in range(i+1,i+nums[i]+1):
                    if jumps_remaining[j]+1 < jumps_remaining[i]:
                        jumps_remaining[i] = jumps_remaining[j]+1
        return int(jumps_remaining[0])
