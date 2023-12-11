# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        prev = float('inf')
        for p in prices:
            if p < prev:
                prev = p
            elif p - prev > maxProfit:
                maxProfit = p - prev
        return maxProfit
