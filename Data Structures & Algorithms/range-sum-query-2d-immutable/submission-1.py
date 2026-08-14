from copy import deepcopy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._2d_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(1,len(self._2d_matrix)):
            for c in range(1,len(self._2d_matrix[0])):
                self._2d_matrix[r][c] = matrix[r-1][c-1]
                self._2d_matrix[r][c] = self._2d_matrix[r][c-1] + self._2d_matrix[r][c] + self._2d_matrix[r-1][c] - self._2d_matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._2d_matrix[row2 + 1][col2 + 1] - self._2d_matrix[row1][col2+1] - self._2d_matrix[row2+1][col1] + self._2d_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)