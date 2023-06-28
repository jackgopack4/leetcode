# 1342. Number of Steps to Reduce a Number to Zero
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        cur = num
        steps = 0
        while cur > 0:
            if cur % 2 == 0: 
                cur = cur/2
            else:
                cur = cur-1
            steps = steps + 1
        return steps
