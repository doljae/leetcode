from typing import *
from heapq import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        t_x, t_y = len(grid) - 1, len(grid[0]) - 1
        height, width = t_x + 1, t_y + 1
        dist = [[float("inf")] * width for _ in range(height)]
        dist[0][0] = 0
        # 마지막에 시작점 dist 더해야함
        q = [(0, 0, 0)]
        while q:
            cur_length, cur_x, cur_y = heappop(q)
            if dist[cur_x][cur_y] < cur_length:
                continue
            r_x, r_y = cur_x, cur_y + 1
            if 0 <= r_x < height and 0 <= r_y < width:
                new_length = cur_length + grid[r_x][r_y]
                if dist[r_x][r_y] > new_length:
                    dist[r_x][r_y] = new_length
                    heappush(q, (new_length, r_x, r_y))

            d_x, d_y = cur_x + 1, cur_y
            if 0 <= d_x < height and 0 <= d_y < width:
                new_length = cur_length + grid[d_x][d_y]
                if dist[d_x][d_y] > new_length:
                    dist[d_x][d_y] = new_length
                    heappush(q, (new_length, d_x, d_y))
            # for item in dist:
            #     print(item)
            # print()
        return dist[t_x][t_y] + grid[0][0]