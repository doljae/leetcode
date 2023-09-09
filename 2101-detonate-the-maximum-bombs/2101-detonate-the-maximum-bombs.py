import math
from collections import defaultdict, deque
from typing import *


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_map = defaultdict(list)
        for i in range(len(bombs)):
            x1, y1, z1 = bombs[i]
            bomb_map[i] = []
            for j in range(len(bombs)):
                x2, y2, z2 = bombs[j]
                if i == j:
                    continue

                if self.is_connected(x1, y1, z1, x2, y2):
                    bomb_map[i].append(j)

        result = 0
        for bomb in bomb_map:
            q = deque([bomb])
            visited = set()
            visited.add(bomb)
            temp_result = 1
            # print("start")
            while q:
                cur = q.popleft()
                # print(f"{cur} 터짐")

                for item in bomb_map[cur]:
                    if item in visited:
                        continue
                    visited.add(item)
                    temp_result += 1
                    q.append(item)

            result = max(result, temp_result)
            # print(result)

        return result

    def is_connected(self, x1, y1, z1, x2, y2):
        return self.distance(x1, y1, x2, y2) <= z1

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)