#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *


def is_covered(s1, e1, s2, e2):
    return s2 <= s1 and e1 <= e2


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = []

        for interval in intervals:
            start, end = interval

            if not result:
                result.append(interval)
            else:
                s1, e1 = result[-1]
                if is_covered(start, end, s1, e1):
                    continue
                if is_covered(s1, e1, start, end):
                    result.pop()
                result.append(interval)
        return len(result)
