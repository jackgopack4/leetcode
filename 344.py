# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        max = (len(s)) // 2
        for i in range(max):
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
        return s
