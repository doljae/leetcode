import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, int(math.sqrt(n)) + 1):
            dp[i * i] = 1
        for i in range(1, n + 1):
            if dp[i]:
                continue
            else:
                temp = int(math.sqrt(i))
                dp[i] = dp[temp] + dp[i - temp]
                for j in range(1, temp + 1):
                    dp[i] = min(dp[i], dp[j * j] * (i // (j * j)) + dp[i % (j * j)])
        # print(dp)
        return dp[n]