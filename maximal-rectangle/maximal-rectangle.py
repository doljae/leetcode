from typing import *


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        height, width = len(matrix), len(matrix[0])

        dp = [[0] * width for _ in range(height)]

        for i in range(height):
            temp = 0
            for j in range(width):
                if matrix[i][j] == "1":
                    temp += 1
                else:
                    temp = 0
                dp[i][j] = temp

        answer = 0
        for i in reversed(range(height)):
            for j in reversed(range(width)):
                row, col = dp[i][j], 0
                k = i
                while k >= 0 and dp[k][j]:
                    row = min(row, dp[k][j])
                    col += 1
                    answer = max(answer, row * col)
                    k -= 1

        return answer