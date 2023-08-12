class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # i, how many multiplications done
        # left, how many left operations done (also index for left side)
        # (i - left) how many right operations done
        # right = n - 1- (i - left), index for right side

        memo = {}

        def dp(i, left):
            if i == len(multipliers):
                if (i,left) not in memo:
                    memo[(i,left)] = 0
                return memo[(i,left)]
            else:
                right = len(nums) - 1 - (i - left)
                if (i+1,left+1) not in memo:
                    memo[(i+1,left+1)] = dp(i+1,left+1)
                if (i+1,left) not in memo:
                    memo[(i+1,left)] = dp(i+1,left)
                if (i,left) not in memo:
                    memo[(i,left)] = max(nums[left]*multipliers[i]+memo[(i+1,left+1)], \
                        nums[right]*multipliers[i] + memo[(i+1,left)])
                return memo[(i,left)]
        return dp(0,0)
                
                
