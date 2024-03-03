from collections import deque
from typing import *


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        empty, fresh, rotten = 0, 1, 2
        rottons = []
        freshes = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == rotten:
                    rottons.append((i, j, 0))
                if grid[i][j] == fresh:
                    freshes.append((i, j, 0))

        if not rottons and freshes:
            return -1

        if rottons and not freshes:
            return 0

        minute = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        q = deque(rottons)
        while q:
            cur_x, cur_y, cur_minute = q.popleft()
            minute = max(minute, cur_minute)

            for i in range(4):
                new_x, new_y = cur_x + dx[i], cur_y + dy[i]
                new_minute = cur_minute + 1

                if 0 <= new_x < height and 0 <= new_y < width:
                    if grid[new_x][new_y] == fresh:
                        grid[new_x][new_y] = rotten
                        q.append((new_x, new_y, new_minute))

        for i in range(height):
            for j in range(width):
                if grid[i][j] == fresh:
                    return -1

        return minute