from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        board = defaultdict(int)

        for num in nums:
            if num not in board:
                board[num] = 2
            else:
                board[num] -= 1

        for num in board:
            if board[num] == 2:
                return num