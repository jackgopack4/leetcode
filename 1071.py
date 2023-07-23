# 1071. Greatest Common Divisor of Strings

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) > len(str2):
            shorter = str2
            longer = str1
        else:
            shorter = str1
            longer = str2
        substr = shorter
        match = False
        while len(substr) > 0 and match == False:
            match = False
            if len(str2) % len(substr) == 0 and len(str1) % len(substr) == 0:
                # can attempt matching
                i = 0
                match = True
                while i+len(substr) <= len(str1):
                    if substr != str1[i:i+len(substr)]:
                        match = False
                        break
                    i+=len(substr)
                i = 0
                while i+len(substr) <= len(str2):
                    if substr != str2[i:i+len(substr)]:
                        match = False
                        break
                    i+=len(substr)
            if match == False: 
                substr = substr[:-1]
        return substr
                
