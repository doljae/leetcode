from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses in [0, 1] or not prerequisites:
            return True

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for item in prerequisites:
            b, a = item
            graph[a].append(b)
            if b not in graph:
                graph[b] = []
            indegree[b] += 1
            if a not in indegree:
                indegree[a] = 0
                
        q = deque([])
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)

        if not q:
            return False

        while q:
            cur = q.popleft()
            for adj in graph[cur]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        for key in indegree:
            if indegree[key] != 0:
                return False
            
        return True