#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2]) - 1

        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        print(nums)