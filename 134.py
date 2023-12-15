class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # first check if we have enough gas in stations total
        if sum(gas) - sum(cost) < 0:
            return -1
        diff = [g-c for g,c in zip(gas,cost)]
        max_diffs = sorted([(v,i) for i,v in enumerate(diff) if v >= 0],reverse=True)
        max_idx = max_diffs[0][1]
        for _,i in max_diffs:
            visited = 0
            cur_gas = 0
            idx = i
            while visited < len(gas):
                cur_gas += gas[idx]
                cur_gas -= cost[idx]
                if cur_gas < 0:
                    break
                visited += 1
                if idx < len(gas)-1:
                    idx += 1
                else:
                    idx = 0
            if visited == len(gas):
                return i
        return -1
