# 2336. Smallest Number in Infinite Set
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

class SmallestInfiniteSet(object):
    # faster version using a hashset and heap combo; only add when adding back below current minimum
    def __init__(self):
        self.addedList = []
        self.addedSet = set()
        self.smallest = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.addedList) == 0:
            res = self.smallest
            self.smallest +=1
        else:
            res = heapq.heappop(self.addedList)
            self.addedSet.remove(res)
        return res

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.smallest and num not in self.addedSet:
            heapq.heappush(self.addedList,num)
            self.addedSet.add(num)
        
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
