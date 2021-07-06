from typing import *
from collections import defaultdict


class Solution:
    answer = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1 = defaultdict(set)
        for item in prerequisites:
            src, dsc = item
            if src == dsc:
                return False
            dict1[src].add(dsc)

        visited, finished = set(), set()

        def dfs(cur_node):
            visited.add(cur_node)
            for adj_node in dict1[cur_node]:
                if adj_node not in visited:
                    dfs(adj_node)
                elif adj_node not in finished:
                    self.answer = True
            finished.add(cur_node)

        for node in range(numCourses):
            if node not in visited:
                dfs(node)
        return not self.answer
