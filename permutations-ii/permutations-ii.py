from typing import *


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        visited = [0] * len(nums)
        answer = set()

        def dfs(cur, seq):
            if cur == len(nums):
                answer.add(tuple(seq[:]))
                return

            for i in range(0, len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    seq.append(nums[i])
                    dfs(cur + 1, seq)
                    visited[i] = 0
                    seq.pop()

        dfs(0, [])

        return list(map(lambda x: list(x), list(answer)))
