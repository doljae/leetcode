class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        max_length = 0
        for i in range(1, len(t) + 1):
            t1 = t[i - 1]
            for j in range(1, len(s) + 1):
                t2 = s[j - 1]

                if t1 == t2:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                max_length = max(max_length, dp[i][j])
        
        return max_length == len(s)
