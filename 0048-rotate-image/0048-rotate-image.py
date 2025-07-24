class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        a=len(matrix)
        b=len(matrix[0])
        for i in range(a):
            for j in range(i+1,a):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(a):
            matrix[i].reverse()
        return matrix      