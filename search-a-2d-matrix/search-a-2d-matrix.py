from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height, width = len(matrix), len(matrix[0])

        start, end = 0, height * width - 1

        while start <= end:
            mid = start + (end - start) // 2
            cur = matrix[mid // width][mid % width]

            if cur == target:
                return True
            elif cur < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False