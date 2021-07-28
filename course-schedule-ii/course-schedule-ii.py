from typing import *
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        graph = defaultdict(set)
        degree = [0] * numCourses

        for i in range(numCourses):
            graph[i] = set()

        for item in prerequisites:
            dsc, src = item
            graph[src].add(dsc)
            degree[dsc] += 1

        q = deque([])
        answer = []
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            answer.append(cur)
            for adj in graph[cur]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    q.append(adj)

        return answer if len(answer) == numCourses else []