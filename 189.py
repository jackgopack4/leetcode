class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotateAmount = k % len(nums)
        res = [0]*len(nums)
        for i,n in enumerate(nums):
            new_idx = (i+rotateAmount) % len(nums)
            res[new_idx] = n
        for i,n in enumerate(res):
            nums[i] = n
