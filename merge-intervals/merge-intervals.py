from typing import *
from collections import deque


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        q = deque(intervals)
        answer = []

        while q:
            start, end = q.popleft()
            while q and end >= q[0][0]:
                end = max(end, q.popleft()[1])
            answer.append([start, end])
        
        return answer
