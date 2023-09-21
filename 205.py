from collections import deque
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        s_array = deque()
        t_array = deque()
        s_count = 0
        t_count = 0
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = s_count
                s_count += 1
            if t[i] not in t_dict:
                t_dict[t[i]] = t_count
                t_count += 1
            if s_count != t_count:
                return False
            s_array.append(s_dict[s[i]])
            t_array.append(t_dict[t[i]])
        s_dict.clear()
        t_dict.clear()
        return s_array == t_array
