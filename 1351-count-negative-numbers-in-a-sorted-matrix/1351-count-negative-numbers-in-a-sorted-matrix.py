from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        row = grid[0]
        target = len(row) - 1
        for i in range(len(grid)):

            while target >= 0 > grid[i][target]:
                target -= 1

            result += (len(row) - (target + 1))

        return result