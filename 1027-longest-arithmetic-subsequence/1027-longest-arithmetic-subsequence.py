from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2:
            return n

        result = 2
        board = [{} for _ in range(n)]

        for i in range(len(nums)):
            for j in range(i):
                gap = nums[i] - nums[j]
                board[i][gap] = board[j].get(gap, 1) + 1

                result = max(result, board[i][gap])

        return result