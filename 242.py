from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        for char in t:
            if char not in s_dict:
                return False
            else:
                if s_dict[char] > 1:
                    s_dict[char] -= 1
                else:
                    s_dict.pop(char)
        return True
