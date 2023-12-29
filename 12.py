class Solution:
    def intToRoman(self, num: int) -> str:
        substrings = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        res = ""
        s_idx = 0
        while num > 0:
            while substrings[s_idx][0] <= num:
                res+=substrings[s_idx][1]
                num -= substrings[s_idx][0]
            s_idx += 1
        return res
