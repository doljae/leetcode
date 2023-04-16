#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import *


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_map, bottom_map = defaultdict(set), defaultdict(set)

        for index in range(len(tops)):
            top_map[tops[index]].add(index)
            bottom_map[bottoms[index]].add(index)

        result = float('inf')
        for key in top_map:
            u = top_map[key].union(bottom_map[key])
            i = top_map[key].intersection(bottom_map[key])
            if len(u) == len(tops):
                result = min(result, min(len(top_map[key] - i), len(bottom_map[key] - i)))

        if result == float('inf'):
            return -1
        return result