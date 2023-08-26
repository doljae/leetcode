from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    result += 1

        return result
