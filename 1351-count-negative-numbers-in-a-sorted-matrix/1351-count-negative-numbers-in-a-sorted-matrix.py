from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            board = grid[i]
            left, right = 0, len(board) - 1

            while left <= right:
                mid = (left + right) // 2
                if board[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

            result += (len(board) - left)

        return result