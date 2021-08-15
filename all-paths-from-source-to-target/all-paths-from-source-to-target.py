from typing import *


class Solution:
    def allPathsSourceTarget(self, input_list: List[List[int]]) -> List[List[int]]:
        graph = {}
        length = len(input_list)

        for i in range(length):
            graph[i] = set(input_list[i])
        answer = []

        def dfs(cur, seq):
            if cur == length - 1:
                answer.append(seq[::])

            else:
                for adj in graph[cur]:
                    seq.append(adj)
                    dfs(adj, seq)
                    seq.pop()

        dfs(0, [0])
        return answer
