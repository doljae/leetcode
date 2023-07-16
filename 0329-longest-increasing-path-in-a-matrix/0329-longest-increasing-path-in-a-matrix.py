from typing import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height, width = len(matrix), len(matrix[0])
        cache = [[0] * width for _ in range(height)]
        nx = [1, -1, 0, 0]
        ny = [0, 0, 1, -1]

        def dfs(x, y):
            cache[x][y] = 1

            for i in range(4):
                new_x, new_y = x + nx[i], y + ny[i]
                if 0 <= new_x < height and 0 <= new_y < width:
                    if matrix[new_x][new_y] > matrix[x][y]:
                        if not cache[new_x][new_y]:
                            cache[x][y] = max(dfs(new_x, new_y) + 1, cache[x][y])
                        else:
                            cache[x][y] = max(cache[new_x][new_y] + 1, cache[x][y])

            return cache[x][y]

        result = 0
        for i in range(height):
            for j in range(width):
                if not cache[i][j]:
                    result = max(result, dfs(i, j))

        return result
