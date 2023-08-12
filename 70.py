# bottom-up DP approach, list based
class Solution:
    def climbStairs(self, n: int) -> int:
        list = [1,2]
        for i in range(2,n):
            list.append(list[i-1]+list[i-2])
        return list[n-1]
