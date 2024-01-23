"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if not node.neighbors:
            return copy.deepcopy(node)

        graph = collections.defaultdict(set)
        visited = set()
        start_val = node.val
        q = collections.deque([node])

        while q:
            node = q.popleft()
            visited.add(node.val)
            for adj in node.neighbors:
                if adj.val not in visited:
                    q.append(adj)
                    graph[adj.val].add(node.val)
                    graph[node.val].add(adj.val)

        graph2 = {}
        for key in graph:
            graph2[key] = Node(key, [])

        for key in graph:
            for adj in graph[key]:
                graph2[key].neighbors.append(graph2[adj])

        return graph2[start_val]