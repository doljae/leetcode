from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = 0, len(matrix[0]) - 1
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            temp = matrix[row][col]
            if temp == target:
                return True
            elif temp > target:
                col -= 1
            elif temp < target:
                row += 1
        return False