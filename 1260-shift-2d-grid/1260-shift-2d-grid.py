from typing import *


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        height, width = len(grid), len(grid[0])
        k %= (height * width)
        board = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                row, col = self.shift(i, j, height, width, k)
                board[row][col] = grid[i][j]

        return board

    def shift(self, row, col, height, width, count):
        col += count
        a, b = divmod(col, width)
        row, col = (row + a) % height, b

        return (row, col)