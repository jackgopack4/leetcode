class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # any space can only be reached by down or right
        # need to take number of ways to get to space to left plus
        # number of ways to get to space above
        # idea: loop through each row, updating DP matrix
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,n+1):
            dp[1][i] = 1
        for j in range(1,m+1):
            dp[j][1] = 1
        #print(f"m={len(dp)}")
        #print(f"n={len(dp[0])}")
        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
