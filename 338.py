# 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        res = [0]
        cur_pow = 1
        idx = 1
        while idx <= n:
            if cur_pow == idx:
                dp[idx] = 1
            elif 2*cur_pow == idx:
                cur_pow *= 2
                dp[idx] = 1
            else:
                dp[idx] = dp[idx-cur_pow]+1
            idx += 1
        return dp
