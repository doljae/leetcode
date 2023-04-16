#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import *


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top, bottom = defaultdict(set), defaultdict(set)

        for index in range(len(tops)):
            top[tops[index]].add(index)
            bottom[bottoms[index]].add(index)

        result = float('inf')
        for key in top:
            u = top[key].union(bottom[key])
            i = top[key].intersection(bottom[key])
            if len(u) == len(tops):
                result = min(result, min(len(top[key] - i), len(bottom[key] - i)))

        if result == float('inf'):
            return -1
        return result