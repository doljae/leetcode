class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board, cols = [0] * n, [0] * n
        left_div, right_div = [0] * (2 * n), [0] * (2 * n)

        def is_possible(row, col):
            if cols[col]:
                return False
            if left_div[n - (col - row)]:
                return False
            if right_div[row + col]:
                return False
            return True

        def dfs(row):
            nonlocal res
            
            if row == n:
                res += 1
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
        return res