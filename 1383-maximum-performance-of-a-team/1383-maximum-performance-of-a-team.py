import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiency_and_speed = zip(efficiency, speed)
        efficiency_and_speed = sorted(efficiency_and_speed, key=lambda x: x[0], reverse=True)

        sum_of_speed, result = 0, 0
        heap = []
        for efficiency, speed in efficiency_and_speed:
            sum_of_speed += speed
            heapq.heappush(heap, speed)

            if len(heap) > k:
                sum_of_speed -= heapq.heappop(heap)

            result = max(result, sum_of_speed * efficiency)
            
        return result % (pow(10, 9) + 7)
