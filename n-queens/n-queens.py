from typing import *


class Solution:
    answer = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.answer = []
        board = [0] * n
        cols = [0] * n
        left_div, right_div = [0] * (2 * n), [0] * (2 * n)

        def record(board):
            answer = []
            default = ["."] * len(board)
            for i in range(len(board)):
                default[board[i]] = "Q"
                answer.append("".join(default))
                default[board[i]] = "."
            return answer

        def is_possible(row, col):
            if cols[col]:
                return False
            if left_div[n - (col - row)]:
                return False
            if right_div[row + col]:
                return False
            return True

        def dfs(row):
            if row == n:
                self.answer.append(record(board))
                return
            for col in range(n):
                if is_possible(row, col):
                    board[row] = col
                    cols[col] = 1
                    left_div[n - (col - row)] = 1
                    right_div[row + col] = 1
                    dfs(row + 1)
                    cols[col] = 0
                    left_div[n - (col - row)] = 0
                    right_div[row + col] = 0

        dfs(0)
        return self.answer
