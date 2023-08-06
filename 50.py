# 50. Pow
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0.0
        if n < 0:
            x = 1/x
            n = abs(n)
        res = 1.0
        while n > 0:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
