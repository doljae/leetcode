# 조건: s1를 n개로 쪼개면 s2는 n-1, n, n+1로 쪼개야 함
# 이 조건은 의미가 없음
# 예를 들어 s1을 4개로, s2를 2개로 쪼개서 s3를 만들 수 있다고 가정하면
# s1 2개는 붙어있게 되는데 이걸 붙이면 s1 3개로, s2를 2개로 쪼개서 s3를 만든것과 동일함
# 즉 쪼개는 갯수와 상관 없이 만들 수만 있으면 됨...
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(left, right):
            if left == len(s1) and right == len(s2):
                return True

            t1, t2 = False, False

            if left < len(s1) and s1[left] == s3[left + right]:
                t1 = dfs(left + 1, right)

            if right < len(s2) and s2[right] == s3[left + right]:
                t2 = dfs(left, right + 1)

            return t1 or t2

        return dfs(0, 0)
