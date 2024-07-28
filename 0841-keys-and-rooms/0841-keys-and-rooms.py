from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque(rooms[0])
        visited = set()
        visited.add(0)

        while q:
            cur = q.popleft()

            if cur in visited:
                continue

            visited.add(cur)
            q.extend(rooms[cur])

        return len(visited) == len(rooms)