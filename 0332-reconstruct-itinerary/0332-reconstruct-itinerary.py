from collections import defaultdict
from typing import *


class Solution:
    def __init__(self):
        self.board = defaultdict(list)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        for ticket in tickets:
            src, dsc = ticket
            self.board[src].append(dsc)

        for item in self.board:
            self.board[item].sort(reverse=True)

        def dfs(cur, result):
            while self.board[cur]:
                new = self.board[cur].pop()
                dfs(new, result)
            result.append(cur)

        result = []
        dfs("JFK", result)

        return result[::-1]
