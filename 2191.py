# 2191. Sort the Jumbled Numbers
# You are given a 0-indexed integer array mapping which represents the mapping rule of a 
# shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

# The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i 
# in the integer with mapping[i] for all 0 <= i <= 9.

# You are also given another integer array nums. Return the array nums sorted in non-decreasing order 
# based on the mapped values of its elements.


class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # create new dict
        # list comprehension to add chars to dict for mapping
        mapDict = {}
        numTuples = []
        for i in range(10):
            mapDict[str(i)] = str(mapping[i])
        for i in range(0,len(nums)):
            tmpStr = str(nums[i])
            tmpArray = [char for char in tmpStr]
            mappedArray = [mapDict[char] for char in tmpArray]
            newStr = ''.join(mappedArray)
            newInt = int(newStr)
            numTuples.append((nums[i],newInt))
        sortedTuples = sorted(numTuples,key=lambda newNum: newNum[1])
        sortedList = list(zip(*sortedTuples)[0])
        return sortedList

