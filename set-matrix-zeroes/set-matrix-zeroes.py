from typing import *


def set_row(board, row):
    board[row] = [1] * len(board[row])


def set_col(board, col):
    for row in range(len(board)):
        board[row][col] = 1


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        board = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    set_row(board, row)
                    set_col(board, col)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if board[row][col] == 1:
                    matrix[row][col] = 0