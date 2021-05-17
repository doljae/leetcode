from collections import deque
from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        height, width = len(grid), len(grid[0])
        visited = [[0] * width for _ in range(height)]

        def bfs(x, y):
            visited[x][y] = 1
            q = deque([(x, y)])
            xpo, ypo = [1, -1, 0, 0], [0, 0, 1, -1]
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    new_x, new_y = cur_x + xpo[i], cur_y + ypo[i]
                    if 0 <= new_x < height and 0 <= new_y < width:
                        if not visited[new_x][new_y] and grid[new_x][new_y] == "1":
                            visited[new_x][new_y] = 1
                            q.append((new_x, new_y))

        for i in range(height):
            for j in range(width):
                if not visited[i][j] and grid[i][j] == "1":
                    answer += 1
                    bfs(i, j)
        return answer