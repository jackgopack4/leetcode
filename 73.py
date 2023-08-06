# 73. Set Matrix Zeroes
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Strategy: hashset for columns and rows to zero
        # go through matrix once and then iterate through sets to clear out rows/cols
        rows = set()
        cols = set()

        horMin = 0
        horMax = len(matrix[0])
        vertMin = 0
        vertMax = len(matrix)
        i = horMin
        while(i<horMax):
            j = vertMin
            while(j<vertMax):
                if matrix[j][i] == 0:
                    rows.add(j)
                    cols.add(i)
                j+=1
            i+=1
        for row in rows:
            matrix[row] = [0]*horMax
        for col in cols:
            for k in range(0,vertMax):
                matrix[k][col] = 0
