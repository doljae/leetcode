from typing import *


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def switch(input_list):
            return list(map(lambda x: 1 if x == 0 else 0, input_list))

        height, width = len(grid), len(grid[0])

        for i in range(height):
            if grid[i][0] == 0:
                result = switch(grid[i])
                grid[i] = result

        for j in range(1,width):
            temp = []
            for i in range(height):
                temp.append(grid[i][j])
            result = None
            if height - sum(temp) > height // 2:
                result = switch(temp)
            if result:
                for i in range(height):
                    grid[i][j] = result[i]
        for item in grid:
            print(item)
        answer = 0
        for i in range(height):
            temp = grid[i]
            temp = list(map(str, temp))
            answer += int("".join(temp), 2)

        return answer
