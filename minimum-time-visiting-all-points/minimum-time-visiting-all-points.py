from typing import *


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0

        for i in range(len(points) - 1):
            answer += max(map(abs, (points[i + 1][0] - points[i][0], points[i + 1][1] - points[i][1])))

        return answer
