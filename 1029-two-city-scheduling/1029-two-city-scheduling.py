from typing import *


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        board = sorted(costs, key=lambda x: (abs(x[1] - x[0]), x[0], x[1]), reverse=True)

        a = b = len(costs) // 2
        result = 0
        for cost in board:
            a_site_cost, b_site_cost = cost
            if a_site_cost >= b_site_cost:
                if b > 0:
                    b -= 1
                    result += b_site_cost
                else:
                    a -= 1
                    result += a_site_cost
            else:
                if a > 0:
                    a -= 1
                    result += a_site_cost
                else:
                    b -= 1
                    result += b_site_cost
        return result