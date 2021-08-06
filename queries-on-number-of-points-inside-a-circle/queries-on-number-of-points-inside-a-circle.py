from typing import *


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []

        for query in queries:
            cx, cy, length = query
            temp = 0
            for point in points:
                x, y = point
                if (cx - x) ** 2 + (cy - y) ** 2 <= length ** 2:
                    temp += 1
            answer.append(temp)

        return answer