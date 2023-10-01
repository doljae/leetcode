from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

 

        result = 2
        board = [{} for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                gap = nums[i] - nums[j]
                board[i][gap] = board[j].get(gap, 1) + 1

                result = max(result, board[i][gap])

        return result