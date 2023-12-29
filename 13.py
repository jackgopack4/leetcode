# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {'I':1, 'IV':4, 'V':5, 'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        total = 0
        idx = 0
        while idx < len(s):
            if idx < len(s)-1 and s[idx:idx+2] in mappings:
                total += mappings[s[idx:idx+2]]
                idx += 2
            else:
                total += mappings[s[idx]]
                idx += 1
        return total
