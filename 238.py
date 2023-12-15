class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_mult = [1]*(len(nums)+1)
        for i,n in enumerate(nums):
            right_mult[i+1] = right_mult[i]*n
        left_mult = 1
        idx = len(right_mult)-1
        for n in nums[::-1]:
            right_mult[idx] = right_mult[idx-1]*left_mult
            left_mult *= nums[idx-1]
            idx -= 1
        return right_mult[1:]
