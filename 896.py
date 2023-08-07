# Runtime Details
# 727ms
# Beats 98.78% of users with Python
# Memory Details
# 23.76mb
# Beats 93.15% of users with Python

# 896. Monotonic Array

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 1:
            return True

        changedYet = False
        increasing = False
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > prev:
                if not changedYet:
                    changedYet = True
                    increasing = True
                else:
                    if not increasing:
                        return False
            elif nums[i] < prev:
                if not changedYet:
                    changedYet = True
                    # increasing = False set by default
                else:
                    if increasing:
                        return False
            prev = nums[i]
        return True
