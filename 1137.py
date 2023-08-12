class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(n+1):
            if i == 0:
                dp[i] = 0
            elif i < 3:
                dp[i] = 1
            elif i == 3:
                dp[i] = 2
            else:
                dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp)
        return dp[n]
