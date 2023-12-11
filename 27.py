class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        array_end_idx = len(nums)-1
        i = 0
        while i <= array_end_idx:
            if nums[i] == val:
                nums[i],nums[array_end_idx] = nums[array_end_idx],nums[i]
                array_end_idx -= 1
            else:
                i += 1
        return array_end_idx + 1
