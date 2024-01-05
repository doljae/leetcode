from collections import deque
from typing import *


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height, width = len(mat), len(mat[0])

        starts = []
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    starts.append((i, j, 0))
                else:
                    mat[i][j] = -1

        q = deque(starts)

        xs, ys = [1, -1, 0, 0], [0, 0, 1, -1]
        while q:
            cur_x, cur_y, cur_length = q.popleft()
            for i in range(4):
                new_x, new_y = cur_x + xs[i], cur_y + ys[i]
                if 0 <= new_x < height and 0 <= new_y < width:
                    if mat[new_x][new_y] == -1:
                        mat[new_x][new_y] = cur_length + 1
                        q.append((new_x, new_y, cur_length + 1))
        
        return mat
