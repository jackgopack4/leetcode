# 2336. Smallest Number in Infinite Set
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

class SmallestInfiniteSet(object):
    # One-hot vector implementation for removed items that grows only when items are removed
    def __init__(self):
        self.removed = []
        self.smallest = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        res = self.smallest
        if len(self.removed) < res:
            self.removed.append(True)
        else:
            self.removed[res-1] = True
        i = res
        while i < len(self.removed):
            if not self.removed[i]:
                break
            i+=1
        self.smallest=i+1
        return res
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num <= len(self.removed):
            if self.removed[num-1]:
                self.removed[num-1] = False
                if num < self.smallest:
                    self.smallest = num
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
