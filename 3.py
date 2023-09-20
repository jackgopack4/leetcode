class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        seen = {}
        max_len = 0
        for rp in range(len(s)):
            if s[rp] not in seen:
                max_len = max(max_len,rp-lp+1)
            else:
                if seen[s[rp]] < lp:
                    max_len = max(max_len,rp-lp+1)
                else:
                    lp = seen[s[rp]]+1
            seen[s[rp]] = rp
        return max_len
