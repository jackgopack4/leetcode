# 1822. Sign of the Product of an Array
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        for x in nums:
            if x == 0:
                return 0
            elif x < 0:
                res = -res
        return res
