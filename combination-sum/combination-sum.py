from typing import *


# DP로 풀어야할 것 같다
# 완전탐색으로 하면 반드시 TLE가 날 것 같은 문제
# 라고 생각했는데 노트에 써보니깐 백트래킹 문제 같다.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        set1 = set()

        def dfs(cur):
            if sum(cur) >= target:
                if sum(cur) == target:
                    if "".join(list(map(str, sorted(cur)))) not in set1:
                        answer.append(cur[:])
                        set1.add("".join(list(map(str, sorted(cur)))))
                return

            for candidate in candidates:
                cur.append(candidate)
                dfs(cur)
                cur.pop()

        dfs([])

        return answer