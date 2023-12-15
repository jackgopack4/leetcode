class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # first check if we have enough gas in stations total
        if sum(gas) - sum(cost) < 0:
            return -1
        diff = [g-c for g,c in zip(gas,cost)]
        total_diff = 0
        curr_start = 0
        for i in range(len(diff)):
            total_diff += diff[i]
            if total_diff < 0:
                total_diff = 0
                curr_start = i+1
        return curr_start
