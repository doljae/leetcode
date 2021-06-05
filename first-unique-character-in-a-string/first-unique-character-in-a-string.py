from typing import *
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for char in s:
            dict1[char] += 1
        min_val = float("inf")
        min_key_index = 0
        for key in dict1:
            if dict1[key] < min_val:
                min_val, min_key_index = dict1[key], s.index(key)
        if min_val != 1:
            return -1
        return min_key_index
