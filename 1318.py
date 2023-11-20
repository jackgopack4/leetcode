# 1318. Minimum Flips to Make a OR b Equal to c
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a | b == c:
            return 0
        num_bits = 0
        while a>0 or b> 0 or c> 0:
            a_lowest_bit = a & 0x1
            b_lowest_bit = b & 0x1
            c_lowest_bit = c & 0x1
            if c_lowest_bit & ~(a_lowest_bit | b_lowest_bit):
                num_bits += 1
            elif ~c_lowest_bit & (a_lowest_bit & b_lowest_bit):
                num_bits += 2
            elif ~c_lowest_bit & (a_lowest_bit | b_lowest_bit):
                num_bits += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1

        return num_bits
