# Longest increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            dp = [0]
            dp.extend(1 for _ in nums)
            highest = [-float('inf')]
            highest.extend(nums)
            for i in range(1,len(dp)):
                max_len = dp[0]
                highest_so_far = highest[0]
                for j in range(0,i+1):
                    if highest[j] < nums[i-1]:
                        tmp_compare = dp[j]+1
                        if tmp_compare > max_len:
                            highest_so_far = nums[i-1]
                            max_len = tmp_compare

                if max_len > 0:
                    dp[i] = max_len
                    highest[i] = highest_so_far

            return max(dp)
