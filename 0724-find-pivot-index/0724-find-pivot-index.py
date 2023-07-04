#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == sum_ - left_sum - num:
                return i
            else:
                left_sum += num
        return -1
