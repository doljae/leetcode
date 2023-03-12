from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        length = len(grid)
        visited = [[0] * length for _ in range(length)]
        pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        island_list = []

        for i in range(length):
            for j in range(length):
                if not visited[i][j] and grid[i][j]:
                    visited[i][j] = 1
                    island = [(i, j)]
                    q = deque([(i, j)])

                    while q:
                        cur_x, cur_y = q.popleft()
                        for x, y in pos:
                            new_x, new_y = cur_x + x, cur_y + y
                            if 0 <= new_x < length and 0 <= new_y < length and not visited[new_x][new_y] and \
                                    grid[new_x][new_y]:
                                visited[new_x][new_y] = 1
                                island.append((new_x, new_y))
                                q.append((new_x, new_y))
                    island_list.append(island)

                else:
                    visited[i][j] = 1

        result = float("inf")
        dist = [[0] * length for _ in range(length)]
        visited2 = [[0] * length for _ in range(length)]
        initial_islands = [[0] * length for _ in range(length)]
        island_one, island_two = island_list
        q = deque([])
        for x, y in island_one:
            visited2[x][y] = 1
            initial_islands[x][y] = 1
            q.append((x, y))
        for x, y in island_two:
            visited2[x][y] = 1
            initial_islands[x][y] = 2
            q.append((x, y))

        while q:
            cur_x, cur_y = q.popleft()
            for x, y in pos:
                new_x, new_y = cur_x + x, cur_y + y

                if not 0 <= new_x < length or not 0 <= new_y < length:
                    continue
                if initial_islands[new_x][new_y]:
                    continue
                if visited2[new_x][new_y]:
                    continue
                else:
                    dist[new_x][new_y] = dist[cur_x][cur_y] + 1
                    visited2[new_x][new_y] = 1
                    initial_islands[new_x][new_y] = initial_islands[cur_x][cur_y]
                    q.append((new_x, new_y))

        for cur_x in range(length):
            for cur_y in range(length):
                for x, y in pos:
                    new_x, new_y = cur_x + x, cur_y + y

                    if not 0 <= new_x < length or not 0 <= new_y < length:
                        continue

                    if initial_islands[cur_x][cur_y] != initial_islands[new_x][new_y]:
                        result = min(result, dist[cur_x][cur_y] + dist[new_x][new_y])
        return result