

class Solution:
    def createGraph(self, routes):
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if self.haveCommonNode(routes[i], routes[j]):
                    self.adjList[i].append(j)
                    self.adjList[j].append(i)

    def haveCommonNode(self, route1, route2):
        i, j = 0, 0
        while i < len(route1) and j < len(route2):
            if route1[i] == route2[j]:
                return True
            if route1[i] < route2[j]:
                i += 1
            else:
                j += 1
        return False

    def addStartingNodes(self, q, routes, source):
        for i in range(len(routes)):
            if self.isStopExist(routes[i], source):
                q.append(i)

    def isStopExist(self, route, stop):
        return stop in route

    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        for i in range(len(routes)):
            routes[i].sort()

        self.adjList = [[] for _ in range(501)]
        self.createGraph(routes)

        q = deque()
        self.addStartingNodes(q, routes, source)

        vis = [0] * len(routes)
        busCount = 1

        while q:
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if target in routes[node]:
                    return busCount

                for adj in self.adjList[node]:
                    if not vis[adj]:
                        vis[adj] = 1
                        q.append(adj)

            busCount += 1

        return -1

