# 283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = [i for i, x in enumerate(nums) if x == 0]
        print(zeros)
        for i in range(len(zeros)-1,-1,-1):
            nums.pop(zeros[i])
        nums.extend([0]*len(zeros))
