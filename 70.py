# bottom-up DP approach
class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {1:1,2:2}
        for i in range(3,n+1):
            hashmap.update({i:(hashmap[i-1]+hashmap[i-2])})
            hashmap.pop(i-2)
        return hashmap[n]
