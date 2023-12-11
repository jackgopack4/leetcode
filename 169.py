import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        numsLen = len(nums)
        majorityAmount = math.floor(numsLen / 2)
        for n in nums:
            if counts.get(n) is None:
                counts[n] = 1
            else:
                counts[n] += 1
            if counts[n] > majorityAmount:
                return n
        return -1
