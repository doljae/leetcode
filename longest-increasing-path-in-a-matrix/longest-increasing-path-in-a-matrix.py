from typing import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        height, width = len(matrix), len(matrix[0])
        cache = [[0] * width for _ in range(height)]
        xpo, ypo = [0, 0, 1, -1], [1, -1, 0, 0]
        answer = 0

        def dfs(cx, cy):
            cache[cx][cy] = 1

            for p in range(4):
                nx, ny = cx + xpo[p], cy + ypo[p]
                if 0 <= nx < height and 0 <= ny < width:
                    if matrix[nx][ny] > matrix[cx][cy]:
                        if not cache[nx][ny]:
                            cache[cx][cy] = max(cache[cx][cy], dfs(nx, ny) + 1)
                        else:
                            cache[cx][cy] = max(cache[cx][cy], cache[nx][ny] + 1)
            return cache[cx][cy]

        for i in range(height):
            for j in range(width):
                if not cache[i][j]:
                    answer = max(answer, dfs(i, j))
        for item in cache:
            print(item)
        print()
        return answer
