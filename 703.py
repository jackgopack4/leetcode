import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.klargest = []
        heapify(self.klargest)
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        tmp = val + 10001
        heappush(self.klargest,tmp)
        if len(self.klargest) > self.k:
            heappop(self.klargest)
        return self.klargest[0]-10001


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
