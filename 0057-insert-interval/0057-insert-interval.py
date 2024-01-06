from collections import deque
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        board = [(newInterval[0], "in"), (newInterval[1], "out")]
        for interval in intervals:
            start, end = interval
            board.append((start, "in"))
            board.append((end, "out"))

        board.sort(key=lambda x: (x[0], (x[1] == "out")))

        result = []
        temp = deque([])
        start_cnt, end_cnt = 0, 0
        while board:
            cur_val, cur_flag = board.pop()
            if cur_flag == "in":
                temp.appendleft(cur_val)
                start_cnt += 1
            else:
                if temp and cur_val != temp[0] and start_cnt == end_cnt:
                    result.append([temp[0], temp[-1]])
                    temp = deque([cur_val])
                    start_cnt, end_cnt = 0, 1
                elif temp and cur_val == temp[0]:
                    end_cnt += 1
                else:
                    temp.appendleft(cur_val)
                    end_cnt += 1
        if temp:
            result.append([temp[0], temp[-1]])

        return sorted(result)