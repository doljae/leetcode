from collections import deque
from typing import *


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1] == 1:
            return -1

        x = [-1, -1, -1, 0, 1, 1, 1, 0]
        y = [-1, 0, 1, 1, 1, 0, -1, -1]
        height, width = len(grid), len(grid[0])
        visited = [[0] * width for _ in range(height)]
        visited[0][0] = 1
        q = deque([(0, 0, 1)])

        while q:
            cur_x, cur_y, cur_length = q.popleft()
            if cur_x == height - 1 and cur_y == width - 1:
                return cur_length

            for i in range(8):
                nx, ny = cur_x + x[i], cur_y + y[i]
                if not 0 <= nx < height or not 0 <= ny < width:
                    continue
                if visited[nx][ny]:
                    continue
                if grid[nx][ny] == 1:
                    continue
                visited[nx][ny] = 1
                q.append((nx, ny, cur_length + 1))

        return -1
