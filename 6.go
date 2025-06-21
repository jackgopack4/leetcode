func convert(s string, numRows int) string {
    // store this in 2D array then traverse
    // 1 column for numRows, plus numRows - 2 columns for (2*numrows-2) chars
    // len(s) % (2*numrows-2) decides how many extra chars
    // numRows or les = 1 extra col, greater than numRows = one extra column each
    if numRows == 1 || len(s) <= numRows {
        return s
    }
    matrix := allocateMatrix(len(s), numRows)
    movingDown := true // flip to false when moving up/diagonal
    x, y := 0, 0
    for _, c := range s {
        (*matrix)[y][x] = c
        if y == numRows - 1 {
            movingDown = false
        } else if y == 0 && x > 0 {
            movingDown = true
        }
        if movingDown {
            y += 1
        } else {
            x += 1
            y -= 1
        }
    }
    return traverseMatrix(len(s), matrix)
}

func traverseMatrix(stringLen int, matrix *[][]int32) string {
    arr := make([]int32, stringLen)
    pos := 0
    for i:=0; i<len(*matrix); i++ {
        for _, c := range (*matrix)[i] {
            if c != int32(0) {
                arr[pos] = c
                pos += 1
            }
        }
    }
    return string(arr)
}

func allocateMatrix(stringLen int, numRows int) *[][]int32 {
    columnsPerBlock := numRows - 1
    numBlocks := stringLen / (2 * numRows - 2)
    if stringLen % (2 * numRows - 2) > 0 {
        numBlocks += 1
    }
    numCols := numBlocks * columnsPerBlock
    modulo := numBlocks % (2 * numRows - 2)
    if modulo > 0 {
      numCols += 1
    }
    if modulo > numRows {
      numCols += modulo % numRows  
    }
    matrix := make([][]int32, numRows)
    for i := range matrix {
        matrix[i] = make([]int32, numCols)
    }
    return &matrix
}
