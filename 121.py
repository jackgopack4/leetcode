// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp, max_profit = 0, 1, 0
        while rp < len(prices):
            if prices[rp] > prices[lp]:
                if prices[rp]-prices[lp] > max_profit:
                    max_profit = prices[rp]-prices[lp]
                rp += 1
            else:
                lp = rp
                rp += 1
        return max_profit
