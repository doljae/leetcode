from collections import deque
from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        height, width = len(grid), len(grid[0])
        answer = 0
        visited = [[0] * width for _ in range(height)]
        p, q = [1, -1, 0, 0], [0, 0, 1, -1]

        def dfs(x, y):
            visited[x][y] = 1
            if grid[x][y] == "0":
                return 0

            queue = deque([(x, y)])

            while queue:
                cx, cy = queue.popleft()

                for z in range(4):
                    nx, ny = cx + p[z], cy + q[z]
                    if 0 <= nx < height and 0 <= ny < width:
                        if not visited[nx][ny] and grid[nx][ny] == "1":
                            visited[nx][ny] = 1
                            queue.append((nx, ny))

            return 1

        for i in range(height):
            for j in range(width):
                if not visited[i][j]:
                    answer += dfs(i, j)

        return answer