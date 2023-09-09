from collections import deque
from typing import *


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dir_x = [0, 0, 1, -1, 1, -1, 1, -1]
        dir_y = [1, -1, 0, 0, 1, -1, -1, 1]
        height, width = len(grid), len(grid[0])

        start_x, start_y = 0, 0

        if grid[start_x][start_y] != 0:
            return -1

        q = deque([(start_x, start_y, 1)])
        visited = set()

        while q:
            cur_x, cur_y, cur_len = q.popleft()

            if grid[cur_x][cur_y] != 0:
                continue

            if (cur_x, cur_y) == (height - 1, width - 1):
                return cur_len

            for i in range(8):
                new_x, new_y = cur_x + dir_x[i], cur_y + dir_y[i]
                new_len = cur_len + 1
                if 0 <= new_x < height and 0 <= new_y < width:
                    if (new_x, new_y) in visited:
                        continue

                    visited.add((new_x, new_y))
                    q.append((new_x, new_y, new_len))

        return -1