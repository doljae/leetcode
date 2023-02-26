from collections import defaultdict, deque
from typing import *


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        reversed_graph = defaultdict(set)
        in_degree = [0] * len(graph)
        q = deque([])

        for target_node, nodes in enumerate(graph):
            for node in nodes:
                reversed_graph[node].add(target_node)
                in_degree[target_node] += 1

        for node, value in enumerate(in_degree):
            if value == 0:
                q.append(node)

        result = []
        while q:
            cur_node = q.popleft()

            for node in reversed_graph[cur_node]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
            result.append(cur_node)

        return sorted(result)