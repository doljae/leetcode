class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        if len(s) == 1:
            return 1
        elif len(s) == 2:
            return len(s) + 1 if s[0] == s[1] else len(s)

        dp = [[0] * len(s) for _ in range(len(s) + 1)]

        for i in range(len(s)):
            dp[1][i] = 1

        for i in range(len(s) - 2 + 1):
            dp[2][i] = 1 if s[i] == s[i + 1] else 0

        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                dp[length][i] = 1 if s[i] == s[i + length - 1] and dp[length - 2][i + 1] == 1 else 0
        for item in dp:
            answer += sum(item)

        return answer