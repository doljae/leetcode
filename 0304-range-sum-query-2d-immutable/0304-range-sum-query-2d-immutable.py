from typing import *


class NumMatrix:
    matrix: List[List[int]]

    def __init__(self, matrix: List[List[int]]):
        width, height = len(matrix[0]), len(matrix)
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col - 1]
        for row in range(1, len(matrix)):
            for col in range(width):
                matrix[row][col] += matrix[row - 1][col]

        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.matrix[row2][col2]
        if row1 - 1 >= 0:
            result -= self.matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            result -= self.matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            result += self.matrix[row1 - 1][col1 - 1]
        return result