# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0;
        j = len(s)-1;
        while i < j:
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            i+=1;
            j-=1;
