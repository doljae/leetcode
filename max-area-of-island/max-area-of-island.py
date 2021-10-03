from collections import deque
from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x, y = [0, 0, 1, -1], [1, -1, 0, 0]
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        answer = 0

        def bfs(cur_x, cur_y):
            visited[cur_x][cur_y] = 1
            temp = 1
            q = deque([(cur_x, cur_y)])

            while q:
                cx, cy = q.popleft()

                for i in range(4):
                    nx, ny = cx + x[i], cy + y[i]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        if not visited[nx][ny] and grid[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            temp += 1

            return temp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    cur_island_size = bfs(i, j)
                    answer = max(answer, cur_island_size)

        return answer
