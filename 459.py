# 459. Repeated Substring Pattern
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)-1,0,-1):
            if len(s) % i == 0:
                # divisible length; check for substring
                j = i
                substr = s[0:i]
                while j < len(s):
                    if s[j:j+i] != substr:
                        break
                    j+=i
                    if j == len(s):
                        return True
        return False
