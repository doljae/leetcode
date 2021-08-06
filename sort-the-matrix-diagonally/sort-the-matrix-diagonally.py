from typing import *


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return None

        height, width = len(mat), len(mat[0])
        xpo, ypo = 0, width - 1

        # to left
        while ypo >= 0:
            cur_x, cur_y = xpo, ypo
            temp = []
            while cur_x < height and cur_y < width:
                temp.append(mat[cur_x][cur_y])
                cur_x, cur_y = cur_x + 1, cur_y + 1
            temp.sort()
            cur_x, cur_y = xpo, ypo
            index = 0
            while cur_x < height and cur_y < width:
                mat[cur_x][cur_y] = temp[index]
                cur_x, cur_y, index = cur_x + 1, cur_y + 1, index + 1
            ypo -= 1

        xpo, ypo = 0, 0
        # to down
        while xpo < height:
            cur_x, cur_y = xpo, ypo
            temp = []
            while cur_x < height and cur_y < width:
                temp.append(mat[cur_x][cur_y])
                cur_x, cur_y = cur_x + 1, cur_y + 1
            temp.sort()
            cur_x, cur_y = xpo, ypo
            index = 0
            while cur_x < height and cur_y < width:
                mat[cur_x][cur_y] = temp[index]
                cur_x, cur_y, index = cur_x + 1, cur_y + 1, index + 1
            xpo += 1
        
        return mat