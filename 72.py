class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for w2idx in range(1,len(dp[0])):
            dp[0][w2idx] = w2idx
        for w1idx in range(1,len(dp)):
            dp[w1idx][0] = w1idx
        for w1idx in range(1,len(dp)):
            for w2idx in range(1,len(dp[0])):
                if word1[w1idx-1] == word2[w2idx-1]:
                    dp[w1idx][w2idx] = dp[w1idx-1][w2idx-1]
                else:
                    dp[w1idx][w2idx] = min(
                        dp[w1idx-1][w2idx],
                        dp[w1idx][w2idx-1],
                        dp[w1idx-1][w2idx-1]
                    )+1
        return dp[len(word1)][len(word2)]
