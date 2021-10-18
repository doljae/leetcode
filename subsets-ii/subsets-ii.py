from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()

        def dfs(cur, seq):
            if cur == len(nums):
                answer.add(tuple(seq[:]))
                return

            dfs(cur + 1, seq + [nums[cur]])
            dfs(cur + 1, seq)

        dfs(0, [])
        return list(map(lambda x: list(x), list(answer)))