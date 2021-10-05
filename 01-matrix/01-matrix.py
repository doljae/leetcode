from collections import deque
from typing import *


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        answer = [[-1] * len(mat[0]) for _ in range(len(mat))]

        candi = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    candi.append((i, j, 0))
                    answer[i][j] = 0

        q = deque(candi)

        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        while q:
            cur_x, cur_y, cur_length = q.popleft()

            for i in range(4):
                nx, ny = cur_x + x[i], cur_y + y[i]
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    if answer[nx][ny] == -1:
                        answer[nx][ny] = cur_length + 1
                        q.append((nx, ny, cur_length + 1))

        return answer
