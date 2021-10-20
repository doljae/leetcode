from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        height, width = len(board), len(board[0])
        x, y = [0, 0, 1, -1], [1, -1, 0, 0]
        visited = [[0] * width for _ in range(height)]
        flag = False

        def reset_visited():
            return [[0] * width for _ in range(height)]

        def dfs(cur_x, cur_y, cur_index):
            nonlocal flag
            visited[cur_x][cur_y] = 1

            if cur_index == len(word) - 1:
                flag = True
                return

            for i in range(4):
                new_x, new_y = cur_x + x[i], cur_y + y[i]
                if 0 <= new_x < height and 0 <= new_y < width:
                    if not visited[new_x][new_y] and board[new_x][new_y] == word[cur_index + 1]:
                        dfs(new_x, new_y, cur_index + 1)

            visited[cur_x][cur_y] = 0

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
                    if flag:
                        return True
                    visited = reset_visited()
        return False
