from typing import *


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()

        def dfs(cur):
            visited.add(cur)

            for i in range(len(isConnected)):
                if i not in visited and isConnected[cur][i]:
                    dfs(i)

            return 1

        answer = 0
        for i in range(len(isConnected)):
            if i not in visited:
                answer += dfs(i)
        return answer
