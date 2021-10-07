from typing import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        nums = [i for i in range(1, n + 1)]
        visited = [0] * n

        def dfs(pos, seq):
            if pos == n or len(seq) == k:
                answer.append(seq[:])
                return

            for i in range(pos, n):
                if not visited[i]:
                    visited[i] = 1
                    seq.append(nums[i])
                    dfs(i, seq)
                    seq.pop()
                    visited[i] = 0

        dfs(0, [])
        return answer


print(Solution().combine(4, 2))
