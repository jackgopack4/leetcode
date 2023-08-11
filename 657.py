class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lateralMoves = 0
        verticalMoves = 0
        for x in moves:
            match x:
                case 'R':
                    lateralMoves+=1
                case 'L':
                    lateralMoves-=1
                case 'U':
                    verticalMoves+=1
                case 'D':
                    verticalMoves-=1
        return lateralMoves == 0 and verticalMoves == 0
