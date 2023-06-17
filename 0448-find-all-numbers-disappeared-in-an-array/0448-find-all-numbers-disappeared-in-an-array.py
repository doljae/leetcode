#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            cur = abs(nums[i]) - 1
            if nums[cur] > 0:
                nums[cur] *= -1

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result