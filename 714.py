class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold_var = -prices[0]
        free_var = 0

        for i in range(1,len(prices)):
            free_var = max(free_var,hold_var+prices[i]-fee)
            hold_var = max(hold_var,free_var-prices[i])
        return max(free_var,hold_var)
                
