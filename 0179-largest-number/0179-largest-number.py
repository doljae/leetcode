#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class LargestNum(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        largest_num = "".join(sorted(str_nums, key=LargestNum))

        return "0" if largest_num[0] == "0" else largest_num