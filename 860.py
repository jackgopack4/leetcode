class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = [0]*2
        if bills[0] != 5:
            return False
        for b in bills:
            if b == 20: # need to give back a 10 and 2 5s or three fives
                if register[1] >=1 and register[0] >= 1:
                    register[1]-=1
                    register[0]-=1
                elif register[0]>=3:
                    register[0]-=3
                else:
                    return False
            elif b == 10:
                register[1] += 1
                if register[0] >= 1:
                    register[0]-=1
                else: 
                    return False
            else:
                register[0] += 1
        return True
