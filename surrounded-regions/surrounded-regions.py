from collections import deque
from typing import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        height, width = len(board), len(board[0])
        visited = [[0] * width for _ in range(height)]

        def check(cx, cy):
            if cx in [0, height - 1] or cy in [0, width - 1]:
                return False
            x, y = [0, 0, 1, -1], [1, -1, 0, 0]
            for p in range(4):
                nx, ny = cx + x[p], cy + y[p]
                if not (0 <= nx < height and 0 <= ny < width):
                    return False
            return True

        def bfs(cx, cy):
            q = deque([])
            q.append((cx, cy))
            seq = [(cx, cy)]
            x, y = [0, 0, 1, -1], [1, -1, 0, 0]
            visited[cx][cy] = 1
            while q:
                cur_x, cur_y = q.popleft()

                for p in range(4):
                    nx, ny = cur_x + x[p], cur_y + y[p]
                    if not (0 <= nx < height and 0 <= ny < width):
                        continue
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] == "X":
                        continue
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    seq.append((nx, ny))
            flag = 1
            for item in seq:
                sx, sy = item
                if not check(sx, sy):
                    flag = 0
                    break
            # print(seq)
            if flag:
                for item in seq:
                    board[item[0]][item[1]] = "X"

        for i in range(height):
            for j in range(width):
                if board[i][j] == "O" and not visited[i][j]:
                    bfs(i, j)