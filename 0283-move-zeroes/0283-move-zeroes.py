#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> list[int]:
        last_zero_index = 0

        for i, num in enumerate(nums):
            if num == 0:
                if last_zero_index == -1:
                    last_zero_index = i
            else:
                nums[last_zero_index] = num
                last_zero_index += 1

        for i in range(last_zero_index, len(nums)):
            nums[i] = 0

        return nums