# do it without counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n]+=1
        return [key for key, val in sorted(seen.items(), key=lambda item: item[1],reverse=True)][0:k]
