from collections import deque
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        board = []
        if not intervals:
            return [newInterval]
        for interval in intervals:
            start, end = interval
            board.append((start, "start"))
            board.append((end, "end"))
        new_interval_start, new_interval_end = newInterval
        new_interval_start_flag = False
        new_interval_end_flag = False
        # print(board)
        if board and board[0][0] >= new_interval_start:
            board = [(new_interval_start, "start")] + board
            new_interval_start_flag = True
            # print(1)
        for i in range(len(board) - 1):
            if new_interval_start_flag is False and board[i][0] <= new_interval_start <= board[i + 1][0]:
                board = board[:i] + [(new_interval_start, "start")] + board[i:]
                new_interval_start_flag = True
                # print(1)
            if new_interval_end_flag is False and board[i][0] <= new_interval_end <= board[i + 1][0]:
                board = board[:i] + [(new_interval_end, "end")] + board[i:]
                new_interval_end_flag = True
                # print(2)
        if not new_interval_start_flag:
            board.append((new_interval_start, "start"))
        if not new_interval_end_flag:
            board.append((new_interval_end, "end"))
        board.sort(key=lambda x: (x[0], (x[1] == "end")))
        # print(board)

        result = []
        temp = deque([])
        start_cnt, end_cnt = 0, 0
        while board:
            # print(temp)
            cur_val, cur_flag = board.pop()
            if cur_flag == "start":
                temp.appendleft(cur_val)
                start_cnt += 1
            else:
                if temp and cur_val != temp[0] and start_cnt == end_cnt:
                    result.append([temp[0], temp[-1]])
                    start_cnt, end_cnt = 0, 1
                    temp = deque([])
                    temp.appendleft(cur_val)
                elif temp and cur_val == temp[0]:
                    end_cnt += 1
                else:
                    temp.appendleft(cur_val)
                    end_cnt += 1
        if temp:
            result.append([temp[0], temp[-1]])

        return sorted(result)