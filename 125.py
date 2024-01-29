# Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower_list = [c.lower() for c in s if c.isalnum()]
        lp = 0
        rp = len(s_lower_list)-1
        while lp < rp:
            if s_lower_list[lp] != s_lower_list[rp]:
                return False
            lp += 1
            rp -= 1
        return True
