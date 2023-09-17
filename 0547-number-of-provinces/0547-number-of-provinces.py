from collections import defaultdict, deque
from typing import *


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num_of_provinces = 0
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            graph[i] = [x for x in range(len(isConnected[i])) if isConnected[i][x] == 1 and x != i]

        for i in range(len(isConnected)):
            if i in visited:
                continue

            visited.add(i)
            q = deque([i])

            while q:
                cur = q.popleft()
                for adj in graph[cur]:
                    if adj in visited:
                        continue
                    visited.add(adj)
                    q.append(adj)

            num_of_provinces += 1

        return num_of_provinces
