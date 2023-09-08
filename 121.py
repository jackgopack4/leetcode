// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        # highest = prices[0]
        lowest = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - lowest)
            if prices[i] < lowest:
                lowest = prices[i]
        return dp[len(prices) - 1]