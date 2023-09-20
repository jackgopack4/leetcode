# valid sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = set(["0","1","2","3","4","5","6","7","8","9"])
        def validBox(top_left:(int,int)) -> bool:
            seen = set()
            x,y = top_left
            for i in range(y,y+3):
                for j in range(x,x+3):
                    if board[i][j] in numbers:
                        if board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])
            return True
        def validRow(top_left:int) -> bool:
            seen = set()
            i = top_left
            for j in range(9):
                if board[i][j] in numbers:
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
            return True
        def validColumn(top_left:int) -> bool:
            seen = set()
            j = top_left
            for i in range(9):
                if board[i][j] in numbers:
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
            return True
        for i in range(9):
            if not validRow(i):
                return False
        for j in range(9):
            if not validColumn(j):
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not validBox((j,i)):
                    return False
        return True


        
