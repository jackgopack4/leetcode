class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            tmp = target - n
            if tmp in seen:
                res = [seen[tmp],i]
                seen.clear()
                return res
            else:
                seen[n] = i
        return [-1,-1]
