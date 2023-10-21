# 조건: s1를 n개로 쪼개면 s2는 n-1, n, n+1로 쪼개야 함
# 이 조건은 의미가 없음
# 예를 들어 s1을 4개로, s2를 2개로 쪼개서 s3를 만들 수 있다고 가정하면
# s1 2개는 붙어있게 되는데 이걸 붙이면 s1 3개로, s2를 2개로 쪼개서 s3를 만든것과 동일함
# 즉 쪼개는 갯수와 상관 없이 만들 수만 있으면 됨...


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        left_len, right_len = len(s1), len(s2)
        target_len = len(s3)
        if left_len + right_len != target_len:
            return False

        # dp = [[False] * (right_len + 1) for _ in range(left_len + 1)]
        dp = [False] * (right_len + 1)

        dp[0] = True

        for i in range(1, right_len + 1):
            dp[i] = dp[i - 1] and (s2[i - 1] == s3[i - 1])

        for i in range(1, left_len + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, right_len + 1):
                r1, r2 = False, False
                if s1[i - 1] == s3[i + j - 1]:
                    r1 = dp[j]
                if s2[j - 1] == s3[i + j - 1]:
                    r2 = dp[j - 1]

                dp[j] = r1 or r2

        # print()
        # for item in dp:
        #     print(item)

        return dp[-1]
