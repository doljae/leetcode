#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        width = len(nums)
        board = [0] * (width + 1)

        for i in range(1, width + 1):
            board[i] = board[i - 1] + nums[i - 1]

        s = set()

        for i in range(2, width+1):
            s.add(board[i - 2] % k)
            if board[i] % k in s:
                return True

        return False