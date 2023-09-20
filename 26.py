class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 0
        rp = 1
        k = 1
        while rp < len(nums):
            if nums[rp] > nums[lp]:
                lp += 1
                nums[lp] = nums[rp]
                k += 1
            rp += 1
        return k
