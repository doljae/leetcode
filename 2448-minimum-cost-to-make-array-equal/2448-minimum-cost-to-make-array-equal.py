from typing import *


# Weighted median

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0

        board = []
        for i in range(len(nums)):
            board.append((nums[i], cost[i]))
        board.sort()

        total, cnt = sum(cost), 0
        target = 0
        for item in board:
            num, weight = item
            cnt += weight
            if cnt > total // 2:
                target = num
                break

        return sum(abs(num - target) * weight for num, weight in board)