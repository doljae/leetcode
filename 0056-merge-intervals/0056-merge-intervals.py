from collections import deque
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = deque(sorted(intervals))

        while intervals:
            cur_left, cur_right = intervals.popleft()

            if not result:
                result.append([cur_left, cur_right])
            else:
                prev_left, prev_right = result[-1]
                if prev_right < cur_left:
                    result.append([cur_left, cur_right])
                elif prev_right >= cur_left:
                    result[-1][1] = max(prev_right, cur_right)
                elif prev_left <= cur_left <= cur_right <= prev_right:
                    pass

        return result
