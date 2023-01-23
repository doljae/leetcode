class Solution:
    result = 0

    def totalNQueens(self, n: int) -> int:
        vertical, left, right = [0] * n, [0] * n * 2, [0] * n * 2

        def dfs(row):
            if row == n:
                self.result += 1
                return

            for col in range(n):
                if vertical[col] or left[row + col] or right[n - 1 - col + row]:
                    continue
                vertical[col] = left[row + col] = right[n - 1 - col + row] = 1
                dfs(row + 1)
                vertical[col] = left[row + col] = right[n - 1 - col + row] = 0

        dfs(0)
        return self.result