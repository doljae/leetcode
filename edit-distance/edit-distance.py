class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)

        board = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len(board)):
            board[i][0] = i
        for i in range(len(board[0])):
            board[0][i] = i

        for i in range(1, len(board)):
            for j in range(1, len(board[0])):
                if word1[i - 1] == word2[j - 1]:
                    board[i][j] = board[i - 1][j - 1]
                else:
                    board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

        return board[-1][-1]