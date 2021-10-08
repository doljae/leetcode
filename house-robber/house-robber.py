from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        dp[0][0], dp[0][1] = 0, nums[0]
        dp[1][0], dp[1][1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = max(dp[i - 2]) + nums[i]

        return max(dp[-1])
