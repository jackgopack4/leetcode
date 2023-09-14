from collections import deque
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.klargest = sorted(nums,reverse=True)[0:k][::-1]
        self.klargest = [c+10001 for c in self.klargest]
        heapify(self.klargest)

    def add(self, val: int) -> int:
        addedKth = False
        if len(self.klargest)< self.k:
            addedKth = True
            heappush(self.klargest,val+10001)
        smallest = self.klargest[0]
        if val+10001 < smallest:
            return smallest-10001
        else:
            if len(self.klargest) >= self.k and not addedKth:
                heapreplace(self.klargest,val+10001)
            return self.klargest[0]-10001
         


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
