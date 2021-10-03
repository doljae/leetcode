from collections import deque
from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque([(sr, sc)])
        visited = {(sr, sc)}
        spreadable_color = image[sr][sc]
        x, y = [1, -1, 0, 0], [0, 0, 1, -1]
        while q:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                new_x, new_y = cur_x + x[i], cur_y + y[i]

                if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]):
                    if (new_x, new_y) not in visited and image[new_x][new_y] == spreadable_color:
                        image[new_x][new_y] = newColor
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))

        image[sr][sc] = newColor

        return image