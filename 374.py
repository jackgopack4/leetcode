import math
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        highest_low_guess = 0
        lowest_high_guess = n+1
        def guessHigher(g,n):
            return int(round(g + (lowest_high_guess-g)/2,0))
        def guessLower(g,n):
            return int(round(g-(g-highest_low_guess)/2,0))
        cur = n/2
        r = guess(cur)
        #print('r = %d, for cur = %d'%(r,cur))
        while r != 0:
            if r > 0:
                if cur > highest_low_guess:
                    highest_low_guess = cur
                cur = guessHigher(cur,n)
            else:
                if cur < lowest_high_guess:
                    lowest_high_guess = cur
                cur = guessLower(cur,n)
            r = guess(cur)
            
            #print('r = %d, for cur = %d'%(r,cur))
            #count += 1
        return int(cur)
