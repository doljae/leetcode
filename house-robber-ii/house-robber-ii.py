from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(nums, i, j):
            rob1, rob2 = 0, 0
            for index in range(i, j):
                rob1, rob2 = rob2 + nums[index], max(rob1, rob2)

            return max(rob1, rob2)

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(help(nums, 1, len(nums)), help(nums, 0, len(nums) - 1))
