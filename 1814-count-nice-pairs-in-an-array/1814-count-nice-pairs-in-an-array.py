from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(str(num)[::-1])

        result = 0
        converted = []
        board = defaultdict(int)

        for num in nums:
            temp = num - rev(num)
            converted.append(temp)

        for i in range(len(converted)):
            if converted[i] in board:
                result += board[converted[i]]
            board[converted[i]] += 1

        return result % (pow(10, 9) + 7)