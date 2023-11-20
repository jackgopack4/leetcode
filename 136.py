# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = 0
        for n in nums:
            tmp ^= n
        return tmp
