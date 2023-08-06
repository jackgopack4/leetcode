# 389. Find the Difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sDict = {}
        tDict = {}
        for x in s:
            if x not in sDict:
                sDict[x] = 0
            else:
                sDict[x] = sDict[x]+1
        for x in t:
            if x not in sDict:
                return x
            else:
                if x not in tDict:
                    tDict[x] = 0
                else:
                    tDict[x] = tDict[x]+1
                if tDict[x] > sDict[x]:
                    return x
        return ""
