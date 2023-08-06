# 1041. Robot Bounded in Circle

class Solution(object):
    
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        l, r, g, turns = (0,)*4
        dir = UP
        pos = [0,0]
        for i in instructions:
            if i == 'L': 
                l+=1
                if dir == UP:
                    dir = 3
                else:
                    dir-=1
            elif i == 'R': 
                r+=1
                if dir == LEFT:
                    dir = 0
                else:
                    dir+=1
            elif i == 'G': 
                g+=1
                if dir == UP:
                    pos[1]+=1
                elif dir == RIGHT:
                    pos[0]+=1
                elif dir == DOWN:
                    pos[1]-=1
                else:
                    pos[0]-=1
        if pos == [0,0]:
            return True
        turns = abs(l-r)
        print('turns: %d' % turns)   
        if turns == 0:
            return False
        elif turns % 4 == 0:
            return False
        else: 
            return True
                
