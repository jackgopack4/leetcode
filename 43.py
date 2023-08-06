# 43. Multiply Strings

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = 0
        n2 = 0
        multiplier = 1
        for i in range(len(num1),0,-1):
            n1 += (int(num1[i-1]) * multiplier)
            multiplier *= 10
        multiplier = 1
        for i in range(len(num2),0,-1):
            n2 += (int(num2[i-1]) * multiplier)
            multiplier *= 10
        resInt = n1 * n2
        return str(resInt)
