class Solution:
    def uniquePaths(self, height: int, width: int) -> int:
        board = [[0] * width for _ in range(height)]
        for i in range(height):
            board[i][0] = 1
        for i in range(width):
            board[0][i] = 1

        for i in range(1, height):
            for j in range(1, width):
                board[i][j] = board[i - 1][j] + board[i][j - 1]
        return board[-1][-1]
