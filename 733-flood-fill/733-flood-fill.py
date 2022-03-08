from collections import deque
from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        target_color = image[sr][sc]
        height, width = len(image), len(image[0])
        areas = [(sr, sc)]
        rows, cols = [0, 0, 1, -1], [1, -1, 0, 0]
        visited = [[0] * width for _ in range(height)]
        visited[sr][sc] = 1
        q = deque([(sr, sc)])

        while q:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                new_x, new_y = cur_x + rows[i], cur_y + cols[i]

                if 0 <= new_x < height and 0 <= new_y < width and not visited[new_x][new_y]:
                    if image[new_x][new_y] == target_color:
                        areas.append((new_x, new_y))
                        visited[new_x][new_y] = 1
                        q.append((new_x, new_y))

        for area in areas:
            x, y = area
            image[x][y] = newColor

        return image
