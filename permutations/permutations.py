from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = [0] * len(nums)
        length = len(nums)

        def dfs(seq):
            if len(seq) == length:
                answer.append(seq[:])
                return

            for i in range(length):
                if not visited[i]:
                    visited[i] = 1
                    seq.append(nums[i])
                    dfs(seq)
                    seq.pop()
                    visited[i] = 0

        dfs([])
        return answer
