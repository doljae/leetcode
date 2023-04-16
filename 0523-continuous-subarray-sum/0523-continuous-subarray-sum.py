#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: 0}
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True
            # print(hash_map)
        return False

