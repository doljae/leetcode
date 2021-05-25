from typing import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        height, width = len(matrix), len(matrix[0])

        def count(number):
            x, y = 0, height - 1
            cnt = 0
            while x < height and y >= 0:
                if matrix[x][y] < number:
                    cnt += (y + 1)
                    x += 1
                else:
                    y -= 1
            return cnt

        def solution():
            low, high = matrix[0][0], matrix[-1][-1]
            while low <= high:
                mid = (low + high) // 2
                if count(mid) >= k:
                    high = mid - 1
                else:
                    low = mid + 1
            return high

        return solution()
