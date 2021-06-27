class Solution:

    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2, 5]

        def sol(val):
            answer = 0
            start, end = 0, val - 1
            while start < val:
                answer += dp[start] * dp[end]
                start += 1
                end -= 1
            return answer

        if n < len(dp):
            return dp[n]
        else:
            for i in range(4, n + 1):
                dp.append(sol(i))
            return dp[n]