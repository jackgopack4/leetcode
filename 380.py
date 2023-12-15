from random import randrange
class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.keys = []

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.keys.append(val)
            self.data[val] = len(self.keys)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            last_element, idx = self.keys[-1],self.data[val]
            self.keys[idx],self.data[last_element] = last_element,idx
            self.keys.pop()
            del self.data[val]
            return True
        return False

    def getRandom(self) -> int:
        size = len(self.keys)
        return self.keys[randrange(size)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
