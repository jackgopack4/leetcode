# 12. Integer to Roman
'''
Runtime Details
49ms
Beats 91.66% of users with Python3
Memory Details
16.14mb
Beats 98.89% of users with Python3
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        numeralsDict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", \
                    40: "XL", 50: "L", 90: "XC", 100: "C", \
                    400: "CD", 500: "D", 900: "CM", 1000: "M"}
        numeralsList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, \
                        5, 4, 1]
        tmp = num
        res = ""
        idx = 0
        while (tmp != 0):
            if numeralsList[idx] <= tmp:
                res += numeralsDict[numeralsList[idx]]
                tmp -= numeralsList[idx]
            else:
                idx += 1
        return res
