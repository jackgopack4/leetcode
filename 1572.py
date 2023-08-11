class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dimension = len(mat)
        result = 0
        for i in range(dimension):
            for j in range(dimension):
                if i == j:
                    result+=mat[i][j]
                elif i+j == dimension-1:
                    result+=mat[i][j]
        return result
