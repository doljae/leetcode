#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = deque([])
        window_sum = 0
        window_len = 0
        result = float("inf")

        for num in nums:
            window.append(num)
            window_sum += num
            window_len += 1

            while window and window_sum >= target:
                result = min(result, window_len)
                temp = window.popleft()
                window_sum -= temp
                window_len -= 1

            if result == 1:
                return result

        return 0 if result == float("inf") else result