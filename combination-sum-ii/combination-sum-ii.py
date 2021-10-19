from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dict1 = {}
        for candi in candidates:
            if candi not in dict1:
                dict1[candi] = 1
            else:
                dict1[candi] += 1

        candidates = sorted(list(set(candidates)))
        max_index = len(candidates)
        answer = []

        def dfs(index, cur_sum, seq):
            if cur_sum == target:
                answer.append(seq[:])
                return

            if cur_sum > target or index == max_index:
                return

            if dict1[candidates[index]]:
                dict1[candidates[index]] -= 1
                dfs(index, cur_sum + candidates[index], seq + [candidates[index]])
                dict1[candidates[index]] += 1
            dfs(index + 1, cur_sum, seq)

        dfs(0, 0, [])
        return answer
