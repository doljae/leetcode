from typing import *

'''
Any live cell with fewer than two live neighbors dies as if caused by under-population.
8방으로 이웃이 2개 미만이면 죽인다
Any live cell with two or three live neighbors lives on to the next generation.
8방으로 이웃이 2개 혹은 3개면 살린다
Any live cell with more than three live neighbors dies, as if by over-population.
8방으로 이웃이 4개 이상이면 죽인다
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
8방으로 이웃이 정확히 3개면 생산한다.
'''


class Solution:
    def neighbor_num(self, x, y, board):
        xpo = [0, 0, 1, -1, 1, -1, 1, -1]
        ypo = [1, -1, 0, 0, 1, 1, -1, -1]
        answer = 0
        for i in range(8):
            new_x, new_y = x + xpo[i], y + ypo[i]
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] == 1:
                    answer += 1
        return answer

    def gameOfLife(self, board: List[List[int]]) -> None:
        born = []
        die = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                temp = self.neighbor_num(i, j, board)
                if temp == 3:
                    born.append((i, j))
                elif temp < 2:
                    die.append((i, j))
                elif temp >= 4:
                    die.append((i, j))
        # print(born, die)
        for item in born:
            x, y = item
            board[x][y] = 1
        for item in die:
            x, y = item
            board[x][y] = 0
