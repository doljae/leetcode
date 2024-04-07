from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(cur: List, remain: int, start: int):
            if remain == 0:
                result.append(cur.copy())
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                remain -= candidates[i]
                cur.append(candidates[i])
                dfs(cur, remain, i)
                cur.pop()
                remain += candidates[i]

        dfs([], target, 0)

        return result