from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if not coins:
            return -1

        coins.sort()

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            coin = coins[i]
            for j in range(amount + 1):
                if j >= coin:
                    dp[j] = min(dp[j], dp[j - coin] + 1)

        return -1 if dp[-1] == float("inf") else dp[-1]