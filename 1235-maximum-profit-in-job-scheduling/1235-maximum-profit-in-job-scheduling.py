from heapq import heappush, heappop
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted((startTime[i], endTime[i], profit[i]) for i in range(len(startTime)))

        heap, cur_profit, max_profit = [], 0, 0

        for start_time, end_time, profit in jobs:
            while heap and heap[0][0] <= start_time:
                temp_end_time, temp_profit = heappop(heap)
                cur_profit = max(cur_profit, temp_profit)
                
            new_profit = cur_profit + profit
            heappush(heap, (end_time, new_profit))
            max_profit = max(max_profit, new_profit)

        return max_profit
