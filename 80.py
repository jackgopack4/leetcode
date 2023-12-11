class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 0
        rp = 1
        dups = 0
        k = 1
        while rp < len(nums):
            if nums[rp] == nums[lp] and dups == 0:
                dups += 1
                lp += 1
                nums[lp] = nums[rp]
                k += 1
            elif nums[rp] > nums[lp]:
                dups = 0
                lp += 1
                nums[lp] = nums[rp]
                k += 1
            rp += 1
        return k
