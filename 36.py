from collections import deque
class Solution:
    def isValidSudoku(self, board):
        res = deque()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res.extend([(i, element), (element, j), (i // 3, j // 3, element)])
        return len(res) == len(set(res))
