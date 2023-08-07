# Runtime Details
# 14ms
# Beats 99.34% of users with Python
# Memory Details
# 13.17mb
# Beats 99.51% of users with Python

# 1502. Can Make Arithmetic Progression From Sequence
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        itemSet = set()
        length = len(arr)
        smallest = 1000001
        largest = -1000001

        for x in arr:
            if x > largest:
                largest = x
            if x < smallest:
                smallest = x

        if (largest - smallest) % (length-1) != 0:
            return False
        distance = (largest - smallest) / (length-1)

        for x in arr:
            if x not in itemSet:
                itemSet.add(x)
            else:
                if distance != 0:
                    return False

        for x in arr:
            if x != smallest and x != largest:
                if (( x - distance ) not in itemSet) or \
                        ((x + distance ) not in itemSet):
                    return False
        return True
