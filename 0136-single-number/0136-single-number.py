#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = set([])
        for num in nums:
            if num in check:
                check.remove(num)
            else:
                check.add(num)

        return check.pop()
