class Solution:
    def integerBreak(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            temp, board = 1, None
            if n % i == 0:
                board = [i] * (n // i)
            else:
                board = [i] * (n // i) + [n % i]

            if len(board) >= 2:
                for item in board:
                    temp *= item
                # print(board)
                result = max(result, temp)

            temp = 1
            if len(board) > 2:
                one = board[-1]
                board = board[:-1]
                board[-1] += one
                for item in board:
                    temp *= item
                # print(board)
                result = max(result, temp)

        return result
