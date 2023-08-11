class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        aMoves = [x for ind, x in enumerate(moves) if ind % 2 == 0]
        bMoves = [x for ind, x in enumerate(moves) if ind % 2 == 1]
        aXMoves = [x[0] for ind, x in enumerate(moves) if ind % 2 == 0]
        aYMoves = [x[1] for ind, x in enumerate(moves) if ind % 2 == 0]
        bXMoves = [x[0] for ind, x in enumerate(moves) if ind % 2 == 1]
        bYMoves = [x[1] for ind, x in enumerate(moves) if ind % 2 == 1]
        #print(aMoves)
        #print(bMoves)
        if aXMoves.count(0) == 3 or aXMoves.count(1) == 3 or aXMoves.count(2) == 3 or aYMoves.count(0) == 3 or aYMoves.count(1) == 3 or aYMoves.count(2) == 3:
            return "A"
        elif bXMoves.count(0) == 3 or bXMoves.count(1) == 3 or bXMoves.count(2) == 3 or bYMoves.count(0) == 3 or bYMoves.count(1) == 3 or bYMoves.count(2) == 3:
            return "B"
        elif [1,1] in aMoves and ([0,0] in aMoves and [2,2] in aMoves or \
            [0,2] in aMoves and [2,0] in aMoves):
            return "A"
        elif [1,1] in bMoves and ([0,0] in bMoves and [2,2] in bMoves or \
            [0,2] in bMoves and [2,0] in bMoves):
            return "B"
        elif len(moves) < 9:
            return "Pending"
        else:
            return "Draw"
