# 13. Roman to Integer
class Solution(object):
    def __init__(self):
        self.values= {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        self.prefixes = {
            "I": ["V","X"],
            "X": ["L","C"],
            "C": ["D","M"]
        }
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = 0
        # handle case of one char
        if len(s) == 1:
            return self.values.get(s)
        else:
            skip = False
            for i in range(len(s)):
                if skip:
                    skip = False
                    continue
                if s[i] in self.prefixes and \
                    i+1<len(s) and \
                    s[i+1] in self.prefixes.get(s[i]): 
                    tmp+=(self.values.get(s[i+1])-self.values.get(s[i]))
                    skip = True
                else:
                    tmp+=self.values.get(s[i])
        return tmp

