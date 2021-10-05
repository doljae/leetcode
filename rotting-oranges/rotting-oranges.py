from collections import deque
from typing import *


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        apple = []
        blank = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))
                elif grid[i][j] == 1:
                    apple.append((i, j, 0))
                elif grid[i][j] == 0:
                    blank.append((i, j, 0))

        if not rotten:
            return -1 if apple else 0

        x, y = [1, -1, 0, 0], [0, 0, 1, -1]
        q = deque(rotten)
        answer = 0
        while q:
            cx, cy, ct = q.popleft()
            answer = ct
            for i in range(4):
                nx, ny = cx + x[i], cy + y[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny, ct + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return answer
