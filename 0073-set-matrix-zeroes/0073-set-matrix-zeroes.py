class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        
        first_row_zero = False
        first_col_zero = False

        # Check if first row has zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column has zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use first row & column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero using markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
