# 380. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x not in sDict:
                sDict[x] = 0
            else:
                sDict[x] = sDict[x]+1
        for x in t:
            if x not in sDict:
                return False
            else:
                if x not in tDict:
                    tDict[x] = 0
                else:
                    tDict[x] = tDict[x]+1
                if tDict[x] > sDict[x]:
                    return False
        return True
        
