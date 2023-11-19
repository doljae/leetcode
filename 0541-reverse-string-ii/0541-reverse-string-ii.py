class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        board = [s[i:i + k] for i in range(0, len(s), k)]
        for i in range(0, len(board), 2):
            if len(board[i]) <= k:
                board[i] = board[i][::-1]

        return "".join(board)