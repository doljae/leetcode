class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = {}
        in_degree = {}
        min_degree = float("inf")
        for i in range(n):
            graph[i] = set()
            in_degree[i] = 0

        for edge in edges:
            src, dsc = edge
            graph[src].add(dsc)
            in_degree[dsc] += 1

        for node in graph:
            min_degree = min(min_degree, in_degree[node])

        candi = []
        for node in graph:
            if in_degree[node] == min_degree:
                candi.append(node)

        return candi